# GlowUp Gang v2.1 - Modular Version

## 📋 Deskripsi

Aplikasi CLI berbasis Python untuk rekomendasi skincare dan workout dengan output PDF. Versi 2.1 ini menampilkan arsitektur modular yang lebih mudah dibaca dan dipresentasikan.

## ✨ Perubahan dari v2.0 ke v2.1

### 1. **Struktur Workout Disederhanakan**

- ❌ Dihapus: `equipment` dan `brand` fields
- ✅ Sekarang: Hanya `exercise` dan `duration`
- 💡 Input admin lebih cepat dengan format: `Exercise | Duration`

### 2. **PDF Text Overflow Fixed**

- Menggunakan `Paragraph` objects dari reportlab
- Text otomatis wrap dalam tabel
- Tidak ada lagi teks terpotong

### 3. **Kode Dimodularisasi & Dioptimasi**

Dari 1 file (1000+ baris) → 6 file terpisah dengan generic functions:

```
config.py         (36 baris)   - Konstanta & konfigurasi
helpers.py        (73 baris)   - Fungsi utilitas
pdf_generator.py  (195 baris)  - Generate PDF
admin.py          (316 baris)  - CRUD operations (OPTIMIZED!)
user.py           (100+ baris) - User features
main.py           (50 baris)   - Entry point
```

**Admin.py Optimizations:**

- ❌ Before: 535 lines dengan 8 fungsi CRUD terpisah
- ✅ After: 316 lines dengan 4 generic CRUD functions
- 🎯 Reduction: **41% less code** dengan fungsi yang sama!

## 📁 Struktur File

```
Projek/
├── main.py                    # Entry point - jalankan ini!
├── config.py                  # Konstanta (file paths, credentials, dll)
├── helpers.py                 # Utility functions (BMI calc, JSON I/O)
├── pdf_generator.py           # PDF generation logic
├── admin.py                   # Admin CRUD functions
├── user.py                    # User features (Facial & Body GlowUp)
├── glowup_skincare.json       # Database skincare
├── glowup_workouts.json       # Database workout (struktur baru)
└── glowup_pdfs/               # Output folder untuk PDF
```

## 🚀 Quick Start

### Install Dependencies

```bash
pip install reportlab
```

### Jalankan Aplikasi

```bash
python main.py
```

## 🔐 Admin Credentials

- **Username**: `admin`
- **Password**: `admin123`

## 💻 Alur Penggunaan

### User Flow

1. Pilih menu **User - GlowUp Services**
2. Pilih **Facial GlowUp** atau **Body GlowUp**
3. Input data (tipe kulit / berat & tinggi)
4. PDF otomatis terbuat di folder `glowup_pdfs/`

### Admin Flow

1. Pilih menu **Admin - Manage Data**
2. Login dengan credentials admin
3. Kelola **Skincare** atau **Workout** (CRUD)

## 📝 Cara Input Workout (Admin)

**Format Baru (v2.1):**

```
Exercise | Duration
```

**Contoh:**

```
Push-ups | 3 set x 15 reps
Jogging | 30 menit, 3x/minggu
Plank | 3 set x 60 detik
```

Atau input terpisah:

```
Exercise: Push-ups
Duration: 3 set x 15 reps
```

## 🎨 Fitur PDF

### Skincare PDF (Biru - #2E86AB)

- Header dengan tipe kulit & timestamp
- Tabel 4 kolom: No | Step | Produk | Brand
- Text wrapping otomatis

### Workout PDF (Orange - #F18F01)

- Header dengan BMI & kategori
- Info berat & tinggi badan
- Tabel 2 kolom: No | Exercise & Duration
- Text wrapping otomatis

## 🔧 Penjelasan Modul

### config.py

Berisi semua konstanta:

- File paths (JSON, PDF output directory)
- Admin credentials
- Skin types mapping (1-5)
- BMI categories dengan ranges
- Color scheme untuk PDF

### helpers.py

