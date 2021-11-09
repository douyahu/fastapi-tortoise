## 描述

tortoise 使用aiomysql驱动程序

## 依赖包

* aerich Tortoise-ORM 的数据库迁移工具  
  https://github.com/tortoise/aerich

* fastapi-users 用户管理包   
  https://github.com/fastapi-users/fastapi-users

* fastapi-crudrouter 路由管理包   
  https://github.com/awtkns/fastapi-crudrouter

* fastapi-pagination 分页包   
  https://github.com/uriyyo/fastapi-pagination

## mysql数据库参数修改

下述参数不修改，会导致同步数据库结构时报错

```shell
vi /etc/mysql/mysql.confs.d/mysqld.cnf
max_allowed_packet = 25600
```

## 初始化数据库结构

```shell
aerich init -t settings.TORTOISE_ORM
aerich init-db
```

## 日志模块

AuthenticationUser中间件，记录了所有对服务端的请求操作，并保存导数据，该操作会影响服务的性能

## Test model为测试数据模型

test路由中包含了覆盖路由的写法和临时内存路由MemoryCRUDRouter类的demo

## backend

* 如需在后端运行，则需要在run.py中添加对应方法
* 并且需要在该方法上添加装饰器@typer_app.command()
* 然后运行：python run.py --help

## 服务的运行

### fastapi的运行

* 调试模式下: python run asgi.py
* 非调试模式下：gunicorn -c gunicorn.conf.py asgi:app

### 后端脚本服务的运行

* 通过docker-compose 指定supervisor-all直接拉起来所有脚本服务
* supervisor守护指定的后端服务
  ```shell
    cp ./backend/supervisor/*.confs /etc/supervisor/confs.d/ 
    supervisorctl update 
    supervisor restart log 启动指定脚本服务
  ```


### 添加pylint检查代码
```shell
pip install pylint
pylint --rcfile=.pylintrc app
```


### 添加celery
celery对目录结构的要求十分严格
windows机器上必须加上-P eventlet启动，否则会出错，
* -n 指定当前worker名字，
* -Q 指定该worker监听一个或多个任务队列。
```shell
celery -A backend.celery.celery_app worker -l info -P eventlet -n win
```
