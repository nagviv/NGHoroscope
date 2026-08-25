from app.models.requests import BirthDetailsRequest
import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph

class PDFService:
    @staticmethod
    def generate_kundli_pdf(req: BirthDetailsRequest) -> bytes:
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        doc.build([Paragraph("VEDIC KUNDLI REPORT", getSampleStyleSheet() if 'getSampleStyleSheet' in globals() else None)])
        val = buffer.getvalue()
        buffer.close()
        return val
