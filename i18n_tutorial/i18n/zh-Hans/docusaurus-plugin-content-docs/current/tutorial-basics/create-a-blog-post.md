---
sidebar_position: 3
---

# 創建部落格文章

Docusaurus 為 **每篇部落格文章** 創建一個頁面，還創建一個 **部落格索引頁面**、一個 **標籤系統** 、一個 **RSS** 饋送...

## 創建您的第一篇文章

創建一個名為 `blog/2021-02-28-greetings.md` 的文件：

```md title="blog/2021-02-28-greetings.md"
---
slug: greetings
title: Greetings!
authors:
  - name: Joel Marcey
    title: Co-creator of Docusaurus 1
    url: https://github.com/JoelMarcey
    image_url: https://github.com/JoelMarcey.png
  - name: Sébastien Lorber
    title: Docusaurus maintainer
    url: https://sebastienlorber.com
    image_url: https://github.com/slorber.png
tags: [greetings]
---

Congratulations, you have made your first post!

Feel free to play around and edit this post as much you like.
```

現在有一篇新的部落格文章可以在 `http://localhost:3000/blog/greetings` 訪問。
