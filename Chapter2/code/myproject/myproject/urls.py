from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
] # 런서버 주소 뒤에 /admin 하면 admin(관리자) 사이트 들어가진다는 말
