from django.contrib import admin
from django.urls import path
from compras.views import compras, nova_transacao, update, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', compras, name='url_compras'),
    path('update/<int:pk>/', update, name='url_update'),
    path('delete/<int:pk>/', delete, name='url_delete'),
    path('nova/', nova_transacao, name='url_nova'),

]
