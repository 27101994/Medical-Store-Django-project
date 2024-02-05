
from django.urls import path,include
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('home/',views.home_page,name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_page,name='logout'),
    path('createproduct/',views.product_create, name='createproduct'),
    path('retrieve/',views.product_read,name='retrieveproduct'),
    path('update/<int:id>/',views.product_update,name='updateproduct'),
    path('delete/<int:id>',views.product_delete,name='deleteproduct'),
    path('search/', views.product_search, name='product_search'),
    path('', RedirectView.as_view(url='login/')),

]