from django.urls import path
from . import views
# from django.views.decorators.cache import cache_page

app_name = "product"

urlpatterns = [
    path("",(views.HomeView.as_view()), name="home"),
    path("navbar",(views.NavbarPartialView.as_view()), name="navbar"),
    path("search", views.ProductSearchView.as_view(), name='product_search'),
    path("product/detail/<int:pk>", views.ProductDetailCommentView.as_view(), name='product_detail'),
    path("products", views.ProductListView.as_view(), name='product_list'),
    path("category/shop/<slug:slug>", views.CategoryDetailView.as_view(), name='category_list')
]