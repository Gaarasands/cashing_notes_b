from django.urls import path
from productrawmaterial import views

urlpatterns = [
   path('delete/<int:id>',views.render)
]
