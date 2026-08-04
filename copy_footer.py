import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    home_html = f.read()

# 1. Extract WA FAB
wa_match = re.search(r'(<!-- ===== WHATSAPP FLUTUANTE.*?</div>\s*)\n\s*<!-- ===== NAVBAR', home_html, re.DOTALL | re.IGNORECASE)
wa_block = wa_match.group(1) if wa_match else ""

# 2. Extract CTA + FOOTER
cta_match = re.search(r'(<!-- ===== CTA FINAL.*?</footer>)', home_html, re.DOTALL | re.IGNORECASE)
cta_footer_block = cta_match.group(1) if cta_match else ""

# Read agentejuridico/index.html
with open('public/agentejuridico/index.html', 'r', encoding='utf-8') as f:
    target_html = f.read()

# Inject WA FAB right after <body>
if 'wa-fab' not in target_html and wa_block:
    target_html = target_html.replace('<body>', '<body>\n\n' + wa_block)

# Replace existing footer with CTA + FOOTER
target_html = re.sub(r'<!-- ===== FOOTER ===== -->\s*<footer.*</footer>', cta_footer_block, target_html, flags=re.DOTALL | re.IGNORECASE)
# if the target file didn't have <!-- ===== FOOTER ===== -->, let's just replace <footer ... </footer>
if cta_footer_block not in target_html:
    target_html = re.sub(r'<footer.*?</footer>', cta_footer_block, target_html, flags=re.DOTALL | re.IGNORECASE)

with open('public/agentejuridico/index.html', 'w', encoding='utf-8') as f:
    f.write(target_html)

print("Merge completed successfully.")
