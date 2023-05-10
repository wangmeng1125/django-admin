# 2023毕业设计

[![img](https://img.shields.io/badge/license-MIT-blue.svg)](https://gitee.com/liqianglog/django-vue-admin/blob/master/LICENSE)  [![img](https://img.shields.io/badge/python-%3E=3.7.x-green.svg)](https://python.org/)  [![PyPI - Django Version badge](https://img.shields.io/badge/django%20versions-3.2-blue)](https://docs.djangoproject.com/zh-hans/3.2/) [![img](https://img.shields.io/badge/node-%3E%3D%2012.0.0-brightgreen)](https://nodejs.org/zh-cn/) 


## 平台简介
* 前端采用[D2Admin](https://github.com/d2-projects/d2-admin) 、[Vue](https://cn.vuejs.org/)、[ElementUI](https://element.eleme.cn/)。
* 后端采用 Python 语言 Django 框架以及强大的 [Django REST Framework](https://pypi.org/project/djangorestframework)。
* 权限认证使用[Django REST Framework SimpleJWT](https://pypi.org/project/djangorestframework-simplejwt)，支持多终端认证系统。
* 支持加载动态权限菜单，多方式轻松权限控制。


## 内置功能

1.  菜单管理：配置系统菜单，操作权限，按钮权限标识、后端接口权限等。
2.  部门管理：配置系统组织机构（公司、部门、角色）。
3.  角色管理：角色菜单权限分配、数据权限分配、设置角色按部门进行数据范围权限划分。
4.  权限权限：授权角色的权限范围。
5.  用户管理：用户是系统操作者，该功能主要完成系统用户配置。
6.  接口白名单：配置不需要进行权限校验的接口。
7.  字典管理：对系统中经常使用的一些较为固定的数据进行维护。
8.  地区管理：对省市县区域进行管理。
9.  附件管理：对平台上所有文件、图片等进行统一管理。
10.  操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。
11.  [插件市场 ](https://bbs.django-vue-admin.com/plugMarket.html)：基于Django-Vue-Admin框架开发的应用和插件。

##  插件市场 🔌

- Celery异步任务：[dvadmin-celery](https://gitee.com/huge-dream/dvadmin-celery)
- 升级中心后端：[dvadmin-upgrade-center](https://gitee.com/huge-dream/dvadmin-upgrade-center)
- 升级中心前端：[dvadmin-upgrade-center-web](https://gitee.com/huge-dream/dvadmin-upgrade-center-web)

## 准备工作
~~~
Python >= 3.9.0 (推荐3.9版本)
nodejs >= 16.0 (推荐最新)
Mysql >= 8.0 (可选，默认数据库sqlite3，推荐8.0版本)
Redis(可选，最新版)
~~~

## 前端♝

```bash
# 克隆项目
git clone https://gitee.com/liqianglog/django-vue-admin.git

# 进入项目目录
cd web

# 安装依赖
npm install --registry=https://registry.npm.taobao.org

# 启动服务
npm run dev
# 浏览器访问 http://localhost:8080
# .env.development 文件中可配置启动端口等参数
# 构建生产环境
# npm run build
```



## 后端💈

~~~bash
# 1. 进入项目目录 cd backend

# 2. 在项目根目录中，复制 ./conf/env.example.py 文件为一份新的到 ./conf 文件夹下，并重命名为 env.py

# 3. 在 env.py 中配置数据库信息
	mysql数据库版本建议：8.0
	mysql数据库字符集：utf8mb4

# 4. 安装依赖环境
	pip3 install -r requirements.txt

# 5. 执行迁移命令：
	python3 manage.py makemigrations
	python3 manage.py migrate

# 6. 初始化数据
	python3 manage.py init

# 7. 初始化省市县数据:
	python3 manage.py init_area

# 8. 启动项目
	python3 manage.py runserver 0.0.0.0:8000

或使用 daphne :
  daphne -b 0.0.0.0 -p 8000 application.asgi:application
~~~

### 访问项目

- 访问地址：[http://localhost:8080](http://localhost:8080) (默认为此地址，如有修改请按照配置文件)
- 账号：`superadmin` 密码：`admin123456`





### docker-compose 运行

~~~bash
# 先安装docker-compose (自行百度安装),执行此命令等待安装，如有使用celery插件请打开docker-compose.yml中celery 部分注释
docker-compose up -d
# 初始化后端数据(第一次执行即可)
docker exec -ti dvadmin-django bash
python manage.py makemigrations 
python manage.py migrate
python manage.py init_area
python manage.py init
exit

前端地址：http://127.0.0.1:8080
后端地址：http://127.0.0.1:8080/api
# 在服务器上请把127.0.0.1 换成自己公网ip
账号：superadmin 密码：admin123456

# docker-compose 停止
docker-compose down
#  docker-compose 重启
docker-compose restart
#  docker-compose 启动时重新进行 build
docker-compose up -d --build
~~~



## 演示图✅

01-登录界面
![01-登录界面](https://github.com/wangmeng1125/django-admin/blob/master/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/WPS%E5%9B%BE%E7%89%87%E6%89%B9%E9%87%8F%E5%A4%84%E7%90%86/1%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2.png?raw=true)
02-控制台界面
![02-控制台界面](https://github.com/wangmeng1125/django-admin/blob/master/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/WPS%E5%9B%BE%E7%89%87%E6%89%B9%E9%87%8F%E5%A4%84%E7%90%86/2%E6%8E%A7%E5%88%B6%E5%8F%B0%E7%95%8C%E9%9D%A2.png?raw=true)
03-菜单管理界面
![03-菜单管理界面](https://github.com/wangmeng1125/django-admin/blob/master/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/WPS%E5%9B%BE%E7%89%87%E6%89%B9%E9%87%8F%E5%A4%84%E7%90%86/3%E8%8F%9C%E5%8D%95%E7%AE%A1%E7%90%86.png?raw=true)
04-数据可视化界面
![04-数据可视化界面](https://github.com/wangmeng1125/django-admin/blob/master/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/WPS%E5%9B%BE%E7%89%87%E6%89%B9%E9%87%8F%E5%A4%84%E7%90%86/4%E6%95%B0%E6%8D%AE%E5%8F%AF%E8%A7%86%E5%8C%96.png?raw=true)
05-模型管理界面
![05-模型管理界面](https://github.com/wangmeng1125/django-admin/blob/master/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/WPS%E5%9B%BE%E7%89%87%E6%89%B9%E9%87%8F%E5%A4%84%E7%90%86/5%E6%A8%A1%E5%9E%8B%E7%AE%A1%E7%90%86%E7%95%8C%E9%9D%A2.png?raw=true)
06-角色权限界面
![06-角色权限界面](https://github.com/wangmeng1125/django-admin/blob/master/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/WPS%E5%9B%BE%E7%89%87%E6%89%B9%E9%87%8F%E5%A4%84%E7%90%86/6%E8%A7%92%E8%89%B2%E6%9D%83%E9%99%90%E7%AE%A1%E7%90%86.png?raw=true)
07-用户管理界面
![07-用户管理界面](https://github.com/wangmeng1125/django-admin/blob/master/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/WPS%E5%9B%BE%E7%89%87%E6%89%B9%E9%87%8F%E5%A4%84%E7%90%86/7%E7%94%A8%E6%88%B7%E7%AE%A1%E7%90%86.png?raw=true)
08-地区管理界面
![08-地区管理界面](https://github.com/wangmeng1125/django-admin/blob/master/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/WPS%E5%9B%BE%E7%89%87%E6%89%B9%E9%87%8F%E5%A4%84%E7%90%86/8%E5%9C%B0%E5%8C%BA%E7%AE%A1%E7%90%86%E7%95%8C%E9%9D%A2.png?raw=true)
09-操作日志管界面
![09-操作日志管界面](https://github.com/wangmeng1125/django-admin/blob/master/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/WPS%E5%9B%BE%E7%89%87%E6%89%B9%E9%87%8F%E5%A4%84%E7%90%86/9%E6%93%8D%E4%BD%9C%E6%97%A5%E5%BF%97%E7%AE%A1%E7%90%86.png?raw=true)
10-Bug日志管理界面
![10-Bug日志管理界面](https://github.com/wangmeng1125/django-admin/blob/master/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/WPS%E5%9B%BE%E7%89%87%E6%89%B9%E9%87%8F%E5%A4%84%E7%90%86/10%E9%94%99%E8%AF%AF%E6%97%A5%E5%BF%97%E7%AE%A1%E7%90%86.png?raw=true)
