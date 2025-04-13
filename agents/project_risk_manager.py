# agents/project_risk_manager.py

from agents.market_analysis_agent import MarketAnalysisAgent
from agents.risk_scoring_agent import RiskScoringAgent
from agents.project_tracking_agent import ProjectTrackingAgent
from agents.reporting_agent import ReportingAgent


class ProjectRiskManager:
    def __init__(self):
        self.market_analysis_agent = MarketAnalysisAgent()
        self.risk_scoring_agent = RiskScoringAgent()
        self.project_tracking_agent = ProjectTrackingAgent()
        self.reporting_agent = ReportingAgent()

    def run_risk_analysis(self):
        """Run the complete risk analysis process and generate a report"""
        print("🔍 Starting full project risk analysis...")

        # Get the market analysis insights
        market_analysis = self.market_analysis_agent.analyze_market()
        print("📈 Market analysis complete!")

        # Get the risk score
        risk_score = self.risk_scoring_agent.score_risks()
        print("📉 Risk scoring complete!")

        # Get the project status tracking
        project_status = self.project_tracking_agent.track_project_status()
        print("🛠️ Project tracking complete!")

        # Compile and generate a final risk report
        report_path = self.reporting_agent.compile_report(
            market_analysis=market_analysis,
            risk_score=risk_score,
            project_status=project_status
        )

        print(f"✔️ Risk analysis completed. Report generated at: {report_path}")
        return report_path


# Example usage
if __name__ == "__main__":
    manager = ProjectRiskManager()
    manager.run_risk_analysis()
