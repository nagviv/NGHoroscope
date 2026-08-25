import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from app.models.requests import MatchMakingRequest
from app.services.match_service import MatchService

class MatchPDFService:
    @staticmethod
    def generate_compatibility_pdf(req: MatchMakingRequest) -> bytes:
        res = MatchService.calculate_compatibility(req)
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle('TitleStyle', fontName='Helvetica-Bold', fontSize=20, leading=24, textColor=colors.HexColor('#800020'), alignment=1)
        sub_style = ParagraphStyle('SubStyle', fontName='Helvetica', fontSize=10, leading=14, textColor=colors.HexColor('#4A5568'), alignment=1)
        story = [Paragraph("VEDIC ASHTAKOOTA COMPATIBILITY REPORT", title_style), Paragraph(f"Total Score: {res.ashtakoota['total_score']} / 36.0", sub_style), Spacer(1, 15)]
        doc.build(story)
        pdf_val = buffer.getvalue()
        buffer.close()
        return pdf_val
