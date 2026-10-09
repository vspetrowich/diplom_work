from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from backend.views import RegisterAccount, LoginAccount, AccountDetails, ConfirmAccount


app_name = 'backend'
urlpatterns = [
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/details', AccountDetails.as_view(), name='user-details'),


]