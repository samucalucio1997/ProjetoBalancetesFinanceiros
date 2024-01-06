from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="Financeiro"
urlpatterns = [
    path('', views.Principal.as_view(), name=""),
    path('cad/', views.CadastrarUsuario.as_view(), name = "cad"),
    path('auth/', views.LoginFace.as_view(), name = "auth"),
    path('Telacad/', views.FormCad.as_view(), name = "Telacad"),
    path('Dashboard/', views.Red.as_view() , name = "Dashboard"),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)