# Juris8 — Site principal (juris8.ai)

Site institucional da Juris8 com a home e as landing pages de cada solução,
publicado na Vercel a partir da branch `main`.

## Páginas no ar

| URL | O que é | Fonte |
|---|---|---|
| [juris8.ai](https://juris8.ai) | Home — IA jurídica + vitrine das soluções | `index.html` (raiz) |
| [juris8.ai/DET](https://juris8.ai/DET/) | LP do DET Monitor (+ `empresas.html` para grupos) | `public/DET/` |
| [juris8.ai/crm](https://juris8.ai/crm/) | LP do CRM com IA no WhatsApp | `public/crm/` |
| [juris8.ai/secretariajuridica](https://juris8.ai/secretariajuridica/) | LP da caixa de entrada com IA | `public/secretariajuridica/` |
| [juris8.ai/newsletter](https://juris8.ai/newsletter/) | LP da newsletter mensal com IA | `public/newsletter/` |
| [juris8.ai/trabalhistaempresarial](https://juris8.ai/trabalhistaempresarial/) | LP do contencioso trabalhista empresarial | `public/trabalhistaempresarial/` |

## Estrutura

```
juris8-guide/
├── index.html            ← a home (Vite exige na raiz; CSS/JS embutidos)
├── public/               ← tudo aqui é copiado como está para o site final
│   ├── favicon.ico
│   ├── DET/              ← cada LP é uma pasta autocontida
│   ├── crm/                 (index.html + css + imagens, caminhos relativos)
│   ├── newsletter/
│   ├── secretariajuridica/
│   └── trabalhistaempresarial/
├── ADICIONAR-LP.md       ← manual: como adicionar uma nova LP ao site
├── vite.config.js        ← dev server + redirect /<lp> -> /<lp>/ no local
├── vercel.json           ← trailingSlash (evita LP "toda branca") + redirects
├── arquivo/              ← material antigo fora de uso (nada é servido daqui)
├── package.json          ← scripts: npm run dev / build / preview
└── .claude/launch.json   ← config do preview do Claude Code
```

- A logo padrão da navbar em todas as páginas é o wordmark `public/DET/logo.png`
  (513×145) a 52px de altura numa navbar de 68px.
- As LPs enviam leads via Supabase direto do navegador (CDN, sem backend aqui).

## Rodar localmente

```bash
npm install
npm run dev        # http://localhost:8080 (LPs em /DET, /crm, ...)
npm run build      # gera dist/ (o que a Vercel publica)
```

## Adicionar uma nova LP

Siga o passo a passo do **[ADICIONAR-LP.md](ADICIONAR-LP.md)** — resumo:
clonar o repo da LP, copiar para `public/<caminho>/`, registrar o caminho em
`staticDirs` no `vite.config.js`, testar, commit e push.

## Deploy

Push na `main` → a Vercel builda e publica automaticamente (30–60 s).

> ⚠️ Não incluir `Co-Authored-By` na mensagem de commit — o plano Hobby da
> Vercel com repo privado bloqueia o deploy ("commit author did not have
> contributing access"). Detalhes e outras armadilhas no ADICIONAR-LP.md.
# Site-juris8---040826
