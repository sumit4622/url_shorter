
from django.urls import path, include
from shorter import views

app_name = 'shorter'

urlpatterns = [
    path('', views.home, name="home"),
    path('account/', include('account.urls'))
]
