---
sidebar_position: 1
---

# 創建頁面

將 **Markdown 或 React** 文件添加到 `src/pages` 以創建 **單獨頁面** ：

- `src/pages/index.js` -> `localhost:3000/`
- `src/pages/foo.md` -> `localhost:3000/foo`
- `src/pages/foo/bar.js` -> `localhost:3000/foo/bar`

## 創建您的第一個 React 頁面

在`src/pages/my-react-page.js`中創建文件：

```jsx title="src/pages/my-react-page.js"
import React from 'react';
import Layout from '@theme/Layout';

export default function MyReactPage() {
  return (
    <Layout>
      <h1>My React page</h1>
      <p>This is a React page</p>
    </Layout>
  );
}
```

現在有一個新頁面可以在`http://localhost:3000/my-react-page`上使用。

## 創建您的第一個 Markdown 頁面

在 `src/pages/my-markdown-page.md` 中創建文件：

```mdx title="src/pages/my-markdown-page.md"
# My Markdown page

This is a Markdown page
```

現在有一個新頁面可以在 `http://localhost:3000/my-markdown-page` 上使用。
