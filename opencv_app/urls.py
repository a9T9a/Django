from django.conf.urls import url
from opencv_app.views import IndexView, EditCv2ImageView, edit
from opencv_app import views


app_name = 'django_opencv_app'

urlpatterns = [
    url('', IndexView, name='IndexView'),
]