Fungsi-fungsi utility:

- `clear_screen()`: Bersihkan terminal
- `load_json()` / `save_json()`: I/O database
- `calculate_bmi()`: Hitung BMI dari BB & TB
- `get_bmi_category()`: Tentukan kategori BMI
- `generate_id()`: UUID untuk data baru
- `pause()`: Pause untuk user input

### pdf_generator.py

Generate PDF dengan reportlab:

- `generate_skincare_pdf()`: PDF skincare routine
- `generate_workout_pdf()`: PDF workout plan
- Menggunakan `Paragraph` untuk text wrapping
- Custom styling per kategori (warna, spacing)

### admin.py

Semua fungsi admin:

- Login: `admin_login()`
- Skincare CRUD: view/add/edit/delete
- Workout CRUD: view/add/edit/delete (struktur baru)
- Menu navigation

### user.py

Fitur untuk user:

- `user_facial_glowup()`: Input tipe kulit → PDF
- `user_body_glowup()`: Input BB & TB → PDF
- `user_menu()`: Navigation menu

### main.py

Entry point aplikasi:

- `main_menu()`: Menu utama
- Routing ke user atau admin
- Exit application

## 📊 Data Structure

### Skincare JSON

```json
{
  "id": "skincare-xxx",
  "skin_type": "Oily",
  "routine": [
    {
      "step": "Cleanser",
      "product": "Gentle Foam",
      "brand": "Cetaphil"
    }
  ],
  "created_at": "2025-01-15 10:00:00"
}
```

### Workout JSON (NEW v2.1)

```json
{
  "id": "workout-xxx",
  "bmi_category": "Normal",
  "bmi_range": "18.5 - 24.9",
  "plan": [
    {
      "exercise": "Push-ups",
      "duration": "3 set x 15 reps"
    }
  ],
  "created_at": "2025-01-15 10:00:00"
}
```

## 🎓 Keunggulan Modular Design

### Untuk Presentasi:

- **Lebih mudah dijelaskan**: Setiap modul punya fungsi spesifik
- **Code review lebih cepat**: Tidak perlu scroll 1000+ baris
- **Fokus per topik**: Bisa bahas satu modul tanpa overwhelmed

### Untuk Maintenance:

- **Separation of Concerns**: Logic terpisah jelas
- **Reusability**: Helpers bisa dipakai di mana saja
- **Testability**: Mudah test satu modul tanpa jalankan semua
- **Scalability**: Mudah tambah fitur baru tanpa ganggu existing

### Untuk Collaboration:

- **Conflict-free**: Beda orang bisa edit beda file
- **Clear responsibility**: Jelas siapa ngerjain apa
- **Easy onboarding**: Newbie bisa mulai dari satu modul

## 🐛 Troubleshooting

### Error: ModuleNotFoundError: No module named 'reportlab'

```bash
pip install reportlab
```

### Error: File not found (JSON)

Aplikasi otomatis create file kosong `[]` jika belum ada

### PDF tidak terbuat

- Cek folder `glowup_pdfs/` exists (auto-created)
- Pastikan ada data skincare/workout di JSON
- Pastikan reportlab terinstall

### Text masih overflow?

v2.1 sudah fix dengan Paragraph objects. Jika masih issue:

- Check `pdf_generator.py` line untuk column widths
- Adjust di `colWidths` parameter

## 📞 Support

**Author**: Muhammad Rafif Fawwaz  
**Course**: Dasar Pemrograman - IPB  
**Version**: 2.1 (Modular)

---

## 🎯 Checklist Tugas Akhir

- ✅ Berbasis Terminal/CLI
- ✅ Database menggunakan JSON (2 files)
- ✅ Implementasi CRUD (Create, Read, Update, Delete)
- ✅ Modular & clean code structure
- ✅ Error handling & input validation
- ✅ Professional output (PDF)
- ✅ Documentation lengkap

**Ready untuk dipresentasikan! 🚀**
