from django.urls import path
from app2 import views
app_name="app2"

urlpatterns = [
    path("index2/",views.index2,name="app1_index2"),
    
]
