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

        story = [Paragraph("VEDIC ASHTAKOOTA COMPATIBILITY REPORT", title_style), Paragraph(f"Total Score: {res.ashtakoota['total_score']} / 36.0 ({res.overall_compatibility})", sub_style), Spacer(1, 15)]
        table_data = [["Koota", "Max Points", "Obtained Points"]]
        for k_name, k_info in res.ashtakoota["breakdown"].items():
            table_data.append([k_name, str(k_info["max"]), str(k_info["obtained"])])
        t = Table(table_data, colWidths=[180, 150, 150])
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#800020')), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0'))]))
        story.append(t)
        doc.build(story)
        pdf_val = buffer.getvalue()
        buffer.close()
        return pdf_val
