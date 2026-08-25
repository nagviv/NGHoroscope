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
        heading_style = ParagraphStyle('HeadStyle', fontName='Helvetica-Bold', fontSize=13, leading=16, textColor=colors.HexColor('#1A202C'), spaceAfter=8)

        story = []
        story.append(Paragraph("VEDIC ASHTAKOOTA COMPATIBILITY REPORT", title_style))
        story.append(Paragraph(f"Bride Birth: {req.bride.year}-{req.bride.month:02d}-{req.bride.day:02d} | Groom Birth: {req.groom.year}-{req.groom.month:02d}-{req.groom.day:02d}", sub_style))
        story.append(Spacer(1, 15))

        # 36-point Score Summary
        score = res.ashtakoota["total_score"]
        score_verdict = f"TOTAL SCORE: {score} / 36.0 ({res.overall_compatibility})"
        story.append(Paragraph(score_verdict, heading_style))

        # Ashtakoota Breakdown Table
        table_data = [["Koota", "Signification", "Max Points", "Obtained Points"]]
        koota_meanings = {
            "Varna": "Spiritual compatibility / Ego alignment",
            "Vashya": "Mutual attraction / Dominance balance",
            "Tara": "Health, prosperity & destiny alignment",
            "Yoni": "Physical / Biological compatibility",
            "Graha_Maitri": "Mental harmony & friendship",
            "Gana": "Temperament & psychological nature",
            "Bhakoot": "Family welfare, financial growth & happiness",
            "Nadi": "Genetic, physiological & lineage vitality"
        }

        for k_name, k_info in res.ashtakoota["breakdown"].items():
            meaning = koota_meanings.get(k_name, "Vedic factor")
            table_data.append([k_name, meaning, str(k_info["max"]), str(k_info["obtained"])])

        t = Table(table_data, colWidths=[100, 220, 80, 90])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#800020')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F7FAFC')])
        ]))
        story.append(t)
        story.append(Spacer(1, 15))

        # Manglik Dosha Analysis
        story.append(Paragraph("2. Manglik (Kuja) Dosha Comparison", heading_style))
        b_mangal = "Present" if res.bride_mangal_dosha.get("is_present") else "Clear / Cancelled"
        g_mangal = "Present" if res.groom_mangal_dosha.get("is_present") else "Clear / Cancelled"
        
        m_data = [
            ["Partner", "Mangal Dosha Status", "Severity"],
            ["Bride", b_mangal, res.bride_mangal_dosha.get("severity", "None")],
            ["Groom", g_mangal, res.groom_mangal_dosha.get("severity", "None")]
        ]
        t_m = Table(m_data, colWidths=[120, 200, 170])
        t_m.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2D3748')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0'))
        ]))
        story.append(t_m)

        doc.build(story)
        pdf_val = buffer.getvalue()
        buffer.close()
        return pdf_val
