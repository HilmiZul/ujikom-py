from django.contrib import admin
from surat.models import SuratMasuk, SuratKeluar

# Register your models here.
class SuratMasukAdmin(admin.ModelAdmin):
    list_display = ['jenis_surat', 'tanggal_kirim', 'tanggal_terima', 'pengirim']
    list_filter = ('tanggal_terima', 'pengirim')
    search_fields = ['pengirim', 'jenis_surat']
    list_per_page = 10

class SuratKeluarAdmin(admin.ModelAdmin):
    list_display = ['jenis_surat', 'tanggal_kirim', 'pengirim']
    list_filter = ('tanggal_kirim', 'pengirim')
    search_fields = ['pengirim', 'jenis_surat']
    list_per_page = 10

admin.site.register(SuratMasuk, SuratMasukAdmin)
admin.site.register(SuratKeluar, SuratKeluarAdmin)
