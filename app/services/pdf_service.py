import io
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from app.models.requests import BirthDetailsRequest
from app.services.chart_service import ChartService

class PDFService:
    @staticmethod
    def generate_kundli_pdf(req: BirthDetailsRequest) -> bytes:
        chart = ChartService.generate_natal_chart(req)
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
        
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=20, leading=24, textColor=colors.HexColor('#800020'), alignment=1)
        sub_style = ParagraphStyle('SubStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=14, textColor=colors.HexColor('#4A5568'), alignment=1)
        heading_style = ParagraphStyle('HeadStyle', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=13, leading=16, textColor=colors.HexColor('#1A202C'), spaceAfter=8)

        story = []
        
        # Title
        story.append(Paragraph("VEDIC KUNDLI ASTROLOGICAL REPORT", title_style))
        story.append(Paragraph(f"Birth Details: {req.year}-{req.month:02d}-{req.day:02d} {req.hour:02d}:{req.minute:02d} | Lat: {req.latitude}, Lon: {req.longitude}", sub_style))
        story.append(Spacer(1, 15))
        
        # Planetary Table
        story.append(Paragraph("1. Planetary Positions & Nakshatras (Nirayana Lahiri)", heading_style))
        p_table_data = [["Planet", "Sign", "Degrees", "Nakshatra", "Pada", "House", "D9 Sign"]]
        
        # Ascendant row
        asc = chart.ascendant
        p_table_data.append(["Lagna", asc.sign, f"{asc.degree_in_sign:.2f}°", asc.nakshatra, str(asc.pada), "1", asc.d9_sign])
        
        for p_name, p_data in chart.planets.items():
            retro = "(R)" if p_data.is_retrograde else ""
            p_table_data.append([
                f"{p_name} {retro}", p_data.sign, f"{p_data.degree_in_sign:.2f}°",
                p_data.nakshatra, str(p_data.pada), str(p_data.house), p_data.d9_sign
            ])
            
        t = Table(p_table_data, colWidths=[80, 75, 75, 95, 45, 50, 75])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#800020')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F7FAFC')])
        ]))
        story.append(t)
        story.append(Spacer(1, 15))
        
        # Yogas & Doshas
        story.append(Paragraph("2. Active Yogas & Dosha Assessment", heading_style))
        yoga_names = ", ".join([y.name for y in chart.yogas]) if chart.yogas else "Standard Parashara formations"
        mangal_status = "Present" if chart.doshas.mangal_dosha.get("is_present") else "Clear / Cancelled"
        sade_sati_status = chart.doshas.sade_sati.get("phase", "None")
        
        yd_data = [
            ["Active Yogas", yoga_names],
            ["Mangal Dosha", f"{mangal_status} ({chart.doshas.mangal_dosha.get('severity', 'None')})"],
            ["Shani Sade Sati", sade_sati_status],
            ["Kaal Sarp Dosha", chart.doshas.kaal_sarp.get("type", "None")]
        ]
        t_yd = Table(yd_data, colWidths=[150, 345])
        t_yd.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#EDF2F7')),
            ('PADDING', (0, 0), (-1, -1), 5)
        ]))
        story.append(t_yd)
        story.append(Spacer(1, 15))
        
        # Vimshottari Dasha
        story.append(Paragraph("3. Vimshottari Mahadasha Timeline (120 Years)", heading_style))
        d_table_data = [["Dasha Lord", "Start Date", "End Date", "Duration (Years)", "Type"]]
        for d in chart.vimshottari_dasha:
            d_table_data.append([
                d.lord, d.start_date[:10], d.end_date[:10], f"{d.duration_years:.2f}",
                "Birth Balance" if d.is_balance else "Full Cycle"
            ])
        t_d = Table(d_table_data, colWidths=[100, 100, 100, 100, 95])
        t_d.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2D3748')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F7FAFC')])
        ]))
        story.append(t_d)
        
        doc.build(story)
        pdf_val = buffer.getvalue()
        buffer.close()
        return pdf_val
