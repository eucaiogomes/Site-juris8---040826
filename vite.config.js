import { defineConfig } from 'vite';

// LPs estáticas servidas de public/<pasta>/ (em produção o Vercel
// resolve /<pasta> -> /<pasta>/index.html via trailingSlash).
const staticDirs = ['DET', 'newsletter', 'crm', 'secretariajuridica', 'trabalhistaempresarial', 'agentejuridico', 'guia-det'];

export default defineConfig({
  server: { host: true, port: 8080 },
  appType: 'mpa',
  plugins: [
    {
      // Reproduz no dev server o redirect que o host faz em produção.
      name: 'static-dir-index',
      configureServer(server) {
        server.middlewares.use((req, res, next) => {
          if (req.url === '/DET/det-monitor-grupos' || req.url === '/DET/det-monitor-grupos/') {
            req.url = '/DET/det-monitor-grupos.html';
          } else if (req.url === '/DET/empresas' || req.url === '/DET/empresas/') {
            req.url = '/DET/empresas.html';
          }
          for (const dir of staticDirs) {
            if (req.url === `/${dir}`) {
              res.statusCode = 301;
              res.setHeader('Location', `/${dir}/`);
              res.end();
              return;
            }
            if (req.url === `/${dir}/`) {
              req.url = `/${dir}/index.html`;
            }
          }
          next();
        });
      },
    },
  ],
});
