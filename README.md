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

vi /etc/mysql/mysql.conf.d/mysqld.cnf
max_allowed_packet = 25600


## 初始化数据库结构

```shell
aerich init -t settings.TORTOISE_ORM
aerich init-db
```