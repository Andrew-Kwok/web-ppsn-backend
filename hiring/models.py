from django.db import models

import uuid

# Create your models here.
# TODO: consider using models.TextChoices
class RegistrationFormFile(models.Model):
    registration_form = models.FileField(upload_to='documents/')

class RegistrationData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    foto = models.ImageField(upload_to='foto-peserta/')
    nama_lengkap = models.CharField(max_length=200)
    jenis_kelamin = models.CharField(max_length=20)
    tempat_lahir = models.CharField(max_length=50)
    tanggal_lahir = models.DateField(null=True)
    kota_pribadi = models.CharField(max_length=50)
    prov_pribadi = models.CharField(max_length=50)

    email = models.EmailField()
    notelp = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    linkedin = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    telegram = models.CharField(max_length=20)
    line = models.CharField(max_length=50)

    nama_sekolah = models.CharField(max_length=200)
    sistem_sekolah = models.CharField(max_length=50)
    tahun_masuk_sma = models.IntegerField(null=True)
    semester_sma = models.CharField(max_length=5)
    ekstrakurikuler = models.CharField(max_length=200)
    kota_sekolah = models.CharField(max_length=50)
    prov_sekolah = models.CharField(max_length=50)

    nama_institusi = models.CharField(max_length=200)
    fakultas = models.CharField(max_length=200)
    penjurusan = models.CharField(max_length=200)
    prodi = models.CharField(max_length=200)
    tahun_masuk_dikti = models.IntegerField(null=True)
    ukm = models.CharField(max_length=200)
    kota_institusi = models.CharField(max_length=50)
    prov_institusi = models.CharField(max_length=50)

    motivasi_bergabung = models.TextField()
    tujuan_bergabung = models.TextField()

    pakta_setuju = models.BooleanField(default=False)
    pakta_tidak_setuju = models.BooleanField(default=False)

    tautan_dokumen = models.CharField(max_length=200)

    error_notes = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)


class RegistrationDataOrganization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_institusi = models.CharField(max_length=200)
    posisi_jabatan = models.CharField(max_length=25)
    masa_jabatan_mulai = models.DateField(null=True)
    masa_jabatan_akhir = models.DateField(null=True)
    deskripsi_jabatan = models.TextField()

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='organisasi')

    def registration_data__nama_lengkap(self, obj):
        return obj.registration_data.nama_lengkap


class RegistrationDataAchievement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_acara = models.CharField(max_length=200)
    lembaga_penyelenggara = models.CharField(max_length=200)
    tingkat = models.CharField(max_length=20)
    tahun_perolehan = models.IntegerField(null=True)
    keterangan_tambahan = models.TextField()

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='prestasi_penghargaan')

class RegistrationDataExperience(models.Model):
    nama_kegiatan = models.CharField(max_length=200)
    lembaga_penyelenggara = models.CharField(max_length=200)
    masa_kerja_mulai = models.DateField(null=True)
    masa_kerja_akhir = models.DateField(null=True)
    keterangan_tambahan = models.TextField()

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='pengalaman_kerja')


class RegistrationDataScholarship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_beasiswa = models.CharField(max_length=200)
    lembaga_penyelenggara = models.CharField(max_length=200)
    jenjang = models.CharField(max_length=20)
    tahun_beasiswa = models.IntegerField(null=True)
    tipe_pendanaan = models.CharField(max_length=20)

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='beasiswa')


class RegistrationDataPublication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    judul_publikasi = models.CharField(max_length=200)
    jenis_publikasi = models.CharField(max_length=100)
    lembaga_publikasi = models.CharField(max_length=200)
    tahun_publikasi = models.IntegerField(null=True)
    deskripsi_tambahan = models.TextField()

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='publikasi')

class RegistrationDataLanguage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bahasa = models.CharField(max_length=100)
    keterampilan_bicara = models.CharField(max_length=100)
    keterampilan_menulis = models.CharField(max_length=100)
    keterampilan_membaca = models.CharField(max_length=100)
    skor_kemahiran = models.CharField(max_length=200)
    tahun_tes = models.IntegerField(null=True)

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='bahasa_asing')


class RegistrationDataSkill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    saintek = models.TextField()
    seni = models.TextField()
    sosial = models.TextField()
    sastra = models.TextField()

    registration_data = models.OneToOneField(RegistrationData, on_delete=models.CASCADE, related_name='skill')


class RegistrationDataDivisionChoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_formasi = models.CharField(max_length=50)
    tingkat_jabatan = models.CharField(max_length=20)
    minat_bakat = models.TextField()
    pengalaman = models.TextField()
    harapan_kontribusi = models.TextField()

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='pilihan_formasi')