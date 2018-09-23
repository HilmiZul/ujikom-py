"""ujikom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, handler404, handler500
from django.contrib import admin

from dashboard import views as dashboard_view
from petugas import views as petugas_view
from surat import views as surat_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', dashboard_view.dashboard),

    url(r'^login/$', petugas_view.login_to_sys),
    url(r'^logout/$', petugas_view.logout_from_sys),

    url(r'^suma/$', surat_view.suma),
    url(r'^sukel/$', surat_view.sukel),

    url(r'^suma/tambah/$', surat_view.tambah_suma),
    url(r'^sukel/tambah/$', surat_view.tambah_sukel),

    url(r'^suma/ubah/(\d+)', surat_view.ubah_suma),
    url(r'^sukel/ubah/(\d+)', surat_view.ubah_sukel),

    url(r'^suma/hapus/(\d+)', surat_view.hapus_suma),
    url(r'^sukel/hapus/(\d+)', surat_view.hapus_sukel),

    #url(r'^suma/laporan/', surat_view.hapus_suma),
    #url(r'^sukel/hapus/(\d+)', surat_view.hapus_sukel),
]

handler404 = 'dashboard_view.e404'
handler500 = 'dashboard_view.e500'
