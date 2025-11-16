# GlowUp Gang - Module Explanation Guide

## Panduan Penjelasan untuk Presentasi

---

## 🎯 Overview Singkat

**GlowUp Gang v2.1** adalah aplikasi CLI untuk rekomendasi skincare & workout dengan output PDF. Kode dipisah jadi 6 modul untuk kemudahan presentasi dan maintenance.

---

## 📦 1. config.py (36 baris)

### Apa isi modul ini?

Semua **konstanta** dan **konfigurasi** aplikasi dalam satu tempat.

### Kenapa terpisah?

- ✅ Gampang update setting (misal: ganti path file)
- ✅ Tidak hardcode di mana-mana
- ✅ Single source of truth

### Isi penting:

```python
# File paths
SKINCARE_FILE = "glowup_skincare.json"
WORKOUT_FILE = "glowup_workouts.json"

# Admin credentials (hardcoded sesuai requirements)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Skin types mapping (untuk input user)
SKIN_TYPES = {
    "1": "Oily",
    "2": "Dry",
    # dst...
}

# BMI categories dengan ranges
BMI_CATEGORIES = {
    "1": {"name": "Underweight", "range": "< 18.5"},
    # dst...
}

# Color scheme untuk PDF
COLOR_SKINCARE = "#2E86AB"  # Biru
COLOR_WORKOUT = "#F18F01"   # Orange
```

### Cara kerja:

Modul lain import dari sini:

```python
from config import ADMIN_USERNAME, SKIN_TYPES
```

---

## 🔧 2. helpers.py (73 baris)

### Apa isi modul ini?

Fungsi-fungsi **utility** yang dipakai berulang kali di modul lain.

### Kenapa terpisah?

