from django.urls import path
from .views import login_session,logout_session,view_Registro, home

urlpatterns = [
    path('registro/', view_Registro.as_view(), name="registro"),
    path('login/', login_session, name="login"),
    path('logout/', logout_session, name="logout"),
    path('', home, name='home'),
]
