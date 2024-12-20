from django.urls import path
from blog import views

urlpatterns = [
    path("",views.home, name= "home_page" ),
    path("about/",views.about, name= "about_page" ),
    path("contact/",views.contact, name= "contact_page" ),
    path("dashboard/",views.user_dashboard, name= "dashboard_page" ),
    path("login/",views.user_login, name= "login_page" ),
    path("signup/",views.user_signup, name= "signup_page" ),
    path("logout/",views.user_logout, name= "logout_page" ),
    path("manage_post/",views.manage_post, name= "manage_post" ),
    path("create_blog/",views.create_blog, name= "create_blog" ),
    path("delete_record/<int:id>/",views.delete_record, name= "delete_post" ),
    path("post=<int:id>/",views.single_data, name= "single_data" ),
    path("edit/<int:id>/", views.edit_blog, name='edit_post'),
    

]