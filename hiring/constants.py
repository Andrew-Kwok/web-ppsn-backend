REGISTRATION_FORM_EMPTY_VALUE = [None, '', 'Pilih', 'Ketik di sini', 'Ketik di sini.', 'Salin tautan di sini']

REGISTRATION_FORM_DATE_FIELD = {
    'tanggal_lahir': "%A, %d %B %Y", 
    'masa_jabatan_mulai': "%B %y", 
    'masa_jabatan_akhir': "%B %y", 
    # 'masa_kerja_mulai': "%m-%y",
    # 'masa_kerja_akhir': "%m-%y",
}

REGISTRATION_FORM_BOOLEAN_FIELD = {
    'setuju': 'X',
    'tidak_setuju': 'X',
}

REGISTRATION_FORM_DATA_MAPPING = {
    'nama_lengkap': 'nama_lengkap',
    'jenis_kelamin': 'jenis_kelamin',
    'tempat_lahir': 'tempat_lahir',
    'tanggal_lahir': 'tanggal_lahir',
    'kota_pribadi': 'kota_pribadi',
    'prov_pribadi': 'prov_pribadi',

    'email': 'email',
    'notelp': 'notelp',
    'whatsapp': 'whatsapp',
    'linkedin': 'linkedin',
    'instagram': 'instagram',
    'telegram': 'telegram',
    'line': 'line',
    
    'nama_sekolah': 'nama_sekolah',
    'sistem_sekolah': 'sistem_sekolah',
    'tahun_masuk_sma': 'tahun_masuk_sma',
    'semester_sma': 'semester_sma',
    'ekstrakurikuler': 'ekstrakurikuler',
    'kota_sekolah': 'kota_sekolah',
    'prov_sekolah': 'prov_sekolah',

    'nama_institusi': 'nama_institusi',
    'fakultas': 'fakultas',
    'penjurusan': 'penjurusan',
    'prodi': 'prodi',
    'tahun_masuk_dikti': 'tahun_masuk_dikti',
    'ukm': 'ukm',
    'kota_institusi': 'kota_institusi',
    'prov_institusi': 'prov_institusi',

    'motivasi': 'motivasi_bergabung',
    'tujuan': 'tujuan_bergabung',
    'setuju': 'pakta_setuju',
    'tidak_setuju': 'pakta_tidak_setuju',
    'tautan': 'tautan_dokumen',
}

REGISTRATION_FORM_ORGANIZATION_FIELD = {
    ('20', ''): 'nama_institusi',
    ('21', ''): 'posisi_jabatan',
    ('22', 'b'): 'masa_jabatan_mulai',
    ('22', 'a'): 'masa_jabatan_akhir',
    ('23', ''): 'deskripsi_jabatan',
}
REGISTRATION_FORM_ORGANIZATION_MAPPING = {
    code[0] + 'a' + str(i) + code[1]: (field, i)
        for code, field in REGISTRATION_FORM_ORGANIZATION_FIELD.items()
        for i in range(1, 6)
}

REGISTRATION_FORM_ACHIEVEMENT_FIELD = {
    '24': 'nama_acara',
    '25': 'lembaga_penyelenggara',
    '26': 'tingkat',
    '27': 'tahun_perolehan',
    '28': 'keterangan_tambahan',
}
REGISTRATION_FORM_ACHIEVEMENT_MAPPING = {
    code + 'b' + str(i): (field, i)
        for code, field in REGISTRATION_FORM_ACHIEVEMENT_FIELD.items()
        for i in range(1, 6)
}

REGISTRATION_FORM_EXPERIENCE_FIELD = {
    ('29', ''): 'nama_kegiatan',
    ('30', ''): 'lembaga_penyelenggara',
    ('31', 'a'): 'masa_kerja_mulai',
    ('31', 'b'): 'masa_kerja_akhir',
    ('32', ''): 'keterangan_tambahan',
}
REGISTRATION_FORM_EXPERIENCE_MAPPING = {
    code[0] + 'c' + str(i) + code[1]: (field, i)
        for code, field in REGISTRATION_FORM_EXPERIENCE_FIELD.items()
        for i in range(1, 6)
}

REGISTRATION_FORM_SCHOLARSHIP_FIELD = {
    '33': 'nama_beasiswa',
    '34': 'lembaga_penyelenggara',
    '35': 'jenjang',
    '36': 'tahun_beasiswa',
    '37': 'tipe_pendanaan',
}
REGISTRATION_FORM_SCHOLARSHIP_MAPPING = {
    code + 'd' + str(i): (field, i)
        for code, field in REGISTRATION_FORM_SCHOLARSHIP_FIELD.items()
        for i in range(1, 6)
}
REGISTRATION_FORM_SCHOLARSHIP_MAPPING.update({'d34d5': ('lembaga_penyelenggara', 5)})

REGISTRATION_FORM_PUBLICATION_FIELD = {
    '38': 'judul_publikasi',
    '39': 'jenis_publikasi',
    '40': 'lembaga_publikasi',
    '41': 'tahun_publikasi',
    '42': 'deskripsi_tambahan',
}
REGISTRATION_FORM_PUBLICATION_MAPPING = {
    code + 'e' + str(i): (field, i)
        for code, field in REGISTRATION_FORM_PUBLICATION_FIELD.items()
        for i in range(1, 6)
}

REGISTRATION_FORM_LANGUAGE_FIELD = {
    '43': 'bahasa',
    '44': 'keterampilan_bicara',
    '45': 'keterampilan_menulis',
    '46': 'keterampilan_membaca',
    '47': 'skor_kemahiran',
    '48': 'tahun_tes',
}
REGISTRATION_FORM_LANGUAGE_MAPPING = {
    code + 'f' + str(i): (field, i)
        for code, field in REGISTRATION_FORM_LANGUAGE_FIELD.items()
        for i in range(1, 6)
}

REGISTRATION_FORM_SKILL_MAPPING = {
    'saintek': 'saintek',
    'seni': 'seni',
    'sosial': 'sosial',
    'literasi': 'sastra',
}

REGISTRATION_FORM_CHOICE_MAPPING = {
    'pil1_umum': ('nama_formasi', 0),
    'pos1_umum': ('tingkat_jabatan', 0),
    'pil1_umum_minat': ('minat_bakat', 0),
    'pil1_umum_harapan': ('harapan_kontribusi', 0),
    'pil1_umum_pengalaman': ('pengalaman', 0),
    'pil2_umum': ('nama_formasi', 1),
    'pos2_umum': ('tingkat_jabatan', 1),
    'pil2_umum_minat': ('minat_bakat', 1),
    'pil2_umum_harapan': ('harapan_kontribusi', 1),
    'pil2_umum_pengalaman': ('pengalaman', 1),
    "pil1_minat": ('nama_formasi', 2),
    "pos1_minat": ('tingkat_jabatan', 2),
    'pil1_minat_minat': ('minat_bakat', 2),
    'pil1_minat_harapan': ('harapan_kontribusi', 2),
    'pil1_minat_harapan': ('pengalaman', 2),
    "pil2_minat": ('nama_formasi', 3),
    "pos2_minat": ('tingkat_jabatan', 3),
    'pil2_minat_minat': ('minat_bakat', 3),
    'pil2_minat_harapan': ('harapan_kontribusi', 3),
    'pil2_minat_harapan': ('pengalaman', 3),
}