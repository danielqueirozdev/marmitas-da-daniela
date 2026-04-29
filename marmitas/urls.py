from django.urls import path
from . import views


app_name = 'marmitas'

urlpatterns = [
   path('', views.marmitas_view, name='home'),
   path('criar/', views.marmitas_create_view, name='criar'),
   path('editar/<int:id>/', views.marmitas_edit_view, name='editar'),
   path('deletar/<int:id>/', views.marmitas_delete_view, name='deletar'),
]