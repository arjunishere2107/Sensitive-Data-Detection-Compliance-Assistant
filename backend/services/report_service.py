import os

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.platypus import SimpleDocTemplate, Paragraph


class ReportService:

    REPORT_FOLDER = "reports"

    @classmethod
    def generate_report(
        cls,
        document_id,
        filename,
        detection,
        summary
    ):

        os.makedirs(cls.REPORT_FOLDER, exist_ok=True)

        report_path = os.path.join(
            cls.REPORT_FOLDER,
            f"{document_id}.pdf"
        )

        doc = SimpleDocTemplate(report_path)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "<b>Sensitive Data Compliance Report</b>",
                styles["Heading1"]
            )
        )

        story.append(
            Paragraph(f"<b>Filename:</b> {filename}", styles["BodyText"])
        )

        story.append(
            Paragraph(
                f"<b>Overall Risk:</b> {detection['summary']['overall_risk']}",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Risk Score:</b> {detection['summary']['risk_score']}",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph("<br/><b>AI Compliance Summary</b>", styles["Heading2"])
        )

        story.append(
            Paragraph(summary.replace("\n", "<br/>"), styles["BodyText"])
        )

        doc.build(story)

        return report_path