from django.urls import path
from suppliers import views

urlpatterns = [
    path('getall/',views.getall),
    path('add/',views.add),
    path('get/id/<int:id>',views.getid),
    path('get/name/',views.getname),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete)
]
