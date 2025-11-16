"""
Admin functions untuk Care.ly - OPTIMIZED VERSION
Berisi semua CRUD operations untuk skincare dan workout
"""

from helpers import *
from config import *

def admin_login():
    """Admin login"""
    clear_screen()
    print("=" * 50)
    print("ADMIN LOGIN - CARE.LY")
    print("=" * 50)
    
    username = input("\nUsername: ").strip()
    password = input("Password: ").strip()
    
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("\n✓ Login berhasil! Selamat datang, Admin!")
        pause()
        return True
    else:
        print("\n✗ Username atau password salah!")
        pause()
        return False

# ===========================
# GENERIC CRUD FUNCTIONS
# ===========================

def display_items(items, item_type):
    """Generic display function"""
    if not items:
        print(f"\nBelum ada data {item_type}.")
        return False
    
    for idx, item in enumerate(items, 1):
        if item_type == "skincare":
            print(f"\n{idx}. Tipe Kulit: {item['skin_type']}")
            print("   Routine:")
            for routine_item in item['routine']:
                print(f"   - {routine_item.get('product', '-')} | {routine_item.get('brand', '-')}")
        else:  # workout
            print(f"\n{idx}. Kategori: {item['bmi_category']} ({item['bmi_range']})")
            print("   Workout Plan:")
            for ex in item['plan']:
                print(f"   - {ex['exercise']} | {ex['duration']}")
    return True

def select_category(categories, prompt):
    """Generic category selection"""
    for key, value in categories.items():
        if isinstance(value, dict):
            print(f"{key}. {value['name']} ({value['range']})")
        else:
            print(f"{key}. {value}")
    
    choice = input(f"\n{prompt}: ").strip()
    return choice if choice in categories else None

def input_routine_items(item_type):
    """Generic input for routine/workout items"""
    items = []
    num = 1
    
    if item_type == "skincare":
        print("\nFormat: [Produk] | [Brand]")
        print("Contoh: Gentle Daily Cleanser | Cetaphil")
        while True:
            print(f"\n--- Item {num} ---")
            input_text = input("Produk | Brand (atau 'selesai'): ").strip()
            if input_text.lower() == 'selesai':
                break
            
            if '|' in input_text:
                parts = input_text.split('|', 1)
                product, brand = parts[0].strip(), parts[1].strip()
            else:
                product = input_text
                brand = input("Brand: ").strip()
            
            if product:
                items.append({"product": product, "brand": brand or "-"})
                num += 1
    else:  # workout
        print("\nFormat: [Exercise] | [Duration]")
        print("Contoh: Push-ups | 3 set x 15 reps")
        while True:
            print(f"\n--- Exercise {num} ---")
            input_text = input("Exercise | Duration (atau 'selesai'): ").strip()
            if input_text.lower() == 'selesai':
                break
            
            if '|' in input_text:
                parts = input_text.split('|', 1)
                exercise, duration = parts[0].strip(), parts[1].strip()
            else:
                exercise = input_text
                duration = input("Duration/Set: ").strip()
            
            if exercise:
                items.append({"exercise": exercise, "duration": duration or "-"})
                num += 1
    
    return items

def check_duplicate(data, key, value, item_type):
    """Check for duplicate entries"""
    for item in data:
        if item[key].lower() == value.lower():
            print(f"\n{item_type.capitalize()} untuk {value} sudah ada!")
            return item
    return None

# ===========================
# UNIFIED CRUD OPERATIONS
# ===========================

def crud_view(file, item_type):
    """Generic view function"""
    clear_screen()
    print("=" * 50)
    print(f"DAFTAR {item_type.upper()}")
    print("=" * 50)
    
    data = load_json(file)
    display_items(data, item_type)
    pause()

