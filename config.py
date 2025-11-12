"""
Configuration file untuk GlowUp Gang
Berisi constants dan settings
"""

# File Paths
SKINCARE_FILE = "glowup_skincare.json"
WORKOUT_FILE = "glowup_workouts.json"
PDF_OUTPUT_DIR = "glowup_pdfs"

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
