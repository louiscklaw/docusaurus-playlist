---
sidebar_position: 2
---

# 翻譯您的網站

讓我們將 `docs/intro.md` 翻譯成法語。

## 設定 i18n

修改 `docusaurus.config.js` 以添加對 `fr` 語言的支持：

```js title="docusaurus.config.js"
module.exports = {
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'fr'],
  },
};
```

## 翻譯文檔

將 `docs/intro.md` 檔案複製到 `i18n/fr` 資料夾中：

```bash
mkdir -p i18n/fr/docusaurus-plugin-content-docs/current/

cp docs/intro.md i18n/fr/docusaurus-plugin-content-docs/current/intro.md
```

將 `i18n/fr/docusaurus-plugin-content-docs/current/intro.md` 翻譯成法語。

## 啟動您的多語言網站

在法語語言環境下啟動您的網站：

```bash
npm run start -- --locale fr
```

您的多語言網站可以在 `http://localhost:3000/fr/` 訪問，並且翻譯了 `Getting Started` 頁面。

:::caution

在開發階段，您只能同時使用一種語言。

:::

## 添加語言下拉菜單

為了在不同語言之間流暢地導航，請添加語言下拉菜單。

修改 `docusaurus.config.js` 文件：

```js title="docusaurus.config.js"
module.exports = {
  themeConfig: {
    navbar: {
      items: [
        // highlight-start
        {
          type: 'localeDropdown',
        },
        // highlight-end
      ],
    },
  },
};
```

語言下拉菜單現在出現在您的導航欄中：

![語言下拉菜單](./img/localeDropdown.png)

## 構建您的多語言網站

為特定語言構建您的網站：

```bash
npm run build -- --locale fr
```

或者，同時構建所有語言的網站：

```bash
npm run build
```
