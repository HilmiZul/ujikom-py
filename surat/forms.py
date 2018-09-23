from django.forms import ModelForm
from django import forms
from surat.models import SuratMasuk, SuratKeluar

class FormSuratMasuk(ModelForm):
    class Meta:
        model = SuratMasuk
        fields = ['jenis_surat', 'tanggal_kirim', 'tanggal_terima', 'no_surat', 'pengirim', 'perihal']

        labels = {
          'jenis_surat':"Jenis Surat",
          'tanggal_kirim':'Tanggal Kirim',
          'tanggal_terima':'Tanggal Terima',
          'no_surat':'No.Surat',
          'pengirim':'Pengirim',
          'perihal':'Perihal',
        }

        error_messages = {
          'jenis_surat': {
              'required': 'Jenis surat harus diisi'
          },
          'tanggal_kirim' : {
              'required': "Tanggal kirim harus diisi"
          },
          'tanggal_terima' : {
              'required': "Tanggal terima harus diisi"
          },
          'no_surat' : {
            'required': "No.surat ga boleh kosong"
          },
          'pengirim': {
            'required': "Pengirim ga boleh kosong"
          },
          'perihal': {
            'required': "Perihal juga :D"
          },
        }
        widgets = {
          'jenis_surat': forms.TextInput(attrs={
                    'type':'text',
                    'class':'form-control',
                    'required':'required',
                    'autofocus':'autofocus',
                    'placeholder':'Contoh: Undangan',
                    }),
          'tanggal_kirim': forms.TextInput(attrs={
                    'type': 'date',
                    'class':'form-control',
                    'required':'required'
                    }),
          'tanggal_terima': forms.TextInput(attrs={
                    'type':'date',
                    'required':'required',
                    'class': 'form-control'
                    }),
          'no_surat': forms.TextInput(attrs={
                    'type':'text',
                    'class': 'form-control',
                    'required':'required'
                    }),
          'pengirim': forms.TextInput(attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'required': 'required'
                    }),
           'perihal': forms.TextInput(attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'required': 'required'
                    }),
        }

class FormSuratKeluar(ModelForm):
    class Meta:
        model = SuratKeluar
        fields = ['jenis_surat', 'tanggal_kirim', 'no_surat', 'pengirim', 'perihal']

        labels = {
            'jenis_surat': 'Jenis Surat',
            'tanggal_kirim': 'Tanggal Kirim',
            'no_surat': 'No.Surat',
            'pengirim': 'Pengirim',
            'perihal': 'Perihal',
        }

        widgets = {
            'jenis_surat': forms.TextInput(attrs={
                        'type': 'text',
                        'class': 'form-control',
                        'required': 'required',
                        'autofocus': 'autofocus',
                        }),
            'tanggal_kirim': forms.TextInput(attrs={
                        'type': 'date',
                        'class': 'form-control',
                        'required': 'required'
                        }),
            'no_surat': forms.TextInput(attrs={
                        'type': 'text',
                        'class': 'form-control',
                        'required': 'required'
                        }),
            'pengirim': forms.TextInput(attrs={
                        'type': 'text',
                        'class': 'form-control',
                        'required': 'required'
                        }),
            'perihal': forms.TextInput(attrs={
                        'type': 'text',
                        'class': 'form-control',
                        'required': 'required'
                        }),

        }
