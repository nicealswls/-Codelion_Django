from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name='hello_world'),  # 밑 주소에 요청이 들어오면 myapp 안 views에 있는 home 함수 실행시키라는 뜻
]                                                    # myapp.views import 꼭 해야 함

# http://127.0.0.1:8000/
