with open('index.html', 'r', encoding='utf-8') as f:
    home_html = f.read()

# Extract script blocks
start_marker = '// FORMULÁRIO CTA FINAL'
end_marker = '})();' # at the very end of initWaFab

start_idx = home_html.find(start_marker)
end_idx = home_html.find(end_marker, start_idx) + 5
js_code = home_html[start_idx:end_idx]

with open('public/agentejuridico/index.html', 'r', encoding='utf-8') as f:
    target_html = f.read()

# Inject Supabase library
supabase_lib = '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>'
if supabase_lib not in target_html:
    target_html = target_html.replace(
        '<script src="https://cdn.jsdelivr.net/npm/lucide@latest"></script>',
        '<script src="https://cdn.jsdelivr.net/npm/lucide@latest"></script>\n' + supabase_lib
    )

# Inject JS scripts before </body>
script_tag = f"<script>\n{js_code}\n</script>\n"
if 'initCtaFinalForm' not in target_html:
    target_html = target_html.replace('</body>', script_tag + '</body>')

with open('public/agentejuridico/index.html', 'w', encoding='utf-8') as f:
    f.write(target_html)

print("Fix scripts and libs completed successfully.")
