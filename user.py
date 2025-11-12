"""
User functions untuk GlowUp Gang
Berisi fitur Facial GlowUp dan Body GlowUp dengan PDF output
"""

from helpers import *
from config import *
from pdf_generator import *

def user_facial_glowup():
    """Facial GlowUp - Generate skincare PDF"""
    clear_screen()
    print("=" * 50)
    print("FACIAL GLOWUP - SKINCARE RECOMMENDATION")
    print("=" * 50)
    
    print("\nTipe Kulit:")
    for key, value in SKIN_TYPES.items():
        print(f"{key}. {value}")
    
    skin_type_choice = input("\nPilih tipe kulit (1-5): ").strip()
    
    if skin_type_choice not in SKIN_TYPES:
        print("\n✗ Pilihan tidak valid!")
        pause()
        return
    
    skin_type = SKIN_TYPES[skin_type_choice]
    
    # Load skincare data
    skincare_data = load_json(SKINCARE_FILE)
    
    # Find matching routine
    routine = None
    for skincare in skincare_data:
        if skincare['skin_type'].lower() == skin_type.lower():
            routine = skincare['routine']
            break
    
    if not routine:
        print(f"\n✗ Belum ada routine untuk kulit {skin_type}!")
        print("Hubungi admin untuk menambahkan data.")
        pause()
        return
    
    # Generate PDF
    print(f"\n📄 Membuat PDF untuk kulit {skin_type}...")
    pdf_path = generate_skincare_pdf(skin_type, routine)
    
    if pdf_path:
        print(f"\n✓ PDF berhasil dibuat!")
        print(f"   Lokasi: {pdf_path}")
    else:
        print("\n✗ Gagal membuat PDF!")
    
    pause()

def user_body_glowup():
    """Body GlowUp - Generate workout PDF based on BMI"""
    clear_screen()
    print("=" * 50)
    print("BODY GLOWUP - WORKOUT RECOMMENDATION")
    print("=" * 50)
    
    # Input data
    try:
        weight = float(input("\nBerat badan (kg): "))
        height = float(input("Tinggi badan (cm): "))
        
        if weight <= 0 or height <= 0:
            print("\n✗ Berat dan tinggi harus lebih dari 0!")
            pause()
            return
        
    except ValueError:
        print("\n✗ Input tidak valid! Gunakan angka.")
        pause()
        return
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    bmi_category = get_bmi_category(bmi)
    
    print(f"\nBMI: {bmi}")
    print(f"Kategori: {bmi_category}")
    
    # Load workout data
    workout_data = load_json(WORKOUT_FILE)
    
    # Find matching workout
    workout_plan = None
    for workout in workout_data:
        if workout['bmi_category'].lower() == bmi_category.lower():
            workout_plan = workout['plan']
            break
    
    if not workout_plan:
        print(f"\n✗ Belum ada workout plan untuk {bmi_category}!")
        print("Hubungi admin untuk menambahkan data.")
        pause()
        return
    
    # Generate PDF
    print(f"\n📄 Membuat PDF workout untuk {bmi_category}...")
    pdf_path = generate_workout_pdf(bmi, bmi_category, weight, height, workout_plan)
    
    if pdf_path:
        print(f"\n✓ PDF berhasil dibuat!")
        print(f"   Lokasi: {pdf_path}")
    else:
        print("\n✗ Gagal membuat PDF!")
    
    pause()

def user_menu():
    """User main menu"""
    while True:
        clear_screen()
        print("=" * 50)
        print("GLOWUP GANG - USER MENU")
        print("=" * 50)
        print("1. Facial GlowUp (Skincare)")
        print("2. Body GlowUp (Workout)")
        print("0. Kembali")
        
        choice = input("\nPilih (0-2): ").strip()
        
        if choice == "1":
            user_facial_glowup()
        elif choice == "2":
            user_body_glowup()
        elif choice == "0":
            break
        else:
            print("\n✗ Pilihan tidak valid!")
            pause()
