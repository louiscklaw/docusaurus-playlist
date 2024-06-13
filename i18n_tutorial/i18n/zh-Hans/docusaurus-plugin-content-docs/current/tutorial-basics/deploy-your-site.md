---
sidebar_position: 5
---

# 部署您的網站

Docusaurus 是一個**靜態網站產生器**（也被稱為**[Jamstack](https://jamstack.org/)**）。

它將您的網站建置為**簡單的**靜態 **HTML、JavaScript 和 CSS 檔案**。

## 建置您的網站

為**生產**建置您的網站：

```bash
npm run build
```

靜態檔案會在 `build` 資料夾中產生。

## 部署您的網站

在本地測試您的生產建置：

```bash
npm run serve
```

`build` 資料夾現在在 `http://localhost:3000/` 上提供服務。

您現在可以將 `build` 資料夾 **輕鬆部署** 到 **任何地方** ， **免費** 或非常低成本（請閱讀**[部署指南](https://docusaurus.io/docs/deployment)**）。
