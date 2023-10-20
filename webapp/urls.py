from django.urls import path 

from webapp import views 
from .views import ProductList , ProductById
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('',views.index,name='index'),   
    path('product-list/',ProductList.as_view(),name='product-list'),
    path('product-by-id/<str:id>',ProductById.as_view(),name='product-by-id'),
    path('schema/',SpectacularAPIView.as_view(),name="schema"),
    path('schema/docs/',SpectacularSwaggerView.as_view(url_name="schema")),

]
