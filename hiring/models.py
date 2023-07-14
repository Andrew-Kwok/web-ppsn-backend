from django.db import models
from django.utils import timezone

import uuid

# Create your models here.
# TODO: consider using models.TextChoices
# TODO: `masa_kerja_mulai` and `masa_kerja-akhir` are using CharField, consider changing after .docx form is fixed
class RegistrationFormFile(models.Model):
    registration_form = models.FileField(upload_to='documents/')


class RegistrationData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    foto = models.ImageField(upload_to='foto-peserta/', null=True, blank=True)
    nama_lengkap = models.CharField(max_length=200, null=True, blank=True)
    jenis_kelamin = models.CharField(max_length=20, null=True, blank=True)
    tempat_lahir = models.CharField(max_length=50, null=True, blank=True)
    tanggal_lahir = models.DateField(db_index=True)
    kota_pribadi = models.CharField(max_length=50, null=True, blank=True)
    prov_pribadi = models.CharField(max_length=50, null=True, blank=True)

    email = models.EmailField(db_index=True)
    notelp = models.CharField(max_length=20, null=True, blank=True)
    whatsapp = models.CharField(max_length=20, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    telegram = models.CharField(max_length=20, null=True, blank=True)
    line = models.CharField(max_length=50, null=True, blank=True)

    nama_sekolah = models.CharField(max_length=200, null=True, blank=True)
    sistem_sekolah = models.CharField(max_length=50, null=True, blank=True)
    tahun_masuk_sma = models.IntegerField(null=True, blank=True)
    semester_sma = models.CharField(max_length=5, null=True, blank=True)
    ekstrakurikuler = models.CharField(max_length=200, null=True, blank=True)
    kota_sekolah = models.CharField(max_length=50, null=True, blank=True)
    prov_sekolah = models.CharField(max_length=50, null=True, blank=True)

    nama_institusi = models.CharField(max_length=200, null=True, blank=True)
    fakultas = models.CharField(max_length=200, null=True, blank=True)
    penjurusan = models.CharField(max_length=200, null=True, blank=True)
    prodi = models.CharField(max_length=200, null=True, blank=True)
    tahun_masuk_dikti = models.IntegerField(null=True, blank=True)
    ukm = models.CharField(max_length=200, null=True, blank=True)
    kota_institusi = models.CharField(max_length=50, null=True, blank=True)
    prov_institusi = models.CharField(max_length=50, null=True, blank=True)

    motivasi_bergabung = models.TextField(null=True, blank=True)
    tujuan_bergabung = models.TextField(null=True, blank=True)

    pakta_setuju = models.BooleanField(default=False)
    pakta_tidak_setuju = models.BooleanField(default=False)

    tautan_dokumen = models.URLField(max_length=200, null=True, blank=True)
    tautan_dokumen_drive_ppsn = models.URLField(max_length=200, default='', null=True, blank=True)

    error_notes = models.TextField(default='', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)


class RegistrationDataOrganization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_institusi = models.CharField(max_length=200, null=True, blank=True)
    posisi_jabatan = models.CharField(max_length=25, null=True, blank=True)
    masa_jabatan_mulai = models.DateField(null=True, blank=True)
    masa_jabatan_akhir = models.DateField(null=True, blank=True)
    deskripsi_jabatan = models.TextField(null=True, blank=True)

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='organisasi')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir


class RegistrationDataAchievement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_acara = models.CharField(max_length=200, null=True, blank=True)
    lembaga_penyelenggara = models.CharField(max_length=200, null=True, blank=True)
    tingkat = models.CharField(max_length=20, null=True, blank=True)
    tahun_perolehan = models.IntegerField(null=True, blank=True)
    keterangan_tambahan = models.TextField(null=True, blank=True)

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='prestasi_penghargaan')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir


class RegistrationDataExperience(models.Model):
    nama_kegiatan = models.CharField(max_length=200, null=True, blank=True)
    lembaga_penyelenggara = models.CharField(max_length=200, null=True, blank=True)
    masa_kerja_mulai = models.CharField(max_length=20, null=True, blank=True)
    masa_kerja_akhir = models.CharField(max_length=20, null=True, blank=True)
    keterangan_tambahan = models.TextField(null=True, blank=True)

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='pengalaman_kerja')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir


class RegistrationDataScholarship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_beasiswa = models.CharField(max_length=200, null=True, blank=True)
    lembaga_penyelenggara = models.CharField(max_length=200, null=True, blank=True)
    jenjang = models.CharField(max_length=20, null=True, blank=True)
    tahun_beasiswa = models.IntegerField(null=True, blank=True)
    tipe_pendanaan = models.CharField(max_length=20, null=True, blank=True)

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='beasiswa')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir


class RegistrationDataPublication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    judul_publikasi = models.CharField(max_length=200, null=True, blank=True)
    jenis_publikasi = models.CharField(max_length=100, null=True, blank=True)
    lembaga_publikasi = models.CharField(max_length=200, null=True, blank=True)
    tahun_publikasi = models.IntegerField(null=True, blank=True)
    deskripsi_tambahan = models.TextField(null=True, blank=True)

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='publikasi')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir

class RegistrationDataLanguage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bahasa = models.CharField(max_length=100, null=True, blank=True)
    keterampilan_bicara = models.CharField(max_length=100, null=True, blank=True)
    keterampilan_menulis = models.CharField(max_length=100, null=True, blank=True)
    keterampilan_membaca = models.CharField(max_length=100, null=True, blank=True)
    skor_kemahiran = models.CharField(max_length=200, null=True, blank=True)
    tahun_tes = models.IntegerField(null=True, blank=True)

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='bahasa_asing')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir


class RegistrationDataSkill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    saintek = models.TextField(null=True, blank=True)
    seni = models.TextField(null=True, blank=True)
    sosial = models.TextField(null=True, blank=True)
    sastra = models.TextField(null=True, blank=True)

    registration_data = models.OneToOneField(RegistrationData, on_delete=models.CASCADE, related_name='skill')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir


class RegistrationDataDivisionChoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_formasi = models.CharField(max_length=50, null=True, blank=True)
    tingkat_jabatan = models.CharField(max_length=20, null=True, blank=True)
    minat_bakat = models.TextField(null=True, blank=True)
    pengalaman = models.TextField(null=True, blank=True)
    harapan_kontribusi = models.TextField(null=True, blank=True)

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='pilihan_formasi')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir


class RegistrationDataCommitteeDecision(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_panitia = models.CharField(max_length=200, null=True, blank=True)
    tanggal_tinjau = models.DateField(null=True, blank=True)
    berkas_lengkap = models.BooleanField(null=True, blank=True)
    hasil_tinjauan = models.TextField(null=True, blank=True)
    status_lulus = models.BooleanField(null=True, blank=True)

    registration_data = models.OneToOneField(RegistrationData, on_delete=models.CASCADE, related_name='hasil_seleksi')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir

