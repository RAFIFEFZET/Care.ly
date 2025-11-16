# 📊 MATERI PRESENTASI - CARE.LY

## Implementasi Materi Dasar Pemrograman Python

**Proyek:** Care.ly - Skincare & Workout Recommendation System  
**Pembuat:** Muhammad Rafif Fawwaz  
**Tanggal:** November 2025

---

## 🎯 Overview Proyek

Care.ly adalah aplikasi CLI (Command Line Interface) yang memberikan rekomendasi skincare berdasarkan tipe kulit dan workout plan berdasarkan kategori BMI, dengan output berupa file PDF.

**Fitur Utama:**

- 🔐 Admin: CRUD operations untuk skincare & workout data
- 👤 User: Generate PDF rekomendasi skincare & workout
- 📄 PDF Generator: Output profesional dengan branding

---

## 📚 1. TIPE DATA KOLEKSI

### 1.1 Dictionary (Dict) ✅

**Penggunaan di `config.py`:**

```python
# Dictionary untuk menyimpan pilihan tipe kulit
SKIN_TYPES = {
    "1": "Oily",
    "2": "Dry",
    "3": "Combination",
    "4": "Sensitive",
    "5": "Normal"
}

# Dictionary nested untuk kategori BMI
BMI_CATEGORIES = {
    "1": {"name": "Underweight", "range": "< 18.5"},
    "2": {"name": "Normal", "range": "18.5 - 24.9"},
    "3": {"name": "Overweight", "range": "25 - 29.9"},
    "4": {"name": "Obese", "range": ">= 30"}
}
```

**Implementasi:**

- **Key-Value Pairs**: Menggunakan nomor sebagai key, value berupa string atau nested dictionary
- **Nested Dictionary**: `BMI_CATEGORIES` memiliki dictionary di dalam dictionary
- **Akses Data**: `SKIN_TYPES["1"]` → `"Oily"`
- **Akses Nested**: `BMI_CATEGORIES["2"]["name"]` → `"Normal"`

**Contoh Penggunaan di Admin (`admin.py` line 54-57):**

```python
def select_category(categories, prompt):
    """Generic category selection"""
    for key, value in categories.items():  # Loop dictionary
        if isinstance(value, dict):
            print(f"{key}. {value['name']} ({value['range']})")
        else:
            print(f"{key}. {value}")
```

---

### 1.2 List ✅

**Struktur Data JSON (List of Dictionaries):**

**File `data/skincare.json`:**

```json
[
  {
    "id": "uuid-1234",
    "skin_type": "Oily",
    "routine": [
      { "product": "Gentle Cleanser", "brand": "Cetaphil" },
      { "product": "Toner", "brand": "Wardah" },
      { "product": "Moisturizer", "brand": "Emina" }
    ],
    "created_at": "2025-11-16 10:30:00"
  }
]
```

**Implementasi List di Code:**

```python
# helpers.py - Load JSON menghasilkan List
def load_json(filename):
    """Load data from JSON file"""
    # Returns list of dictionaries
    return json.load(f)  # → [dict1, dict2, dict3, ...]

# admin.py - Iterasi List
def display_items(items, item_type):
    """Generic display function"""
    for idx, item in enumerate(items, 1):  # Enumerate list
        if item_type == "skincare":
            print(f"\n{idx}. Tipe Kulit: {item['skin_type']}")
            for routine_item in item['routine']:  # Nested list iteration
                print(f"   - {routine_item.get('product')}")
```

**Operasi List yang Digunakan:**

- `enumerate()` - Loop dengan index (line 38)
- `append()` - Menambah item baru (line 83, 97, 182)
- `pop()` - Menghapus item (line 230)
- List comprehension untuk filtering (implicitly in loops)

---

### 1.3 Tuple ✅

**Penggunaan Tuple untuk Unpacking:**

```python
# admin.py line 78 - Multiple assignment with tuple unpacking
parts = input_text.split('|', 1)  # Returns list
product, brand = parts[0].strip(), parts[1].strip()  # Tuple unpacking

# admin.py line 96 - Tuple unpacking
exercise, duration = parts[0].strip(), parts[1].strip()
```

**Tuple sebagai Return Value Immutable:**

```python
# Implicitly dalam enumerate()
for idx, item in enumerate(items, 1):  # Returns tuple (index, value)
    print(f"{idx}. {item}")
```

---

### 1.4 String sebagai Koleksi ✅

**String Manipulation Extensive:**

```python
# admin.py - String methods
input_text = input("Produk | Brand: ").strip()     # Remove whitespace
if input_text.lower() == 'selesai':                # Lowercase comparison
    break

parts = input_text.split('|', 1)                   # Split string by delimiter
product = parts[0].strip()                         # Clean whitespace

# user.py line 36 - Case-insensitive comparison
if skincare['skin_type'].lower() == skin_type.lower():
    routine = skincare['routine']
```

