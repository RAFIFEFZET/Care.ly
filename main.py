"""
Modules:
- config.py: Konstanta dan konfigurasi
- helpers.py: Fungsi utilitas
- pdf_generator.py: Generate PDF dengan text wrapping
- admin.py: Admin CRUD operations
- user.py: User features (Facial & Body GlowUp)
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
        print("SELAMAT DATANG DI GLOWUP GANG")
        print("=" * 50)
        print("1. User - GlowUp Services")
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
            print("Terima kasih telah menggunakan GlowUp Gang!")
            print("Stay healthy, stay glowing! ✨")
            print("=" * 50)
            break
        else:
            print("\n✗ Pilihan tidak valid!")
            pause()

if __name__ == "__main__":
    main_menu()
