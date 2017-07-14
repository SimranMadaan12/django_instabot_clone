from django.conf.urls import url
from myapp.views import signup_view, login_view

urlpatterns = [

    url('login/', login_view),
    url('', signup_view)
]