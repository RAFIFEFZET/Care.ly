"""
Care.ly v2.1 - Healthcare & Fitness Recommendation System
Aplikasi CLI untuk rekomendasi skincare dan workout dengan output PDF

Modules:
- config.py: Konstanta dan konfigurasi
- helpers.py: Fungsi utilitas
- pdf_generator.py: Generate PDF dengan text wrapping
- admin.py: Admin CRUD operations
- user.py: User features (Facial & Body Care)
- main.py: Entry point aplikasi

"""

from helpers import clear_screen, pause
from admin import admin_login, admin_menu
from user import user_menu

def main_menu():
    """Main menu aplikasi"""
    while True:
        clear_screen()
        print("=" * 50)
        print("SELAMAT DATANG DI CARE.LY")
        print("=" * 50)
        print("1. User - Care Services")
        print("2. Admin - Manage Data")
        print("0. Exit")
        
        choice = input("\nPilih menu (0-2): ").strip()
        
        if choice == "1":
            user_menu()
        elif choice == "2":
            if admin_login():
                admin_menu()
        elif choice == "0":
            clear_screen()
            print("=" * 50)
            print("Terima kasih telah menggunakan Care.ly!")
            print("Stay healthy, stay beautiful! ✨")
            print("=" * 50)
            break
        else:
            print("\n✗ Pilihan tidak valid!")
            pause()

if __name__ == "__main__":
    main_menu()
