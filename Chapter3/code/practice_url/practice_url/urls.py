from django.contrib import admin
from django.urls import path, include
from myapp import views # myapp에서 views 가져옴

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first),
    path('second/', views.second),
    path('products/', include('product.urls')),
    path('boards/', include('board.urls')), # boards로 시작되는 모든 url들은 board 폴더 안 urls.py에서 관리한다는 뜻
]
