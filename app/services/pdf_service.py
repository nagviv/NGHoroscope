import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from app.models.requests import BirthDetailsRequest

class PDFService:
    @staticmethod
    def generate_kundli_pdf(req: BirthDetailsRequest) -> bytes:
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        doc.build([Paragraph("VEDIC KUNDLI ASTROLOGICAL REPORT", styles['Heading1'])])
        pdf_val = buffer.getvalue()
        buffer.close()
        return pdf_val
