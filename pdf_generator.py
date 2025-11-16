"""
PDF Generator untuk Care.ly
Berisi functions untuk generate PDF skincare dan workout
"""

from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from config import PDF_OUTPUT_DIR, COLOR_SKINCARE, COLOR_WORKOUT
from helpers import ensure_pdf_directory

def generate_skincare_pdf(skin_type, routine_data):
    """Generate PDF for skincare routine with text wrapping"""
    ensure_pdf_directory()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{PDF_OUTPUT_DIR}/Skincare_{skin_type}_{timestamp}.pdf"
    
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor(COLOR_SKINCARE),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    title = Paragraph("<b>CARE.LY FACIAL - SKINCARE ROUTINE</b>", title_style)
    story.append(title)
    
    # Subtitle
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#A23B72'),
        spaceAfter=20,
        alignment=TA_CENTER
    )
    subtitle = Paragraph(f"Tipe Kulit: <b>{skin_type}</b>", subtitle_style)
    story.append(subtitle)
    story.append(Spacer(1, 0.3*inch))
    
    # Cell style untuk wrapping text
    cell_style = ParagraphStyle(
        'CellText',
        parent=styles['Normal'],
        fontSize=10,
        leading=12
    )
    
    # Table data dengan Paragraph untuk wrapping - SIMPLIFIED (No Step)
    data = [['No', 'Produk', 'Brand Rekomendasi']]
    
    for idx, item in enumerate(routine_data, 1):
        data.append([
            Paragraph(str(idx), cell_style),
            Paragraph(item.get('product', '-'), cell_style),
            Paragraph(item.get('brand', '-'), cell_style)
        ])
    
    # Create table - SIMPLIFIED 3 columns
    table = Table(data, colWidths=[0.5*inch, 3.5*inch, 2.5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(COLOR_SKINCARE)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F6F6F6')])
    ]))
    
    story.append(table)
    story.append(Spacer(1, 0.5*inch))
    
    # Footer
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.grey,
        alignment=TA_CENTER
    )
    footer = Paragraph(
        f"Generated on {datetime.now().strftime('%d %B %Y, %H:%M')}<br/>"
        "Care.ly - Stay Beautiful! ✨", 
        footer_style
    )
    story.append(footer)
    
    doc.build(story)
    return filename

def generate_workout_pdf(bmi, bmi_category, weight, height, workout_data):
    """Generate PDF for workout plan with text wrapping"""
    ensure_pdf_directory()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{PDF_OUTPUT_DIR}/Workout_{bmi_category}_{timestamp}.pdf"
    
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor(COLOR_WORKOUT),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    title = Paragraph("<b>CARE.LY BODY - WORKOUT PLAN</b>", title_style)
    story.append(title)
    
    # BMI Info
    info_style = ParagraphStyle(
        'Info',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=10,
        alignment=TA_CENTER
    )
    info = Paragraph(
        f"Berat: <b>{weight} kg</b> | Tinggi: <b>{height} cm</b> | BMI: <b>{bmi}</b>", 
        info_style
    )
    story.append(info)
    
    category_style = ParagraphStyle(
        'Category',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#C73E1D'),
        spaceAfter=20,
        alignment=TA_CENTER
    )
    category = Paragraph(f"Kategori: <b>{bmi_category}</b>", category_style)
    story.append(category)
    story.append(Spacer(1, 0.3*inch))
    
    # Cell style untuk wrapping text
    cell_style = ParagraphStyle(
        'CellText',
        parent=styles['Normal'],
        fontSize=10,
        leading=12
    )
    
    # Table data dengan Paragraph untuk wrapping - SIMPLIFIED (no equipment, no brand)
    data = [['No', 'Exercise & Duration']]
    
    for idx, item in enumerate(workout_data, 1):
        # Combine exercise and duration in one cell
        exercise_text = f"<b>{item['exercise']}</b><br/>{item['duration']}"
        data.append([
            Paragraph(str(idx), cell_style),
            Paragraph(exercise_text, cell_style)
        ])
    
    # Create table - SIMPLIFIED COLUMNS
    table = Table(data, colWidths=[0.5*inch, 6*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(COLOR_WORKOUT)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#FFF4E6')])
    ]))
    
    story.append(table)
    story.append(Spacer(1, 0.5*inch))
    
    # Footer
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.grey,
        alignment=TA_CENTER
    )
    footer = Paragraph(
        f"Generated on {datetime.now().strftime('%d %B %Y, %H:%M')}<br/>"
        "Care.ly - Stay Healthy! 💪", 
        footer_style
    )
    story.append(footer)
    
    doc.build(story)
    return filename
