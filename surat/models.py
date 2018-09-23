from __future__ import unicode_literals
from django.db import models

from petugas.models import Petugas

# Create your models here.
class SuratMasuk(models.Model):
    pid = models.ForeignKey(Petugas)
    jenis_surat = models.CharField(max_length=30)
    tanggal_kirim = models.DateField()
    tanggal_terima = models.DateField()
    no_surat = models.CharField(max_length=15)
    pengirim = models.CharField(max_length=30)
    perihal = models.CharField(max_length=30)

class SuratKeluar(models.Model):
    pid = models.ForeignKey(Petugas)
    jenis_surat = models.CharField(max_length=30)
    tanggal_kirim = models.DateField()
    no_surat = models.CharField(max_length=15)
    pengirim = models.CharField(max_length=30)
    perihal = models.CharField(max_length=30)
