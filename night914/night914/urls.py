"""night914 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from night914.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewsSet)
router.register(r'groups', views.GroupViewsSet)

# 因为我们使用的是视图集而不是视图，所以我们只需为路由器类注册视图集即可自动为我们的 API 生成 URL conf 。
# 同样，如果我们需要对 API URL 的更多控制，我们可以简单地使用常规的基于类的视图，并显式地编写 URL conf 。
# 最后，我们包括用于可浏览 API 的默认登录和注销视图。这是可选的，但如果您的 API 需要身份验证并且您想使用可浏览的 API ，则很有用。
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
