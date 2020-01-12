# Some operations

* mkdir djangoapi
* pip install virtualenv  // 安装虚拟环境库
* cd djangoapi
* python3 -m venv env // 创建虚拟环境
* source venv/bin/activate  // 进入虚拟环境  deactivate  // 退出虚拟环境
* django-admin startproject night914  // Creating a django project
* cd night914
* python manage.py startapp quickstart  // Creating a django project's app
* python manage.py migrate // 同步数据库
* python manage.py createsuperuser --email admin@example.com --username admin  // 创建一个初始用户admin，其密码为password123

settings.py add:

```python
# Add 'rest_framework' to 'INSTALLED_APPS'.
INSTALLED_APPS = [
    ...
    'rest_framework',
]

# control how many objects per page are returned.
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```
