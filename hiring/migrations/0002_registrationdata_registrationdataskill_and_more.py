# Generated by Django 4.2.1 on 2023-07-11 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hiring', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='foto-peserta/')),
                ('nama_lengkap', models.CharField(max_length=200)),
                ('jenis_kelamin', models.CharField(max_length=20)),
                ('tempat_lahir', models.CharField(max_length=50)),
                ('tanggal_lahir', models.DateField()),
                ('kota_pribadi', models.CharField(max_length=50)),
                ('prov_pribadi', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('notelp', models.CharField(max_length=20)),
                ('whatsapp', models.CharField(max_length=20)),
                ('linkedin', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
                ('telegram', models.CharField(max_length=20)),
                ('line', models.CharField(max_length=50)),
                ('nama_sekolah', models.CharField(max_length=200)),
                ('sistem_sekolah', models.CharField(max_length=50)),
                ('tahun_masuk_sma', models.IntegerField()),
                ('semester_sma', models.CharField(max_length=5)),
                ('ekstrakurikuler', models.CharField(max_length=200)),
                ('kota_sekolah', models.CharField(max_length=50)),
                ('prov_sekolah', models.CharField(max_length=50)),
                ('nama_institusi', models.CharField(max_length=200)),
                ('fakultas', models.CharField(max_length=200)),
                ('penjurusan', models.CharField(max_length=200)),
                ('prodi', models.CharField(max_length=200)),
                ('tahun_masuk_dikti', models.IntegerField()),
                ('ukm', models.CharField(max_length=200)),
                ('kota_institusi', models.CharField(max_length=50)),
                ('prov_institusi', models.CharField(max_length=50)),
                ('motivasi_bergabung', models.TextField()),
                ('tujuan_bergabung', models.TextField()),
                ('pakta_setuju', models.BooleanField(default=False)),
                ('pakta_tidak_setuju', models.BooleanField(default=False)),
                ('tautan_dokumen', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationDataSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sains', models.TextField()),
                ('seni', models.TextField()),
                ('sosial', models.TextField()),
                ('sastra', models.TextField()),
                ('registration_form', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='hiring.registrationdata')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationDataScholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_beasiswa', models.CharField(max_length=200)),
                ('lembaga_penyelenggara', models.CharField(max_length=200)),
                ('jenjang', models.CharField(max_length=20)),
                ('tahun', models.IntegerField()),
                ('tipe_pendanaan', models.CharField(max_length=20)),
                ('registration_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beasiswa', to='hiring.registrationdata')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationDataPublication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_publikasi', models.CharField(max_length=200)),
                ('jenis_publikasi', models.CharField(max_length=100)),
                ('lembaga_publikasi', models.CharField(max_length=200)),
                ('tahun', models.IntegerField()),
                ('deskripsi_tambahan', models.TextField()),
                ('registration_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publikasi', to='hiring.registrationdata')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationDataOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_institusi', models.CharField(max_length=200)),
                ('posisi_jabatan', models.CharField(max_length=25)),
                ('masa_jabatan_mulai', models.DateTimeField()),
                ('masa_jabatan_akhir', models.DateTimeField()),
                ('deskripsi_jabatan', models.TextField()),
                ('registration_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organisasi', to='hiring.registrationdata')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationDataLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bahasa', models.CharField(max_length=100)),
                ('keterampilan_menulis', models.CharField(max_length=100)),
                ('keterampilan_membaca', models.CharField(max_length=100)),
                ('skor_kemahiran', models.CharField(max_length=200)),
                ('tahun_tes', models.IntegerField()),
                ('registration_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bahasa_asing', to='hiring.registrationdata')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationDataExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kegiatan', models.CharField(max_length=200)),
                ('lembaga_penyelenggara', models.CharField(max_length=200)),
                ('masa_kerja_mulai', models.DateTimeField()),
                ('masa_kerja_akhir', models.DateTimeField()),
                ('keterangan_tambahan', models.TextField()),
                ('registration_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pengalaman_kerja', to='hiring.registrationdata')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationDataDivisionChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_formasi', models.CharField(max_length=50)),
                ('tingkat_jabatan', models.CharField(max_length=20)),
                ('minat_bakat', models.TextField()),
                ('pengalaman', models.TextField()),
                ('harapan_kontribusi', models.TextField()),
                ('registration_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pilihan_formasi', to='hiring.registrationdata')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationDataAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_acara', models.CharField(max_length=200)),
                ('lembaga_penyelenggara', models.CharField(max_length=200)),
                ('tingkat', models.CharField(max_length=20)),
                ('tahun', models.IntegerField()),
                ('keterangan_tambahan', models.TextField()),
                ('registration_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestasi_penghargaan', to='hiring.registrationdata')),
            ],
        ),
    ]
