#from django.conf.urls import url
from django.urls import path

from . import views
app_name="app"
urlpatterns = [
 
    path('',views.index,name="list"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
]
