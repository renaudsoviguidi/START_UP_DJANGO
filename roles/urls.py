from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="roles.index"),
    path('store', views.store, name="roles.store"),
    path('update/<int:id>', views.update, name="roles.update"),
    path('delete/<int:id>', views.delete, name="roles.delete"),
]
