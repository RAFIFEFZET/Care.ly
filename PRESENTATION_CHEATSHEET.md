# GlowUp Gang v2.1.1 - Quick Reference

## 1-Page Cheat Sheet untuk Presentasi

---

## 📊 Project Stats

```
Total Files:    6 modules + 2 JSON databases
Total Lines:    ~770 lines (down from 1000+)
Languages:      Python 3.6+
Dependencies:   reportlab (PDF generation)
Database:       JSON (2 files)
Output:         PDF files
```

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────┐
│              main.py (50 lines)                 │
│                 Entry Point                      │
└────────────┬────────────────────────────────────┘
             │
    ┌────────┴────────┐
    │                 │
┌───▼────┐      ┌────▼─────┐
│ user.py│      │ admin.py │
│(100 L) │      │ (316 L)  │◄────┐
└───┬────┘      └────┬─────┘     │
    │                │            │
    └────────┬───────┘            │
             │                    │
    ┌────────▼─────────┐          │
    │  pdf_generator.py│          │
    │    (195 lines)   │          │
    └────────┬─────────┘          │
             │                    │
    ┌────────▼─────────┐          │
    │    helpers.py    │──────────┘
    │    (73 lines)    │
    └────────┬─────────┘
             │
    ┌────────▼─────────┐
    │     config.py    │
    │    (36 lines)    │
    └──────────────────┘
