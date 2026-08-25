import io
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
        title_style = ParagraphStyle('TitleStyle', fontName='Helvetica-Bold', fontSize=20, leading=24, textColor=colors.HexColor('#800020'), alignment=1)
        sub_style = ParagraphStyle('SubStyle', fontName='Helvetica', fontSize=10, leading=14, textColor=colors.HexColor('#4A5568'), alignment=1)
        heading_style = ParagraphStyle('HeadStyle', fontName='Helvetica-Bold', fontSize=13, leading=16, textColor=colors.HexColor('#1A202C'), spaceAfter=8)

        story = [Paragraph("VEDIC KUNDLI ASTROLOGICAL REPORT", title_style), Paragraph(f"Birth Details: {req.year}-{req.month:02d}-{req.day:02d} {req.hour:02d}:{req.minute:02d}", sub_style), Spacer(1, 15)]
        story.append(Paragraph("1. Planetary Positions (Nirayana Lahiri)", heading_style))
        p_table_data = [["Planet", "Sign", "Degrees", "Nakshatra", "House", "D9 Sign"]]
        asc = chart.ascendant
        p_table_data.append(["Lagna", asc.sign, f"{asc.degree_in_sign:.2f}°", asc.nakshatra, "1", asc.d9_sign])
        for p_name, p_data in chart.planets.items():
            p_table_data.append([f"{p_name}", p_data.sign, f"{p_data.degree_in_sign:.2f}°", p_data.nakshatra, str(p_data.house), p_data.d9_sign])
        t = Table(p_table_data, colWidths=[90, 85, 85, 105, 55, 75])
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#800020')), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0'))]))
        story.append(t)
        doc.build(story)
        pdf_val = buffer.getvalue()
        buffer.close()
        return pdf_val
