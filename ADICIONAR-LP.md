# Manual — Adicionar uma nova LP ao site (juris8.ai/&lt;caminho&gt;)

Processo usado para o `/DET`, `/newsletter`, `/crm` e `/secretariajuridica`:
clonar um repositório com uma LP estática e publicá-la como uma rota do site
principal, sem passar pelo bundler.

## Como funciona

- O site principal é um projeto Vite. **Tudo que está em `public/` é copiado
  como está para o build final** (`dist/`) e servido na raiz do domínio.
- Uma LP em `public/minha-lp/` vira `https://juris8.ai/minha-lp`.
- O deploy é automático: push na branch `main` → Vercel builda e publica.
- O `vercel.json` já tem `"trailingSlash": true`, que redireciona
  `/minha-lp` → `/minha-lp/` em produção (sem isso o CSS da LP quebra e a
  página aparece "toda branca").

## Pré-requisito: a LP precisa ser estática e auto-contida

Serve qualquer repo que tenha:

- `index.html` pronto (não precisa de build/React/npm)
- CSS e imagens no próprio repo, referenciados com **caminhos relativos**
  (`href="css/styles.css"`, `src="images/logo.png"` — sem `/` no começo)
- Dependências externas só via CDN (Google Fonts, Supabase, Lucide etc.)

Se o repo for um app React/Vite com `package.json`, é outro processo:
buildar primeiro e copiar só o `dist/` gerado (caso do embed do DET).

## Passo a passo

### 0. Escolha o caminho da URL

- Minúsculas, **sem acento**, sem espaço: `minha-lp`, `crm`, `newsletter`.
- Maiúsculas funcionam (`/DET`), mas aí a URL só responde com maiúsculas —
  `/det` dá 404. Prefira minúsculas.
- Se quiser que uma variante com acento funcione, veja a seção
  [URL com acento](#url-com-acento).

### 1. Clone o repositório (fora do projeto)

```bash
git clone --depth 5 https://github.com/eucaiogomes/NOME-DO-REPO C:/temp/NOME-DO-REPO
```

### 2. Confira a estrutura e os caminhos

```bash
# o que tem no repo
ls C:/temp/NOME-DO-REPO

# tem caminho absoluto? (o resultado precisa ser 0)
grep -c 'src="/\|href="/\|url(/' C:/temp/NOME-DO-REPO/index.html

# o que o CSS referencia (imagens de fundo etc.)
grep -oE 'url\([^)]*\)' C:/temp/NOME-DO-REPO/css/*.css | grep -v 'gradient\|data:'
```

- **Caminho absoluto encontrado** (`src="/images/..."`): troque para relativo
  (`src="images/..."`) ou a LP vai procurar o arquivo na raiz do site.
- **`url(...)` no CSS**: só confirme que a pasta referenciada será copiada
  mantendo a mesma estrutura de pastas.

### 3. Copie para `public/<caminho>/`

Copie **apenas o que a página usa**: `index.html` + pastas/arquivos de assets
(css, images, logo…).

```bash
mkdir -p public/minha-lp
cp C:/temp/NOME-DO-REPO/index.html public/minha-lp/
cp -r C:/temp/NOME-DO-REPO/css C:/temp/NOME-DO-REPO/images public/minha-lp/
```

**Não copie:** `.git/`, `README.md`, `.gitignore`, `.thumbnail`, screenshots
soltos de documentação, nem comentários `<!-- @dsCard ... -->` no topo do
HTML (metadado de design system — pode apagar a linha).

### 4. Registre a rota no `vite.config.js`

Só adicionar o nome da pasta na lista (isso faz o `npm run dev` local
redirecionar `/minha-lp` → `/minha-lp/` igual à produção):

```js
const staticDirs = ['DET', 'newsletter', 'crm', 'secretariajuridica', 'minha-lp'];
```

### 5. Teste local

```bash
npm run dev
```

Abra `http://localhost:8080/minha-lp` e confira: estilo aplicado (fundo
escuro, não HTML cru), imagens carregando, sem erro no console.

Opcional, para conferir o pacote final:

```bash
npm run build   # depois confira que dist/minha-lp/ existe
```

### 6. Commit e push

```bash
git add public/minha-lp vite.config.js
git commit -m "adicionando LP xyz em /minha-lp"
git push origin main
```

> ⚠️ **NUNCA** inclua `Co-Authored-By: Claude ...` na mensagem do commit.
> O plano Hobby do Vercel com repo privado bloqueia o deploy de commits com
> co-autor de fora do projeto ("commit author did not have contributing
> access"). Se acontecer, reescreva a mensagem e force-push.

### 7. Confira em produção (30–60 s após o push)

```bash
curl -s -o /dev/null -L -w "%{http_code}\n" https://juris8.ai/minha-lp/
```

Ou abra no navegador (janela anônima evita cache de 404 antigo):
`https://juris8.ai/minha-lp`

## URL com acento

URLs oficiais ficam **sem acento** (acento vira `%C3%AD...` na barra do
navegador). Para a variante acentuada redirecionar, adicione no
`vercel.json` as **duas formas** — literal e percent-encoded (o Vercel só
casa a encoded, mas mantemos as duas por segurança):

```json
"redirects": [
  { "source": "/minhalpé",        "destination": "/minhalpe/", "permanent": true },
  { "source": "/minhalpé/",       "destination": "/minhalpe/", "permanent": true },
  { "source": "/minhalp%C3%A9",   "destination": "/minhalpe/", "permanent": true },
  { "source": "/minhalp%C3%A9/",  "destination": "/minhalpe/", "permanent": true }
]
```

(Para descobrir o percent-encoding de um caractere: `á`=`%C3%A1`,
`é`=`%C3%A9`, `í`=`%C3%AD`, `ó`=`%C3%B3`, `ú`=`%C3%BA`, `ç`=`%C3%A7`,
`ã`=`%C3%A3`, `õ`=`%C3%B5` — ou rode
`python -c "from urllib.parse import quote; print(quote('minhalpé'))"`.)

## Armadilhas conhecidas (já vividas aqui)

| Sintoma | Causa | Solução |
|---|---|---|
| Página "toda branca", HTML cru | Acesso sem barra final; CSS relativo quebrou | Já resolvido global: `trailingSlash: true` no `vercel.json` (produção) + middleware no `vite.config.js` (dev). Não remover. |
| Arquivos da LP faltando no deploy | `.gitignore` tem `dist` sem barra — engole **qualquer** pasta `dist`, inclusive dentro da LP | Adicionar exceção: `!public/minha-lp/pasta/dist/` (caso do embed do DET) |
| Deploy bloqueado no Vercel | Trailer `Co-Authored-By` na mensagem do commit | Reescrever mensagem sem o trailer e force-push |
| `/DET` funciona, `/det` dá 404 | URL é case-sensitive | Usar minúsculas ao divulgar; ou criar redirect no `vercel.json` |
| Redirect de URL acentuada não dispara | Vercel não casa o source com acento literal | Usar a forma percent-encoded no `source` |
| Formulário de lead não envia | LPs usam Supabase via CDN direto do navegador | Nada a fazer no site — conferir chaves/tabela no projeto Supabase da LP |

## Atalho: pedindo para o Claude

No Claude Code, dentro do projeto `juris8-guide`, basta pedir:

> clone o repositório https://github.com/eucaiogomes/NOME-DO-REPO e adicione
> no site em juris8.ai/minha-lp, igual fizemos com o DET, a newsletter e o crm

O processo todo (clone → cópia → config → teste local → commit → push →
verificação em produção) é o descrito acima.