def crud_add(file, item_type):
    """Generic add function"""
    clear_screen()
    print("=" * 50)
    print(f"TAMBAH {item_type.upper()}")
    print("=" * 50)
    
    # Select category
    if item_type == "skincare":
        print("\nTipe Kulit:")
        choice = select_category(SKIN_TYPES, "Pilih tipe kulit (1-5)")
        if not choice:
            print("Pilihan tidak valid!")
            pause()
            return
        category = SKIN_TYPES[choice]
        key, value = "skin_type", category
        bmi_cat = None
    else:  # workout
        print("\nKategori BMI:")
        choice = select_category(BMI_CATEGORIES, "Pilih kategori (1-4)")
        if not choice:
            print("Pilihan tidak valid!")
            pause()
            return
        bmi_cat = BMI_CATEGORIES[choice]
        category = bmi_cat['name']
        key, value = "bmi_category", category
    
    # Input items
    print(f"\nMasukkan {item_type} untuk {category}")
    items = input_routine_items(item_type)
    
    if not items:
        print(f"{item_type.capitalize()} tidak boleh kosong!")
        pause()
        return
    
    # Check duplicate
    data = load_json(file)
    duplicate = check_duplicate(data, key, value, item_type)
    
    if duplicate:
        overwrite = input("Timpa data? (y/n): ").strip().lower()
        if overwrite == 'y':
            duplicate['routine' if item_type == "skincare" else 'plan'] = items
            duplicate['updated_at'] = get_timestamp()
            save_json(file, data)
            print(f"\n✓ {item_type.capitalize()} berhasil diperbarui!")
        pause()
        return
    
    # Add new
    new_item = {
        "id": generate_id(),
        key: value,
        ('routine' if item_type == "skincare" else 'plan'): items,
        "created_at": get_timestamp()
    }
    
    if item_type == "workout":
        new_item['bmi_range'] = bmi_cat['range']
    
    data.append(new_item)
    
    if save_json(file, data):
        print(f"\n✓ {item_type.capitalize()} berhasil ditambahkan!")
    else:
        print("\n✗ Gagal menambahkan!")
    
    pause()

def crud_edit(file, item_type):
    """Generic edit function"""
    clear_screen()
    print("=" * 50)
    print(f"EDIT {item_type.upper()}")
    print("=" * 50)
    
    data = load_json(file)
    
    if not display_items(data, item_type):
        pause()
        return
    
    try:
        choice = int(input("\nPilih nomor: "))
        if choice < 1 or choice > len(data):
            print("Nomor tidak valid!")
            pause()
            return
        
        selected = data[choice - 1]
        
        # Display current
        print(f"\n{item_type.capitalize()} saat ini:")
        key = 'routine' if item_type == "skincare" else 'plan'
        for idx, item in enumerate(selected[key], 1):
            if item_type == "skincare":
                print(f"{idx}. {item.get('product')} | {item.get('brand')}")
            else:
                print(f"{idx}. {item['exercise']} | {item['duration']}")
        
        # Input new
        print(f"\nMasukkan {item_type} baru:")
        items = input_routine_items(item_type)
        
        if items:
            selected[key] = items
            selected['updated_at'] = get_timestamp()
            save_json(file, data)
            print("\n✓ Berhasil diperbarui!")
        else:
            print(f"{item_type.capitalize()} tidak boleh kosong!")
        
    except ValueError:
        print("Input tidak valid!")
    
    pause()

def crud_delete(file, item_type):
    """Generic delete function"""
    clear_screen()
    print("=" * 50)
    print(f"HAPUS {item_type.upper()}")
    print("=" * 50)
    
    data = load_json(file)
    
    if not display_items(data, item_type):
        pause()
        return
    
    try:
        choice = int(input("\nPilih nomor: "))
        if choice < 1 or choice > len(data):
            print("Nomor tidak valid!")
            pause()
            return
        
        selected = data[choice - 1]
        key = 'skin_type' if item_type == "skincare" else 'bmi_category'
        confirm = input(f"\nHapus {item_type} {selected[key]}? (y/n): ").strip().lower()
        
        if confirm == 'y':
            data.pop(choice - 1)
            save_json(file, data)
            print("\n✓ Berhasil dihapus!")
        else:
            print("\nBatal hapus.")
        
    except ValueError:
        print("Input tidak valid!")
    
    pause()

# ===========================
# MENU HANDLERS
# ===========================

def crud_menu(file, item_type):
    """Generic CRUD menu"""
    while True:
        clear_screen()
        print("=" * 50)
        print(f"ADMIN - KELOLA {item_type.upper()}")
        print("=" * 50)
        print("1. Lihat Semua")
        print("2. Tambah Baru")
        print("3. Edit")
        print("4. Hapus")
        print("0. Kembali")
        
        choice = input("\nPilih (0-4): ").strip()
        
        if choice == "1":
            crud_view(file, item_type)
        elif choice == "2":
            crud_add(file, item_type)
        elif choice == "3":
            crud_edit(file, item_type)
        elif choice == "4":
            crud_delete(file, item_type)
        elif choice == "0":
            break

def admin_menu():
    """Admin main menu"""
    while True:
        clear_screen()
        print("=" * 50)
        print("ADMIN DASHBOARD")
        print("=" * 50)
        print("1. Kelola Skincare")
        print("2. Kelola Workout")
        print("0. Logout")
        
        choice = input("\nPilih (0-2): ").strip()
        
        if choice == "1":
            crud_menu(SKINCARE_FILE, "skincare")
        elif choice == "2":
            crud_menu(WORKOUT_FILE, "workout")
        elif choice == "0":
            print("\nLogging out...")
            pause()
            break