- ✅ DRY principle (Don't Repeat Yourself)
- ✅ Reusable di semua modul
- ✅ Mudah di-maintain (fix 1 tempat, semua terfix)

### Fungsi-fungsi penting:

#### 1. Terminal Management

```python
clear_screen()  # Bersihkan layar (os.system('cls'))
pause()         # Input("Tekan enter...")
```

#### 2. JSON Database I/O

```python
load_json(filename)           # Baca file JSON → Python list
save_json(filename, data)     # Simpan Python list → JSON file
```

- Auto-create file kosong jika belum ada
- Encoding UTF-8 untuk bahasa Indonesia
- Error handling

#### 3. BMI Calculations

```python
calculate_bmi(weight, height)  # Return: BMI rounded 2 decimal
get_bmi_category(bmi)          # Return: "Normal", "Overweight", dll
```

#### 4. Utilities

```python
generate_id()      # UUID unik untuk data baru
get_timestamp()    # Format: "2025-01-15 10:30:00"
ensure_pdf_directory()  # Create folder glowup_pdfs/ jika belum ada
```

### Cara kerja:

Modul lain tinggal import:

```python
from helpers import calculate_bmi, load_json
```

---

## 📄 3. pdf_generator.py (195 baris)

### Apa isi modul ini?

Logic untuk **generate PDF** dengan reportlab library.

### Kenapa terpisah?

- ✅ PDF generation kompleks, butuh file sendiri
- ✅ Mudah update styling tanpa ganggu logic bisnis
- ✅ 2 jenis PDF (skincare & workout) dalam 1 modul

### Fungsi utama:

#### 1. generate_skincare_pdf()

**Input**: skin_type, routine_data  
**Output**: File PDF di folder `glowup_pdfs/`

**Fitur:**

- Header dengan skin type & timestamp
- Tabel 4 kolom: No | Step | Produk | Brand
- **Text wrapping** dengan `Paragraph` objects
- Color scheme biru (#2E86AB)

**Struktur tabel:**

```python
table_data = [
    [Paragraph("No"), Paragraph("Step"), ...],  # Header
    [Paragraph("1"), Paragraph("Cleanser"), ...]  # Data row
]
```

**Column widths:**

```python
colWidths = [0.5*inch, 1.8*inch, 2.2*inch, 2*inch]
```

#### 2. generate_workout_pdf()

**Input**: bmi, bmi_category, weight, height, workout_data  
**Output**: File PDF

**Fitur:**

- Info BMI, kategori, BB, TB
- Tabel **2 kolom saja**: No | Exercise & Duration
- **Text wrapping** dengan `Paragraph`
- Color scheme orange (#F18F01)

**Perbedaan dari v2.0:**

- ❌ Tidak ada kolom Equipment & Brand lagi
- ✅ Lebih simple, fokus ke exercise & duration

**Struktur tabel:**

```python
table_data = [
    [Paragraph("No"), Paragraph("Exercise & Duration")],
    [Paragraph("1"), Paragraph("Push-ups<br/>3 set x 15 reps")]
]
```

### Key Feature: Text Wrapping

**Masalah v2.0:** Text panjang overflow keluar tabel

**Solusi v2.1:**

```python
# Sebelum (v2.0) - String biasa
cell = "Text panjang yang akan overflow"

# Sekarang (v2.1) - Paragraph object
cell = Paragraph("Text panjang yang auto wrap", style)
```

Paragraph otomatis wrap text sesuai column width.

---

## 👨‍💼 4. admin.py (316 baris - OPTIMIZED!)

### Apa isi modul ini?

Semua fungsi untuk **Admin** - CRUD operations dengan **generic functions**.

### Kenapa terpisah?

- ✅ Admin logic beda dari user logic
- ✅ Generic CRUD functions (reusable untuk skincare & workout)
- ✅ Code reduction 41% (535 → 316 lines)

### ⭐ OPTIMIZATION STRATEGY:

**Before (v2.0):**

- 8 fungsi terpisah: admin_view_skincare(), admin_add_skincare(), dll
- Banyak duplicate code
- Hard to maintain

**After (v2.1 OPTIMIZED):**

- 4 generic functions: crud_view(), crud_add(), crud_edit(), crud_delete()
- 1 logic untuk semua (skincare & workout)
- Easy to extend

### Struktur fungsi:

#### A. Authentication

```python
admin_login()  # Validasi username & password
```

#### B. Generic Helper Functions

```python
display_items(items, type)        # Display skincare/workout
select_category(categories, msg)  # Generic category selection
input_routine_items(type)         # Input skincare/workout items
check_duplicate(data, key, val)   # Check duplicate entries
```

#### C. Generic CRUD Operations (4 fungsi untuk SEMUA!)

```python
crud_view(file, type)    # Read - lihat semua
crud_add(file, type)     # Create - tambah baru
crud_edit(file, type)    # Update - edit existing
crud_delete(file, type)  # Delete - hapus data
```

**Parameter `type`:** "skincare" atau "workout"  
**Satu function handle keduanya!**

**Flow crud_add() - Generic untuk Skincare & Workout:**

1. **Select category:**

   - Skincare: Pilih skin type (1-5)
   - Workout: Pilih BMI category (1-4)

2. **Input items** dengan `input_routine_items(type)`:

   - Skincare: Step | Produk | Brand
   - Workout: Exercise | Duration (SIMPLIFIED!)

3. **Check duplicate** dengan `check_duplicate()`:

   - Jika ada → tanya overwrite?
   - Jika tidak → create new

4. **Save to JSON** dengan `save_json()`

**Contoh penggunaan:**

```python
# Skincare
crud_add(SKINCARE_FILE, "skincare")

# Workout
crud_add(WORKOUT_FILE, "workout")
```

**Magic:** Satu function, handle kedua tipe dengan parameter `type`!

#### D. Menu Navigation (2 fungsi - OPTIMIZED!)

```python
crud_menu(file, type)  # Generic CRUD menu
admin_menu()           # Main admin dashboard
```

**Before (v2.0):**

- admin_skincare_menu() - terpisah
- admin_workout_menu() - terpisah

**After (v2.1 OPTIMIZED):**

- crud_menu(SKINCARE_FILE, "skincare")
- crud_menu(WORKOUT_FILE, "workout")
- **Satu function untuk semua menu!**

### Key Points untuk Presentasi:

- ✅ **Generic CRUD** - 1 logic untuk semua
- ✅ **Code reduction 41%** (535 → 316 lines)
- ✅ **DRY principle** - Don't Repeat Yourself
- ✅ **Easy to extend** - mau tambah tipe baru? Tinggal pass parameter!
- ✅ **Maintainable** - fix bug 1 tempat, semua terfix

---

## 🧑‍🤝‍🧑 5. user.py (100+ baris)

### Apa isi modul ini?

Fitur untuk **User** - generate PDF recommendations.

### Kenapa terpisah?

- ✅ User flow beda dari admin
- ✅ Fokus ke PDF generation (pakai pdf_generator.py)
- ✅ Simple & clean

### Fungsi utama:

#### 1. user_facial_glowup()

**Flow:**

1. Tampilkan pilihan skin type (1-5)
2. User pilih
3. Load data dari `glowup_skincare.json`
4. Cari routine yang cocok
5. Call `generate_skincare_pdf()`
6. Tampilkan path PDF

**Error handling:**

- Pilihan invalid → pesan error
- Data tidak ada → info "Hubungi admin"

#### 2. user_body_glowup()

**Flow:**

1. Input berat badan (kg)
2. Input tinggi badan (cm)
3. Hitung BMI dengan `helpers.calculate_bmi()`
4. Tentukan kategori dengan `helpers.get_bmi_category()`
5. Load workout dari `glowup_workouts.json`
6. Cari workout sesuai kategori
7. Call `generate_workout_pdf()`
8. Tampilkan path PDF

**Error handling:**

- Input bukan angka → ValueError catch
- BB/TB <= 0 → validasi
- Workout tidak ada → info "Hubungi admin"

#### 3. user_menu()

Menu navigation untuk user (pilih Facial atau Body)

### Key Points:

- ✅ Simple user experience
- ✅ Auto-generate PDF tanpa user perlu tau complexity
- ✅ Clear error messages

---

## 🏁 6. main.py (50 baris)

### Apa isi modul ini?

**Entry point** aplikasi - main menu & routing.

### Kenapa terpisah?

- ✅ Clean separation: main.py cuma routing
- ✅ Import semua modul lain
- ✅ Mudah lihat big picture aplikasi

### Fungsi:

#### main_menu()

**Flow:**

```
┌─────────────────────────┐
│   GLOWUP GANG MAIN      │
│  1. User                │
│  2. Admin               │
│  0. Exit                │
└─────────────────────────┘
         │
    ┌────┴────┐
    │         │
  User      Admin
    │         │
user_menu() admin_login()
            │
        admin_menu()
```

**Logic:**

```python
if choice == "1":
    user_menu()  # dari user.py
elif choice == "2":
    if admin_login():  # dari admin.py
        admin_menu()   # dari admin.py
elif choice == "0":
    exit
```

#### if **name** == "**main**"

Standard Python pattern:

```python
if __name__ == "__main__":
    main_menu()
```

Artinya: "Jalankan main_menu() hanya jika file ini dijalankan langsung"

### Cara run:

```bash
python main.py
```

---

## 🔄 How Modules Work Together

```
main.py
  │
  ├─→ config.py (import constants)
  │
  ├─→ admin.py
  │     ├─→ helpers.py (load_json, save_json, dll)
  │     └─→ config.py (ADMIN_USERNAME, SKIN_TYPES, dll)
  │
  └─→ user.py
        ├─→ helpers.py (calculate_bmi, load_json)
        ├─→ config.py (SKIN_TYPES, BMI_CATEGORIES)
        └─→ pdf_generator.py
              ├─→ helpers.py (ensure_pdf_directory)
              └─→ config.py (colors, paths)
```

**Dependency flow:**

1. `config.py` - tidak depend ke siapa-siapa (base)
2. `helpers.py` - depend ke `config.py` saja
3. `pdf_generator.py` - depend ke `helpers` & `config`
4. `admin.py` - depend ke `helpers` & `config`
5. `user.py` - depend ke semua (helpers, config, pdf_generator)
6. `main.py` - import admin & user, orchestrate flow

---

## 📊 Data Flow Example

### Contoh: User Generate Workout PDF

1. **main.py**: User pilih menu 1 → call `user_menu()`
2. **user.py**: User pilih Body GlowUp → call `user_body_glowup()`
3. **user.py**: Input BB=70, TB=175
4. **helpers.py**: `calculate_bmi(70, 175)` → return 22.86
5. **helpers.py**: `get_bmi_category(22.86)` → return "Normal"
6. **user.py**: `load_json(WORKOUT_FILE)` → load workout data
7. **user.py**: Cari workout kategori "Normal" → found!
8. **pdf_generator.py**: `generate_workout_pdf(...)` → create PDF
9. **user.py**: Tampilkan path PDF ke user

---

## 🎤 Tips Presentasi

### 1. Mulai dari Big Picture

"Aplikasi ini punya 6 modul, masing-masing punya tugas spesifik..."

### 2. Jelaskan Dependency

"config.py adalah base, semua modul import dari sini..."

### 3. Demo Flow

"Saya demo user flow: input BB & TB → hitung BMI → generate PDF"

### 4. Highlight Key Features

- ✅ Modular design
- ✅ Simplified workout structure (v2.1)
- ✅ Text wrapping di PDF (v2.1)
- ✅ Complete CRUD
- ✅ Error handling

### 5. Show Code Structure

```
Before (v2.0): 1 file - 1000+ baris ❌
After (v2.1):  6 files - average 100-200 baris ✅
```

### 6. Explain Benefits

- Mudah dibaca
- Mudah di-maintain
- Mudah add fitur baru
- Mudah collaborate

---

## 🐞 Common Questions

**Q: Kenapa tidak pakai database SQL?**  
A: Requirements tugas: "database menggunakan JSON"

**Q: Kenapa admin credentials hardcoded?**  
A: v2.0 requirement: simplify flow, no user registration

**Q: Kenapa pakai reportlab?**  
A: Untuk professional output (PDF), bukan cuma print ke terminal

**Q: Kenapa workout disederhanakan di v2.1?**  
A: User feedback: equipment & brand tidak terlalu penting, focus ke exercise

**Q: Bagaimana handle text overflow?**  
A: Pakai Paragraph objects dari reportlab, otomatis wrap

---

## ✅ Checklist Presentasi

- [ ] Jelaskan problem yang diselesaikan (skincare & workout recommendation)
- [ ] Show struktur modular (6 files)
- [ ] Explain dependency antar modul
- [ ] Demo admin flow (add workout dengan format baru)
- [ ] Demo user flow (generate PDF)
- [ ] Show PDF output (text wrapping works!)
- [ ] Highlight key improvements v2.1
- [ ] Q&A preparation

**Good luck! 🚀**
