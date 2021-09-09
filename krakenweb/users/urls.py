
import users
from django.urls import path
from users.views import registration

app_name="users"
urlpatterns=[
    path('register/',name='register',view=registration)
]