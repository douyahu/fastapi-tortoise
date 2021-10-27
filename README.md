## 依赖包

* aerich Tortoise-ORM 的数据库迁移工具  
  https://github.com/tortoise/aerich

* fastapi-users 用户管理包   
  https://github.com/fastapi-users/fastapi-users   
  
* fastapi-crudrouter  路由管理包   
  https://github.com/awtkns/fastapi-crudrouter
  
* fastapi-pagination 分页包   
  https://github.com/uriyyo/fastapi-pagination


## mysql数据库参数修改
下述参数不修改，会导致同步数据库结构时报错

```shell
vi /etc/mysql/mysql.conf.d/mysqld.cnf
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
如需在后端运行，则需要在run.py中添加对应方法，并且需要在该方法上添加装饰器@typer_app.command()
然后运行：python run.py --help

## fastapi的运行
调试下，直接运行asgi.py


