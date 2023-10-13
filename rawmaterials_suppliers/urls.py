from django.urls import path
from rawmaterials_suppliers import views

urlpatterns = [
    path('add/',views.add),
    path('getall/',views.getall),
    path('get/id/<int:id>',views.getid),
    path('get/name/',views.getname),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete)
]
