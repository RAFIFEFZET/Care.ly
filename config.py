"""
Configuration file untuk Care.ly
Berisi constants dan settings
"""
import os

# Get base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# File Paths - Using absolute paths
SKINCARE_FILE = os.path.join(BASE_DIR, "data", "skincare.json")
WORKOUT_FILE = os.path.join(BASE_DIR, "data", "workouts.json")
PDF_OUTPUT_DIR = os.path.join(BASE_DIR, "output_pdfs")

# Admin Credentials (Hardcoded)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Skin Type Options
SKIN_TYPES = {
    "1": "Oily",
    "2": "Dry",
    "3": "Combination",
    "4": "Sensitive",
    "5": "Normal"
}

# BMI Categories
BMI_CATEGORIES = {
    "1": {"name": "Underweight", "range": "< 18.5"},
    "2": {"name": "Normal", "range": "18.5 - 24.9"},
    "3": {"name": "Overweight", "range": "25 - 29.9"},
    "4": {"name": "Obese", "range": ">= 30"}
}

# PDF Colors
COLOR_SKINCARE = '#2E86AB'  # Blue
COLOR_WORKOUT = '#F18F01'   # Orange