```

---

## 🎯 Key Features

### ✅ Requirements Met

- [x] Berbasis Terminal/CLI
- [x] Database menggunakan JSON
- [x] CRUD Complete (Create, Read, Update, Delete)
- [x] Modular Architecture
- [x] Error Handling
- [x] Professional Output (PDF)

### 🌟 Special Features

- PDF generation with text wrapping
- BMI calculation & categorization
- Simplified workout structure (no equipment/brand)
- Generic CRUD functions (DRY principle)
- Color-coded PDFs (blue/orange)

---

## 📦 Module Breakdown

| Module               | Lines | Purpose       | Key Functions                                   |
| -------------------- | ----- | ------------- | ----------------------------------------------- |
| **config.py**        | 36    | Constants     | ADMIN_USERNAME, SKIN_TYPES, BMI_CATEGORIES      |
| **helpers.py**       | 73    | Utilities     | calculate_bmi(), load_json(), save_json()       |
| **pdf_generator.py** | 195   | PDF Output    | generate_skincare_pdf(), generate_workout_pdf() |
| **admin.py**         | 316   | CRUD Ops      | crud_view/add/edit/delete(), admin_menu()       |
| **user.py**          | 100+  | User Features | user_facial_glowup(), user_body_glowup()        |
| **main.py**          | 50    | Entry Point   | main_menu()                                     |

---

## 🔥 Admin.py Optimization Highlight

### Before v2.1.1:

```python
# 535 lines - 8 specific functions
admin_view_skincare()     # 50 lines
admin_add_skincare()      # 60 lines
admin_edit_skincare()     # 55 lines
admin_delete_skincare()   # 42 lines
admin_view_workout()      # 50 lines
admin_add_workout()       # 90 lines
admin_edit_workout()      # 78 lines
admin_delete_workout()    # 44 lines
```

### After v2.1.1:

```python
# 316 lines - 4 generic functions
crud_view(file, type)     # 15 lines - handles both!
crud_add(file, type)      # 60 lines - handles both!
crud_edit(file, type)     # 50 lines - handles both!
crud_delete(file, type)   # 40 lines - handles both!
```

**Result: 41% code reduction!** 🎉

---

## 💻 Usage Flow

### User Flow:

```
1. Run: python main.py
2. Select: User Menu
3. Choose: Facial or Body GlowUp
4. Input: Skin type / Weight & Height
5. Output: PDF generated in glowup_pdfs/
```

### Admin Flow:

```
1. Run: python main.py
2. Select: Admin Menu
3. Login: admin / admin123
4. Choose: Kelola Skincare or Workout
5. CRUD: View/Add/Edit/Delete
6. Data: Saved to JSON
```

---

## 🎨 PDF Examples

### Skincare PDF (Blue Theme):

```
┌─────────────────────────────────────┐
│ SKINCARE ROUTINE - OILY SKIN       │
│ Generated: 2025-11-12 10:30:00     │
├──────┬────────┬──────────┬─────────┤
│ No   │ Step   │ Produk   │ Brand   │
├──────┼────────┼──────────┼─────────┤
│ 1    │Cleanser│Gentle... │Cetaphil │
│ 2    │ Toner  │Pore...   │Paula's  │
└──────┴────────┴──────────┴─────────┘
```

### Workout PDF (Orange Theme):

```
┌─────────────────────────────────────┐
│ WORKOUT PLAN - NORMAL (BMI: 22.5)  │
│ BB: 70kg | TB: 175cm               │
├──────┬──────────────────────────────┤
│ No   │ Exercise & Duration          │
├──────┼──────────────────────────────┤
│ 1    │ Push-ups                     │
│      │ 3 set x 15 reps              │
├──────┼──────────────────────────────┤
│ 2    │ Jogging                      │
│      │ 30 menit, 3x/minggu          │
└──────┴──────────────────────────────┘
```

---

## 🎤 Presentation Script

### Opening (30 sec):

> "GlowUp Gang adalah aplikasi CLI untuk rekomendasi skincare dan workout dengan output PDF. Aplikasi ini memenuhi semua requirements: CLI-based, JSON database, dan complete CRUD operations."

### Architecture (1 min):

> "Aplikasi terdiri dari 6 modul dengan separation of concerns yang jelas. Config untuk konstanta, helpers untuk utilities, pdf_generator untuk output, admin untuk CRUD, user untuk features, dan main sebagai entry point."

### Key Innovation (1 min):

> "Yang menarik adalah di admin.py, saya implementasi generic CRUD functions. Daripada 8 fungsi terpisah untuk skincare dan workout, saya buat 4 fungsi generic yang handle keduanya dengan parameter. Hasilnya code reduction 41% dari 535 jadi 316 lines."

### Demo (2 min):

> "Let me show you..." [Demo user flow: input data → generate PDF → show result]

### Closing (30 sec):

> "Dengan modular design ini, code lebih maintainable, easy to extend, dan yang penting: mudah dijelaskan saat presentasi!"

---

## 🐛 Common Questions & Answers

**Q: Kenapa pakai JSON bukan SQL?**  
A: Requirement tugas menyebutkan "database menggunakan JSON"

**Q: Kenapa admin hardcoded?**  
A: Untuk simplify flow, fokus ke core features (CRUD & PDF generation)

**Q: Kenapa workout disederhanakan?**  
A: Equipment dan brand tidak terlalu penting, fokus ke exercise dan duration

**Q: Bagaimana handle text overflow di PDF?**  
A: Pakai Paragraph objects dari reportlab, text otomatis wrap

**Q: Kenapa buat modular?**  
A: Untuk easier presentation, maintenance, dan follow best practices

---

## ✅ Checklist Presentasi

- [ ] Show project structure (6 modules)
- [ ] Explain each module's purpose
- [ ] Highlight admin.py optimization (41% reduction)
- [ ] Demo user flow (generate PDF)
- [ ] Demo admin flow (CRUD operations)
- [ ] Show PDF output (text wrapping works!)
- [ ] Explain generic function pattern
- [ ] Q&A preparation

---

## 📁 File Locations

```
Projek/
├── main.py              # python main.py ← Run this!
├── config.py
├── helpers.py
├── pdf_generator.py
├── admin.py
├── user.py
├── glowup_skincare.json
├── glowup_workouts.json
└── glowup_pdfs/         # Output folder
```

---

## 🚀 Quick Commands

```bash
# Run application
python main.py

# Check line count
(Get-Content admin.py | Measure-Object -Line).Lines

# View JSON data
cat glowup_skincare.json
cat glowup_workouts.json
```

---

**Version:** v2.1.1 (Optimized)  
**Author:** Muhammad Rafif Fawwaz  
**Course:** Dasar Pemrograman - IPB  
**Date:** November 2025

**Status:** ✅ Ready for Presentation!
