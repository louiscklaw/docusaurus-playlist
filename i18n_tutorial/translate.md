Translate Markdown files

Translate the pages

```bash
npm run write-translations -- --locale zh-Hans
```

```bash
mkdir -p i18n/zh-Hans/docusaurus-plugin-content-docs/current

cp -r docs/** i18n/zh-Hans/docusaurus-plugin-content-docs/current
```

```bash
mkdir -p i18n/zh-Hans/docusaurus-plugin-content-pages
cp -r src/pages/**.md i18n/zh-Hans/docusaurus-plugin-content-pages
cp -r src/pages/**.mdx i18n/zh-Hans/docusaurus-plugin-content-pages
```
