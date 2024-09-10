from django.urls import path
from .views import LoginViewSet, SignupViewSet

login_list = LoginViewSet.as_view({'post': 'post'})
signup_list = SignupViewSet.as_view({'post': 'post'})

urlpatterns = [
    path('login/', login_list, name='login'),
    path('signup/', signup_list, name='signup'),
]
