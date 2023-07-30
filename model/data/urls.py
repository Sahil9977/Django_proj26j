from django.urls import path , include
from . import views

urlpatterns = [

    path('',views.login,name="login"),
    path('Signup',views.signup,name="signup"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('view_notes',views.notes,name="notes"),
    path('logout',views.logout,name="logout"),
    path('edit_your_note/<slug>',views.edit,name="edit"),
    path('delete_this_note/<int:id>',views.delete,name="delete"),

]