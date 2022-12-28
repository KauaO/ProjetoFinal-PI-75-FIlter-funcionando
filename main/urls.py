"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from oficina.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name="index.html"),
    path('pneus/', Pneus, name="pneus.html"),
    path('aros/', Aros, name="aros.html"),
    path('raios/', Raios, name="raios.html"),
    path('farois/', Farois, name="farois.html"),
    path('retrovisores/', Retrovisores, name="retrovisores.html"),
    path('cadastro_servico/', Cadastrar_servico, name="form_servico.html"),
    path('cadastro_cliente/', Cadastrar_cliente, name="form_cliente.html"),
    path('lista_clientes/', Lista_clientes, name="lista_clientes.html"),
    path('editar_cliente/<int:pk>/', Editar_cliente, name="editCli"),
    path('remover_cliente/<int:pk>/', Remover_cliente, name="removCli"),
    path('cadastro_produto/', Cadastrar_produto, name="form_produto.html"),
    path('atendimento/', Atendimento, name="atendimento.html"),
    path('accounts/login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', logout_aplicação ,name='logout') 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
