---
sidebar_position: 1
---

# 管理文件版本

Docusaurus 可以管理您的文檔的多個版本。

## 创建文件版本

发布您的项目的 1.0 版本：

```bash
npm run docusaurus docs:version 1.0
```

`docs` 文件夹被复制到 `versioned_docs/version-1.0`，并且创建了 `versions.json`。

您的文件现在有两个版本：

- 在 `http://localhost:3000/docs/` 上的 `1.0` 版本，用於 1.0 版本的文檔
- 在 `http://localhost:3000/docs/next/` 上的 `current` 版本，用於 **即將推出、未發布的文檔**

## 添加版本下拉菜单

为了能够轻松地在版本之间导航，请添加一个版本下拉菜单。

修改 `docusaurus.config.js` 文件：

```js title="docusaurus.config.js"
module.exports = {
  themeConfig: {
    navbar: {
      items: [
        // highlight-start
        {
          type: 'docsVersionDropdown',
        },
        // highlight-end
      ],
    },
  },
};
```

文件版本下拉菜单将出现在您的导航栏中：

![文檔版本下拉菜單](./img/docsVersionDropdown.png)

## 更新现有版本

可以在各自的文件夹中编辑版本化的文件：

- 更新 `http://localhost:3000/docs/hello`，編輯 `versioned_docs/version-1.0/hello.md`
- 更新 `http://localhost:3000/docs/next/hello`，編輯 `docs/hello.md`
