
# backend/urls.py

from django.contrib import admin
from django.urls import path, include                 # add this
from rest_framework import routers                    # add this
from todo import views                            # add this
from django.conf.urls.static import static
from django.conf import settings
        
router = routers.DefaultRouter()                      # add this
router.register(r'todos', views.TodoView, 'todo')     # add this
        
urlpatterns = [
    path('admin/', admin.site.urls),           
    path('api/', include(router.urls))                # add this
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 