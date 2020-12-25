from django.urls import path
from .views import sign_up, profile, edit_profile

urlpatterns = [
    path('signup',sign_up , name = "sign_up"),
    path('profile/',profile , name = "profile"),
    path('profile/edit', edit_profile, name = "profile_editor"),
] 

app_name = 'accounts'