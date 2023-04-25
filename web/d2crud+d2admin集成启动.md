# d2-crud-plus与d2-admin集成启动项目

1. d2-crud-plus 和 d2-admin 都是基于 Vue.js 的前端框架，可以用来快速搭建 Web 应用。它们之间可以相互集成使用，共同开发一个项目。

2. d2-admin 是一个基于 Vue.js 和 Element UI 的后台管理系统，提供了多种组件和页面模板，可以帮助用户快速搭建一个功能完备的后台管理系统。

3. d2-crud-plus 是一个基于 Vue.js 和 Element UI 的表格组件库，可以快速生成各种样式的表格，并提供了多种功能和扩展性的接口。

## 集成启动项目
    将 d2-admin 和 d2-crud-plus 两个框架集成在一起，共同构建一个项目，并通过启动一个 Web 服务器（如 Nginx 或 Apache）来提供服务。这样用户就可以通过浏览器访问这个项目，使用其中提供的功能。

## 修改之处
1. `main.js` import `'./busienss'`
2. `business/index.js` 进行`d2-crud-plus`的初始化工作
3. 请求返回结果去掉`.data`，将`{code,msg,data}`整体传递到下层
4. `views/demo` 为示例页面


## 带权限版本
请checkout permission分支