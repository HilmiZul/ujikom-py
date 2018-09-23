from django.contrib import admin

from petugas.models import Petugas

# Register your models here.
class PetugasAdmin(admin.ModelAdmin):
    list_display = ['username', 'nama_depan']
    list_filter = ('nama_depan','username')
    search_fields = ['uname', 'nama_depan']
    list_per_page = 20

admin.site.register(Petugas, PetugasAdmin)
