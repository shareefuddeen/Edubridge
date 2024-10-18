from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eduBridge/auth/', include('Authentication.urls')),
    path('eduBridge/', include('classroom.urls'))
]
