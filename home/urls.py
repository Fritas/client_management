from django.urls import path
# login Django
from django.contrib.auth import views as auth_views
# --------------
from .views import index, logout

urlpatterns = [
    path('', index, name='index'),
    # login Django
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout', logout, name='logout'),

]