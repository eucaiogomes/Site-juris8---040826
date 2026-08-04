with open('agente-juridico/LP---Agente-Juridico/index.html', 'r', encoding='utf-8') as f:
    user_html = f.read()

nav_end_idx = user_html.find('</nav>') + 6
footer_start_idx = user_html.find('<footer')
body_sections = user_html[nav_end_idx:footer_start_idx]

script_start_idx = user_html.find('<script', footer_start_idx)
script_end_idx = user_html.rfind('</body>')
scripts = user_html[script_start_idx:script_end_idx] if script_start_idx != -1 else ""

with open('public/agentejuridico/index.html', 'r', encoding='utf-8') as f:
    target_html = f.read()

t_nav_end_idx = target_html.find('</nav>') + 6
t_footer_start_idx = target_html.find('<footer')

new_target = target_html[:t_nav_end_idx] + '\n' + body_sections + '\n' + target_html[t_footer_start_idx:]
new_target = new_target.replace('</body>', scripts + '\n</body>')

with open('public/agentejuridico/index.html', 'w', encoding='utf-8') as f:
    f.write(new_target)

print("Merge completed successfully.")
