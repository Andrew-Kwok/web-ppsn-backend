from django.db import models

import uuid

# Create your models here.
# TODO: consider using models.TextChoices
# TODO: `masa_kerja_mulai` and `masa_kerja-akhir` are using CharField, consider changing after .docx form is fixed
class RegistrationFormFile(models.Model):
    registration_form = models.FileField(upload_to='documents/')


class RegistrationData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    foto = models.ImageField(upload_to='foto-peserta/')
    nama_lengkap = models.CharField(max_length=200, default='')
    jenis_kelamin = models.CharField(max_length=20, default='')
    tempat_lahir = models.CharField(max_length=50, default='')
    tanggal_lahir = models.DateField(null=True)
    kota_pribadi = models.CharField(max_length=50, default='')
    prov_pribadi = models.CharField(max_length=50, default='')

    email = models.EmailField(default='')
    notelp = models.CharField(max_length=20, default='')
    whatsapp = models.CharField(max_length=20, default='')
    linkedin = models.CharField(max_length=100, default='')
    instagram = models.CharField(max_length=100, default='')
    telegram = models.CharField(max_length=20, default='')
    line = models.CharField(max_length=50, default='')

    nama_sekolah = models.CharField(max_length=200, default='')
    sistem_sekolah = models.CharField(max_length=50, default='')
    tahun_masuk_sma = models.IntegerField(null=True)
    semester_sma = models.CharField(max_length=5, default='')
    ekstrakurikuler = models.CharField(max_length=200, default='')
    kota_sekolah = models.CharField(max_length=50, default='')
    prov_sekolah = models.CharField(max_length=50, default='')

    nama_institusi = models.CharField(max_length=200, default='')
    fakultas = models.CharField(max_length=200, default='')
    penjurusan = models.CharField(max_length=200, default='')
    prodi = models.CharField(max_length=200, default='')
    tahun_masuk_dikti = models.IntegerField(null=True)
    ukm = models.CharField(max_length=200, default='')
    kota_institusi = models.CharField(max_length=50, default='')
    prov_institusi = models.CharField(max_length=50, default='')

    motivasi_bergabung = models.TextField(default='')
    tujuan_bergabung = models.TextField(default='')

    pakta_setuju = models.BooleanField(default=False)
    pakta_tidak_setuju = models.BooleanField(default=False)

    tautan_dokumen = models.CharField(max_length=200, default='')
    tautan_dokumen_drive_ppsn = models.CharField(max_length=200, default='')

    error_notes = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)


class RegistrationDataOrganization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_institusi = models.CharField(max_length=200, default='')
    posisi_jabatan = models.CharField(max_length=25, default='')
    masa_jabatan_mulai = models.DateField(null=True)
    masa_jabatan_akhir = models.DateField(null=True)
    deskripsi_jabatan = models.TextField(default='')

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='organisasi')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir


class RegistrationDataAchievement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_acara = models.CharField(max_length=200, default='')
    lembaga_penyelenggara = models.CharField(max_length=200, default='')
    tingkat = models.CharField(max_length=20, default='')
    tahun_perolehan = models.IntegerField(null=True)
    keterangan_tambahan = models.TextField(default='')

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='prestasi_penghargaan')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir


class RegistrationDataExperience(models.Model):
    nama_kegiatan = models.CharField(max_length=200, default='')
    lembaga_penyelenggara = models.CharField(max_length=200, default='')
    masa_kerja_mulai = models.CharField(max_length=20, default='')
    masa_kerja_akhir = models.CharField(max_length=20, default='')
    keterangan_tambahan = models.TextField(default='')

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='pengalaman_kerja')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir


class RegistrationDataScholarship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_beasiswa = models.CharField(max_length=200, default='')
    lembaga_penyelenggara = models.CharField(max_length=200, default='')
    jenjang = models.CharField(max_length=20, default='')
    tahun_beasiswa = models.IntegerField(null=True)
    tipe_pendanaan = models.CharField(max_length=20, default='')

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='beasiswa')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir


class RegistrationDataPublication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    judul_publikasi = models.CharField(max_length=200, default='')
    jenis_publikasi = models.CharField(max_length=100, default='')
    lembaga_publikasi = models.CharField(max_length=200, default='')
    tahun_publikasi = models.IntegerField(null=True)
    deskripsi_tambahan = models.TextField(default='')

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='publikasi')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir

class RegistrationDataLanguage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bahasa = models.CharField(max_length=100, default='')
    keterampilan_bicara = models.CharField(max_length=100, default='')
    keterampilan_menulis = models.CharField(max_length=100, default='')
    keterampilan_membaca = models.CharField(max_length=100, default='')
    skor_kemahiran = models.CharField(max_length=200, default='')
    tahun_tes = models.IntegerField(null=True)

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='bahasa_asing')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir


class RegistrationDataSkill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    saintek = models.TextField(default='')
    seni = models.TextField(default='')
    sosial = models.TextField(default='')
    sastra = models.TextField(default='')

    registration_data = models.OneToOneField(RegistrationData, on_delete=models.CASCADE, related_name='skill')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir


class RegistrationDataDivisionChoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_formasi = models.CharField(max_length=50, default='')
    tingkat_jabatan = models.CharField(max_length=20, default='')
    minat_bakat = models.TextField(default='')
    pengalaman = models.TextField(default='')
    harapan_kontribusi = models.TextField(default='')

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='pilihan_formasi')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir


class RegistrationDataCommitteeDecision(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_panitia = models.CharField(max_length=200, null=True)
    tanggal_tinjau = models.DateField(null=True)
    berkas_lengkap = models.BooleanField(null=True)
    hasil_tinjauan = models.TextField(null=True)
    status_lulus = models.BooleanField(null=True)

    registration_data = models.ForeignKey(RegistrationData, on_delete=models.CASCADE, related_name='hasil_seleksi')
    def registration_data__nama_lengkap(self):
        return self.registration_data.nama_lengkap
    def registration_data__tanggal_lahir(self):
        return self.registration_data.tanggal_lahir