---

## 🔧 2. FUNGSI (FUNCTIONS)

### 2.1 Fungsi Sederhana

**Basic Function dengan Return Value:**

```python
# helpers.py - Function dengan return value
def get_timestamp():
    """Get current timestamp"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generate_id():
    """Generate unique ID"""
    return str(uuid.uuid4())

def calculate_bmi(weight, height):
    """Calculate BMI"""
    height_m = height / 100  # Convert cm to m
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)
```

**Karakteristik:**

- ✅ Menggunakan `def` keyword
- ✅ Docstring untuk dokumentasi
- ✅ Return value
- ✅ Parameter passing
- ✅ Type conversion & arithmetic operations

---

### 2.2 Fungsi dengan Multiple Parameters

```python
# helpers.py
def save_json(filename, data):
    """Save data to JSON file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving {filename}: {e}")
        return False
```

**Fitur:**

- Multiple parameters: `filename`, `data`
- Exception handling (try-except)
- Boolean return value
- File operations

---

### 2.3 Fungsi Generic (Reusable)

**Generic CRUD Functions - DRY Principle:**

```python
# admin.py - Generic display untuk skincare DAN workout
def display_items(items, item_type):
    """Generic display function"""
    if not items:
        print(f"\nBelum ada data {item_type}.")
        return False

    for idx, item in enumerate(items, 1):
        if item_type == "skincare":
            print(f"\n{idx}. Tipe Kulit: {item['skin_type']}")
            # Display skincare routine
        else:  # workout
            print(f"\n{idx}. Kategori: {item['bmi_category']}")
            # Display workout plan
    return True

# admin.py - Generic CRUD operations
def crud_view(file, item_type):
    """Generic view function - 1 fungsi untuk skincare & workout"""
    data = load_json(file)
    display_items(data, item_type)

def crud_add(file, item_type):
    """Generic add function - 1 fungsi untuk skincare & workout"""
    # ... implementation

def crud_edit(file, item_type):
    """Generic edit function - 1 fungsi untuk skincare & workout"""
    # ... implementation

def crud_delete(file, item_type):
    """Generic delete function - 1 fungsi untuk skincare & workout"""
    # ... implementation
```

**Keuntungan Generic Functions:**

- ✅ Mengurangi code duplication (535 lines → 316 lines, **41% reduction**)
- ✅ Easier maintenance
- ✅ Consistent behavior
- ✅ Single source of truth

---

### 2.4 Fungsi dengan Conditional Logic

```python
# helpers.py - Fungsi dengan multiple conditions
def get_bmi_category(bmi):
    """Get BMI category"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# admin.py - Fungsi untuk check duplicate
def check_duplicate(data, key, value, item_type):
    """Check for duplicate entries"""
    for item in data:
        if item[key].lower() == value.lower():
            print(f"\n{item_type.capitalize()} untuk {value} sudah ada!")
            return item
    return None
```

---

### 2.5 Fungsi dengan Loop dan Akumulasi

```python
# admin.py - Input multiple items dengan loop
def input_routine_items(item_type):
    """Generic input for routine/workout items"""
    items = []  # Initialize empty list
    num = 1

    if item_type == "skincare":
        print("\nFormat: [Produk] | [Brand]")
        while True:  # Infinite loop with break condition
            print(f"\n--- Item {num} ---")
            input_text = input("Produk | Brand (atau 'selesai'): ").strip()
            if input_text.lower() == 'selesai':
                break  # Exit loop

            # String processing
            if '|' in input_text:
                parts = input_text.split('|', 1)
                product, brand = parts[0].strip(), parts[1].strip()
            else:
                product = input_text
                brand = input("Brand: ").strip()

            if product:
                items.append({"product": product, "brand": brand})  # Accumulate
                num += 1

    return items  # Return accumulated list
```

**Konsep:**

- ✅ List accumulation
- ✅ While loop dengan break
- ✅ Counter variable
- ✅ Conditional input processing

---

## 🔍 3. SEARCHING

### 3.1 Linear Search ✅

**Searching dalam List of Dictionaries:**

```python
# user.py - Linear search untuk skincare berdasarkan skin_type
def user_facial_glowup():
    skin_type = SKIN_TYPES[skin_type_choice]
    skincare_data = load_json(SKINCARE_FILE)  # List of dicts

    # LINEAR SEARCH
    routine = None
    for skincare in skincare_data:  # O(n) complexity
        if skincare['skin_type'].lower() == skin_type.lower():  # Compare
            routine = skincare['routine']
            break  # Found - stop searching

    if not routine:  # Not found
        print(f"\n✗ Belum ada routine untuk kulit {skin_type}!")
```

