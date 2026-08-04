with open('public/agentejuridico/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Lucide script to UMD version
html = html.replace(
    '<script src="https://cdn.jsdelivr.net/npm/lucide@latest"></script>',
    '<script src="https://unpkg.com/lucide@0.511.0/dist/umd/lucide.min.js"></script>'
)

# New Navbar definition
new_navbar = """<!-- NAVBAR -->
<nav class="navbar" id="navbar">
  <div class="navbar-inner">
    <a href="/" class="nav-brand" aria-label="Juris8 — Home">
      <img src="/DET/logo.png" alt="Juris8" class="nav-logo" />
    </a>
    <div class="nav-links">
      <a href="#funcionalidades" class="nav-link">Funcionalidades</a>
      <a href="#como-funciona" class="nav-link">Como funciona</a>
      <a href="#comparativo" class="nav-link">Antes e depois</a>
      <a href="#faq" class="nav-link">FAQ</a>
    </div>
    <div class="nav-right">
      <a href="#cta" class="nav-cta nav-cta-desktop">
        <i data-lucide="arrow-right" width="13" height="13" stroke-width="1.7"></i>
        Testar gratuitamente por 7 dias
      </a>
      <button class="nav-burger" id="nav-burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="nav-mobile">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
  <div class="nav-mobile" id="nav-mobile">
    <a href="#funcionalidades">Funcionalidades</a>
    <a href="#como-funciona">Como funciona</a>
    <a href="#comparativo">Antes e depois</a>
    <a href="#faq">FAQ</a>
    <div class="nav-mobile-cta">
      <a href="#cta" class="nav-cta">
        Testar gratuitamente por 7 dias
      </a>
    </div>
  </div>
</nav>"""

# Old simplified navbar to find
old_navbar_pattern = """<!-- NAVBAR -->
<nav class="navbar">
  <div class="navbar-inner">
    <a href="/" class="nav-brand">
      <img src="/DET/logo.png" alt="Juris8" class="nav-logo" />
    </a>
    <div class="nav-links">
      <a href="#fluxo" class="nav-link">Fluxo de Trabalho</a>
      <a href="#funcionalidades" class="nav-link">Funcionalidades</a>
      <a href="#diferencial" class="nav-link">O Diferencial</a>
    </div>
    <div class="nav-right">
      <a href="#teste" class="nav-cta nav-cta-desktop">Teste grátis por 7 dias</a>
    </div>
  </div>
</nav>"""

# Replace navbar
if old_navbar_pattern in html:
    html = html.replace(old_navbar_pattern, new_navbar)
else:
    # If indentation is slightly different, fallback replace
    import re
    html = re.sub(r'<!-- NAVBAR -->\s*<nav class="navbar">.*?</nav>', new_navbar, html, flags=re.DOTALL)

with open('public/agentejuridico/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Navbar and Lucide fix completed.")
