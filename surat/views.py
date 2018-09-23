from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from surat.models import SuratMasuk, SuratKeluar
from surat.forms import FormSuratMasuk, FormSuratKeluar
from petugas.models import Petugas

# SURAT MASUK
@login_required(login_url=settings.LOGIN_URL)
def suma(request):
    rows = SuratMasuk.objects.order_by('-tanggal_kirim')
    ada = rows.count()
    return render(request, 'suma.html', {'rows':rows, 'ada':ada})

# SURAT KELUAR
@login_required(login_url=settings.LOGIN_URL)
def sukel(request):
    rows = SuratKeluar.objects.order_by('-tanggal_kirim')
    ada = rows.count()
    return render(request, 'sukel.html', {'rows':rows, 'ada':ada})

# TAMBAH SURAT MASUK
@login_required(login_url=settings.LOGIN_URL)
def tambah_suma(request):
    if request.POST:
        form = FormSuratMasuk(request.POST)
        if form.is_valid():
            suma = SuratMasuk(
                pid = Petugas.objects.get(nama_depan=request.session['nama']),
                jenis_surat = request.POST['jenis_surat'],
                tanggal_kirim = request.POST['tanggal_kirim'],
                tanggal_terima = request.POST['tanggal_terima'],
                no_surat = request.POST['no_surat'],
                pengirim = request.POST['pengirim'],
                perihal = request.POST['perihal'],
            )
            suma.save()
            msg = "Berhasil tersimpan."
            form = FormSuratMasuk()
            return render(request, 'tambah_suma.html', {'message':msg, 'form':form})
    else:
        form = FormSuratMasuk()
    return render(request, 'tambah_suma.html', {'form':form})

# UBAH SURAT MASUK
@login_required(login_url=settings.LOGIN_URL)
def ubah_suma(request,id_suma):
    if request.POST:
        SuratMasuk.objects.filter(id=id_suma).update(
            jenis_surat = request.POST['jenis_surat'],
            tanggal_kirim = request.POST['tgl_kirim'],
            tanggal_terima = request.POST['tgl_terima'],
            no_surat = request.POST['no_surat'],
            pengirim = request.POST['pengirim'],
            perihal = request.POST['perihal'],
        )
        msg = "Berhasil diperbaharui."
        get_suma = SuratMasuk.objects.get(id=id_suma)
        return render(request, 'ubah_suma.html', {'message':msg, 'suma':get_suma})
    else:
        get_suma = SuratMasuk.objects.get(id=id_suma)
    return render(request, 'ubah_suma.html', {'suma':get_suma})

# HAPUS SURAT MASUK
@login_required(login_url=settings.LOGIN_URL)
def hapus_suma(request,id_suma):
    if request.POST:
        SuratMasuk.objects.filter(id=id_suma).delete()
        return redirect('/suma/')
    return redirect('/suma/')



# TAMBAH SURAT KELUAR
@login_required(login_url=settings.LOGIN_URL)
def tambah_sukel(request):
    if request.POST:
        form = FormSuratKeluar(request.POST)
        if form.is_valid():
            sukel = SuratKeluar(
                pid = Petugas.objects.get(nama_depan=request.session['nama']),
                jenis_surat = request.POST['jenis_surat'],
                tanggal_kirim = request.POST['tanggal_kirim'],
                no_surat = request.POST['no_surat'],
                pengirim = request.POST['pengirim'],
                perihal = request.POST['perihal'],
            )
            sukel.save()
            msg = "Berhasil tersimpan."
            form = FormSuratKeluar()
            return render(request, 'tambah_sukel.html', {'message':msg, 'form':form})
    else:
        form = FormSuratKeluar()
    return render(request, 'tambah_sukel.html', {'form':form})

# HAPUS SURAT KELUAR
@login_required(login_url=settings.LOGIN_URL)
def ubah_sukel(request,id_sukel):
    if request.POST:
        SuratKeluar.objects.filter(id=id_sukel).update(
            jenis_surat = request.POST['jenis_surat'],
            tanggal_kirim = request.POST['tgl_kirim'],
            no_surat = request.POST['no_surat'],
            pengirim = request.POST['pengirim'],
            perihal = request.POST['perihal'],
        )
        msg = "Berhasil diperbaharui."
        get_sukel = SuratKeluar.objects.get(id=id_sukel)
        return render(request, 'ubah_sukel.html', {'message':msg, 'sukel':get_sukel})
    else:
        get_sukel = SuratKeluar.objects.get(id=id_sukel)
    return render(request, 'ubah_sukel.html', {'sukel':get_sukel})

# HAPUS CATATAN KELUAR
@login_required(login_url=settings.LOGIN_URL)
def hapus_sukel(request,id_sukel):
    if request.POST:
        SuratKeluar.objects.filter(id=id_sukel).delete()
        return redirect('/sukel/')
    return redirect('/sukel/')
