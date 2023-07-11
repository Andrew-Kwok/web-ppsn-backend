from django.db import models

# Create your models here.
# TODO: consider using models.TextChoices
class RegistrationFormFile(models.Model):
    registration_form = models.FileField(upload_to='documents/')

class RegistrationData(models.Model):
    foto = models.ImageField(upload_to='foto-peserta/')
    nama_lengkap = models.CharField(max_length=200)
    jenis_kelamin = models.CharField(max_length=20)
    tempat_lahir = models.CharField(max_length=50)
    tanggal_lahir = models.DateField()
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
    tahun_masuk_sma = models.IntegerField()
    semester_sma = models.CharField(max_length=5)
    ekstrakurikuler = models.CharField(max_length=200)
    kota_sekolah = models.CharField(max_length=50)
    prov_sekolah = models.CharField(max_length=50)

    nama_institusi = models.CharField(max_length=200)
    fakultas = models.CharField(max_length=200)
    penjurusan = models.CharField(max_length=200)
    prodi = models.CharField(max_length=200)
    tahun_masuk_dikti = models.IntegerField()
    ukm = models.CharField(max_length=200)
    kota_institusi = models.CharField(max_length=50)
    prov_institusi = models.CharField(max_length=50)

    motivasi_bergabung = models.TextField()
    tujuan_bergabung = models.TextField()

    pakta_setuju = models.BooleanField(default=False)
    pakta_tidak_setuju = models.BooleanField(default=False)

    tautan_dokumen = models.CharField(max_length=200)


class RegistrationDataOrganization(models.Model):
    nama_institusi = models.CharField(max_length=200)
    posisi_jabatan = models.CharField(max_length=25)
    masa_jabatan_mulai = models.DateTimeField()
    masa_jabatan_akhir = models.DateTimeField()
    deskripsi_jabatan = models.TextField()

    registration_form = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='organisasi')

class RegistrationDataAchievement(models.Model):
    nama_acara = models.CharField(max_length=200)
    lembaga_penyelenggara = models.CharField(max_length=200)
    tingkat = models.CharField(max_length=20)
    tahun = models.IntegerField()
    keterangan_tambahan = models.TextField()

    registration_form = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='prestasi_penghargaan')

class RegistrationDataExperience(models.Model):
    nama_kegiatan = models.CharField(max_length=200)
    lembaga_penyelenggara = models.CharField(max_length=200)
    masa_kerja_mulai = models.DateTimeField()
    masa_kerja_akhir = models.DateTimeField()
    keterangan_tambahan = models.TextField()

    registration_form = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='pengalaman_kerja')


class RegistrationDataScholarship(models.Model):
    nama_beasiswa = models.CharField(max_length=200)
    lembaga_penyelenggara = models.CharField(max_length=200)
    jenjang = models.CharField(max_length=20)
    tahun = models.IntegerField()
    tipe_pendanaan = models.CharField(max_length=20)

    registration_form = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='beasiswa')


class RegistrationDataPublication(models.Model):
    judul_publikasi = models.CharField(max_length=200)
    jenis_publikasi = models.CharField(max_length=100)
    lembaga_publikasi = models.CharField(max_length=200)
    tahun = models.IntegerField()
    deskripsi_tambahan = models.TextField()

    registration_form = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='publikasi')

class RegistrationDataLanguage(models.Model):
    bahasa = models.CharField(max_length=100)
    keterampilan_menulis = models.CharField(max_length=100)
    keterampilan_membaca = models.CharField(max_length=100)
    skor_kemahiran = models.CharField(max_length=200)
    tahun_tes = models.IntegerField()

    registration_form = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='bahasa_asing')


class RegistrationDataSkill(models.Model):
    sains = models.TextField()
    seni = models.TextField()
    sosial = models.TextField()
    sastra = models.TextField()

    registration_form = models.OneToOneField(RegistrationData, on_delete=models.CASCADE, related_name='skill')


class RegistrationDataDivisionChoice(models.Model):
    nama_formasi = models.CharField(max_length=50)
    tingkat_jabatan = models.CharField(max_length=20)
    minat_bakat = models.TextField()
    pengalaman = models.TextField()
    harapan_kontribusi = models.TextField()

    registration_form = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='pilihan_formasi')