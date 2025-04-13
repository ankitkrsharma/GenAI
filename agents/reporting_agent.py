# agents/reporting_agent.py

from config.settings import settings
from datetime import datetime

import os


class ReportingAgent:
    def __init__(self, output_dir="reports", filename='final_report.txt'):
        self.output_dir = output_dir
        self.filename = filename

        # Ensure the reports directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def compile_report(self, market_analysis: str, risk_score: str, project_status: str, timestamped_filename=None):
        # print("Market Analysis:", market_analysis)
        # print("Risk Score:", risk_score)
        # print("Project Status:", project_status)

        """Creates a full risk report from multiple agent outputs"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        report_content = f"""
        AI-Powered Project Risk Report
        Generated on: {timestamp}
        =========================================

        📈 Market Risk Analysis:
        {market_analysis.strip()}

        📉 Internal Risk Score:
        {risk_score.strip()}

        🛠️ Project Status Summary:
        {project_status.strip()}

        =========================================
        Summary:
        - This report integrates external market trends, internal project metrics, and operational risks.
        - Use the insights above to inform executive decisions and mitigation planning.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_filename, ext = os.path.splitext(self.filename)
        timestamped_filename = f"{base_filename}_{timestamp}{ext}"
        try:
            # Ensure the reports directory exists
            os.makedirs(self.output_dir, exist_ok=True)
            report_path = os.path.join(self.output_dir, timestamped_filename)

            # Write the report to file
            with open(report_path, "w", encoding="utf-8") as f:
                f.write(report_content)

            print(f"📄 Risk report saved at: {report_path}")
            return report_path

        except Exception as e:
            print(f"❌ Failed to write report: {e}")
            return None