**Analisis:**

- **Algorithm**: Sequential search
- **Complexity**: O(n) - worst case checks all items
- **Early Exit**: `break` saat ditemukan
- **Case-insensitive**: `.lower()` untuk string comparison

---

```python
# user.py - Linear search untuk workout berdasarkan BMI category
def user_body_glowup():
    bmi_category = get_bmi_category(bmi)
    workout_data = load_json(WORKOUT_FILE)

    # LINEAR SEARCH
    workout_plan = None
    for workout in workout_data:  # O(n)
        if workout['bmi_category'].lower() == bmi_category.lower():
            workout_plan = workout['plan']
            break

    if not workout_plan:
        print(f"\n✗ Belum ada workout plan untuk {bmi_category}!")
```

---

### 3.2 Dictionary Lookup (Hash Search) ✅

**O(1) Average Complexity:**

```python
# config.py - Dictionary untuk constant-time lookup
SKIN_TYPES = {
    "1": "Oily",    # O(1) access
    "2": "Dry",
    "3": "Combination"
}

# admin.py - Dictionary key lookup
choice = input("Pilih tipe kulit (1-5): ").strip()
if choice in SKIN_TYPES:  # O(1) membership test
    category = SKIN_TYPES[choice]  # O(1) access
```

**Analisis:**

- **Algorithm**: Hash table lookup
- **Complexity**: O(1) average case
- **Use Case**: Configuration constants, fast category lookup

---

### 3.3 Search dengan .get() Method ✅

```python
# admin.py - Safe dictionary access with default value
def display_items(items, item_type):
    for routine_item in item['routine']:
        # .get() returns default '-' if key not found
        product = routine_item.get('product', '-')
        brand = routine_item.get('brand', '-')
        print(f"   - {product} | {brand}")
```

**Keuntungan `.get()`:**

- ✅ Tidak throw `KeyError` jika key tidak ada
- ✅ Bisa set default value
- ✅ Safer untuk dynamic data

---

### 3.4 Conditional Search Pattern ✅

```python
# admin.py - Search with complex condition
def check_duplicate(data, key, value, item_type):
    """Check for duplicate entries"""
    for item in data:
        # Case-insensitive string comparison
        if item[key].lower() == value.lower():
            print(f"\n{item_type.capitalize()} untuk {value} sudah ada!")
            return item  # Return found item
    return None  # Not found
```

---

## 📊 4. SORTING

### 4.1 Implicit Sorting dengan enumerate() ✅

```python
# admin.py - Display dengan numbering (sorted by insertion order)
def display_items(items, item_type):
    """Display items dengan index berurutan"""
    for idx, item in enumerate(items, 1):  # Start from 1
        print(f"\n{idx}. Tipe Kulit: {item['skin_type']}")
```

**Konsep:**

- Data ditampilkan sesuai urutan dalam list (insertion order)
- `enumerate()` memberikan index terurut mulai dari 1
- User memilih berdasarkan nomor urut

---

### 4.2 Sorting dengan .items() ✅

```python
# admin.py - Dictionary iteration (sorted by key in Python 3.7+)
def select_category(categories, prompt):
    for key, value in categories.items():  # Preserves insertion order
        if isinstance(value, dict):
            print(f"{key}. {value['name']} ({value['range']})")
        else:
            print(f"{key}. {value}")
```

**Note:** Dictionary insertion order guaranteed di Python 3.7+

---

### 4.3 Timestamp-based Ordering ✅

```python
# helpers.py - Generate timestamp untuk ordering
def get_timestamp():
    """Get current timestamp"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Format: "2025-11-16 10:30:00" - lexicographically sortable

# admin.py - Add timestamp to new data
new_item = {
    "id": generate_id(),
    "skin_type": value,
    "routine": items,
    "created_at": get_timestamp()  # Timestamp untuk sorting
}

# Bisa di-sort dengan: sorted(data, key=lambda x: x['created_at'])
```

---

### 4.4 PDF Filename Sorting ✅

```python
# pdf_generator.py - Timestamp di filename untuk auto-sorting
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # 20251116_103000
filename = f"{PDF_OUTPUT_DIR}/Skincare_{skin_type}_{timestamp}.pdf"

# File Explorer akan otomatis sort by filename:
# Skincare_Oily_20251116_103000.pdf
# Skincare_Oily_20251116_113000.pdf  ← Newer
# Skincare_Oily_20251116_123000.pdf  ← Newest
```

**Strategi:**

- ISO 8601 format: `YYYYMMDD_HHMMSS`
- Lexicographic ordering = Chronological ordering
- Memudahkan menemukan file terbaru

---

## 🎨 5. STRING MANIPULATION (BONUS)

### 5.1 String Methods Lengkap ✅

