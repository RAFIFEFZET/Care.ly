# Care.ly - Healthcare & Fitness Recommendation System

> Aplikasi CLI berbasis Python untuk rekomendasi skincare dan workout dengan output PDF profesional

## 📋 Overview

**Care.ly** adalah sistem rekomendasi healthcare yang menyediakan:

- 🧴 **Facial Care**: Rekomendasi skincare berdasarkan tipe kulit
- 💪 **Body Care**: Rekomendasi workout berdasarkan BMI

## ✨ Features

- ✅ CLI-based application
- ✅ JSON database (2 files)
- ✅ Complete CRUD operations (Admin)
- ✅ PDF output generation
- ✅ BMI calculation
- ✅ Modular architecture (6 modules)
- ✅ Text wrapping in PDF tables
- ✅ Professional design

## 📁 Project Structure

```
Care.ly/
├── main.py              # Entry point
├── config.py            # Configuration & constants
├── helpers.py           # Utility functions
├── pdf_generator.py     # PDF generation
├── admin.py             # Admin CRUD operations
├── user.py              # User features
├── data/                # JSON database
│   ├── skincare.json
│   └── workouts.json
├── docs/                # Documentation
│   ├── README_V2.1.md
│   ├── MODULE_EXPLANATION.md
│   ├── PRESENTATION_CHEATSHEET.md
│   └── CHANGELOG_*.md
└── output_pdfs/         # Generated PDF files
```

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.6+
pip install reportlab
```

### Run Application

```bash
python main.py
```

### Admin Login

- **Username**: `admin`
- **Password**: `admin123`

## 💻 Usage

### User Flow

1. Select **User - Care Services**
2. Choose:
   - **Facial Care**: Input skin type → Get skincare PDF
   - **Body Care**: Input weight & height → Get workout PDF
3. PDF automatically saved to `output_pdfs/`

### Admin Flow

1. Select **Admin - Manage Data**
2. Login with credentials
3. Manage:
   - **Skincare**: CRUD operations for skincare routines
   - **Workout**: CRUD operations for workout plans

## 📊 Data Structure

### Skincare

```json
{
  "skin_type": "Oily",
  "routine": [
    {
      "product": "Oil-Free Gel Cleanser",
      "brand": "Cetaphil"
    }
  ]
}
```

### Workout

```json
{
  "bmi_category": "Normal",
  "plan": [
    {
      "exercise": "Push-ups",
      "duration": "3 set x 15 reps"
    }
  ]
}
```

## 🎨 PDF Output

- **Skincare PDF**: Blue theme (#2E86AB)
  - 3 columns: No | Product | Brand
  - Text wrapping enabled
- **Workout PDF**: Orange theme (#F18F01)
  - 2 columns: No | Exercise & Duration
  - BMI info included

## 🔧 Modules

| Module           | Purpose              | Lines |
| ---------------- | -------------------- | ----- |
| config.py        | Constants & settings | 35    |
| helpers.py       | Utility functions    | 73    |
| pdf_generator.py | PDF generation       | 195   |
| admin.py         | CRUD operations      | 316   |
| user.py          | User features        | 100+  |
| main.py          | Entry point          | 50    |

## 📚 Documentation

Full documentation available in `docs/` folder:

- **README_V2.1.md**: Complete guide
- **MODULE_EXPLANATION.md**: Detailed module breakdown
- **PRESENTATION_CHEATSHEET.md**: Quick reference
- **CHANGELOG\_\*.md**: Version history

## 🎓 Academic Context

**Course**: Dasar Pemrograman - IPB  
**Author**: Muhammad Rafif Fawwaz  
**Version**: 2.1.2  
**Date**: November 2025

## ✅ Requirements Checklist

- [x] Berbasis Terminal/CLI
- [x] Database menggunakan JSON
- [x] Implementasi CRUD lengkap
- [x] Modular code structure
- [x] Error handling
- [x] Professional output (PDF)
- [x] Clean & organized file structure

## 🎯 Key Highlights

### Code Optimization

- **Admin module**: 535 → 316 lines (41% reduction)
- **Generic CRUD**: 4 functions handle all operations
- **DRY principle**: No code duplication

### Data Simplification

- **Skincare**: Removed redundant 'step' field
- **Workout**: Simplified to exercise + duration only
- **Cleaner structure**: Easier to maintain

## 🐛 Troubleshooting

### Module not found

```bash
pip install reportlab
```

### File not found

Application auto-creates folders and files if missing

### PDF not generated

Check `output_pdfs/` folder permissions

## 📞 Support

For issues or questions, refer to detailed documentation in `docs/` folder.

---

**Status**: ✅ Production Ready  
**License**: Academic Project  
**Repository**: Care.ly

Made with ❤️ for healthcare and fitness enthusiasts
