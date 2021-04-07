from django.urls import path
from app1 import views
app_name="app1"

urlpatterns = [
    path("index1/",views.index1,name="app1_index1")

]
