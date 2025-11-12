"""
Helper functions untuk GlowUp Gang
Berisi utility functions yang digunakan di banyak tempat
"""

import json
import os
from datetime import datetime
import uuid
from config import PDF_OUTPUT_DIR

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_json(filename):
    """Load data from JSON file"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return []

def save_json(filename, data):
    """Save data to JSON file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving {filename}: {e}")
        return False

def get_timestamp():
    """Get current timestamp"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generate_id():
    """Generate unique ID"""
    return str(uuid.uuid4())

def pause():
    """Pause and wait for user input"""
    input("\nTekan Enter untuk melanjutkan...")

def ensure_pdf_directory():
    """Ensure PDF output directory exists"""
    if not os.path.exists(PDF_OUTPUT_DIR):
        os.makedirs(PDF_OUTPUT_DIR)

def calculate_bmi(weight, height):
    """Calculate BMI"""
    height_m = height / 100  # Convert cm to m
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

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