```python
# STRIP - Remove whitespace
username = input("\nUsername: ").strip()  # "  admin  " → "admin"

# LOWER - Case conversion
if input_text.lower() == 'selesai':  # "SELESAI" → "selesai"

# SPLIT - Tokenization
parts = input_text.split('|', 1)  # "Product | Brand" → ["Product", "Brand"]
product, brand = parts[0].strip(), parts[1].strip()

# F-STRING - String formatting
print(f"\n{idx}. Tipe Kulit: {item['skin_type']}")
filename = f"{PDF_OUTPUT_DIR}/Skincare_{skin_type}_{timestamp}.pdf"

# STRFTIME - DateTime formatting
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# GET - Safe dictionary access
product = routine_item.get('product', '-')
```

---

### 5.2 String Concatenation & Formatting ✅

```python
# pdf_generator.py - Complex string formatting
title = Paragraph(
    "CARE.LY FACIAL - SKINCARE ROUTINE",
    title_style
)

subtitle = Paragraph(
    f"Tipe Kulit: <b>{skin_type}</b>",  # Bold formatting
    subtitle_style
)

footer_text = (
    f"Generated on {datetime.now().strftime('%d %B %Y, %H:%M')}<br/>"
    f"Care.ly - Stay Beautiful!<br/>"
    f"Visit us at www.carely.com"
)
```

---

### 5.3 String Validation & Comparison ✅

```python
# admin.py - String validation
if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
    print("\n✓ Login berhasil!")

# Case-insensitive comparison
if skincare['skin_type'].lower() == skin_type.lower():
    routine = skincare['routine']

# String membership test
if '|' in input_text:
    parts = input_text.split('|', 1)
```

---

## 📈 STATISTIK IMPLEMENTASI

| Materi             | Jumlah Implementasi | File Utama                          |
| ------------------ | ------------------- | ----------------------------------- |
| **Dictionary**     | 8+ occurrences      | `config.py`, `admin.py`             |
| **List**           | 20+ operations      | `admin.py`, `user.py`, `helpers.py` |
| **Tuple**          | 5+ unpacking        | `admin.py`                          |
| **Function**       | 25+ functions       | All modules                         |
| **Linear Search**  | 4+ implementations  | `user.py`, `admin.py`               |
| **Dict Lookup**    | 10+ uses            | `admin.py`, `user.py`               |
| **String Methods** | 50+ calls           | All modules                         |

---

## 🎯 KESIMPULAN

### Implementasi Materi yang Diterapkan:

✅ **Tipe Data Koleksi**

- Dictionary (nested & simple)
- List (with enumerate, append, pop)
- Tuple (unpacking)
- String (as collection)

✅ **Fungsi**

- 25+ fungsi dengan berbagai kompleksitas
- Generic functions (DRY principle)
- Parameter passing & return values
- Docstrings untuk dokumentasi

✅ **Searching**

- Linear search O(n) untuk data skincare & workout
- Dictionary lookup O(1) untuk categories
- `.get()` method untuk safe access
- Case-insensitive search

✅ **Sorting**

- Timestamp-based ordering
- Enumerate untuk display ordering
- Lexicographic filename sorting
- Dictionary insertion order preservation

### Kualitas Code:

📊 **Metrics:**

- 6 modular files (separation of concerns)
- 316 lines di `admin.py` (reduced from 535 - 41%)
- Generic CRUD functions untuk reusability
- Comprehensive error handling
- Clean code with docstrings

🎨 **Best Practices:**

- DRY (Don't Repeat Yourself)
- Separation of concerns (config, helpers, admin, user, PDF)
- Consistent naming conventions
- Type hints ready architecture
- Professional folder structure

---

## 💡 HIGHLIGHT UNTUK PRESENTASI

1. **Generic CRUD Functions** → Menunjukkan pemahaman abstraksi
2. **Nested Dictionary di BMI_CATEGORIES** → Struktur data kompleks
3. **Linear Search dengan Early Exit** → Optimasi algoritma
4. **String Manipulation** → .strip(), .lower(), .split() untuk robust input
5. **List Accumulation di input_routine_items()** → Loop dengan kondisi dinamis
6. **Timestamp Ordering** → Sortable filename untuk file management

---

## 🚀 DEMO FLOW

1. **Admin Login** → String comparison & validation
2. **CRUD Skincare** → List operations, dictionary usage
3. **User Facial Care** → Linear search, PDF generation
4. **User Body Care** → BMI calculation, nested dict access, workout search
5. **Output PDF** → String formatting, file operations

---

**Prepared by:** Muhammad Rafif Fawwaz  
**Course:** Dasar Pemrograman Python  
**Institution:** IPB University  
**Date:** November 2025

**GitHub:** [Care.ly Repository](https://github.com/RAFIFEFZET/Care.ly)
