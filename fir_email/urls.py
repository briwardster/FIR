from django.conf.urls import url
from fir_email.utils import check_smime_status
from fir_email import views

app_name = 'email'

urlpatterns = []

if check_smime_status():
    urlpatterns.append(url(r'^user/certificate/$', views.smime_configuration, name='user-certificate'))
