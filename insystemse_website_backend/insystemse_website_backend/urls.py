from django.contrib import admin
from django.urls import path
from django.conf.urls import include

admin.site.site_header = 'Insystemse'
admin.site.index_title = 'Insystemse'
admin.site.site_title = 'Insystemse'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('presentation.urls')),
]
