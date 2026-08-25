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
        story = [Paragraph("VEDIC KUNDLI ASTROLOGICAL REPORT", title_style), Paragraph(f"Birth Details: {req.year}-{req.month:02d}-{req.day:02d}", sub_style), Spacer(1, 15)]
        doc.build(story)
        pdf_val = buffer.getvalue()
        buffer.close()
        return pdf_val
