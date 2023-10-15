from . import views
from django.urls import path
app_name='credentials'
urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('district_wikipedia',views.district_wikipedia,name='district_wikipedia'),
    path('logout',views.logout,name='logout'),
    path('all_districts',views.all_districts,name='all_districts'),
    path('accountsubmission', views.accountsubmission, name='accountsubmission'),
    path('back', views.back, name='back'),
    path('district_branch_view', views.district_branch_view, name='district_branch_view'),
    path('get_branches/', views.get_branches, name='get_branches'),

]