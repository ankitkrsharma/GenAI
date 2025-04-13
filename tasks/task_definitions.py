# tasks/task_definitions.py

from crewai import Task

from agents.market_analysis_agent import MarketAnalysisAgent
from agents.risk_scoring_agent import RiskScoringAgent
from agents.project_tracking_agent import ProjectTrackingAgent
from agents.reporting_agent import ReportingAgent

# Define Market Analysis Task
class MarketAnalysisTask(Task):
    def __init__(self):
        super().__init__("market_analysis_task")
        self.agent = MarketAnalysisAgent()

    def run(self):
        print("🔍 Running market analysis task...")
        market_analysis = self.agent.analyze_market()
        return market_analysis

# Define Risk Scoring Task
class RiskScoringTask(Task):
    def __init__(self):
        super().__init__("risk_scoring_task")
        self.agent = RiskScoringAgent()

    def run(self):
        print("📉 Running risk scoring task...")
        risk_score = self.agent.score_risks()
        return risk_score

# Define Project Status Tracking Task
class ProjectStatusTrackingTask(Task):
    def __init__(self):
        super().__init__("project_status_tracking_task")
        self.agent = ProjectTrackingAgent()

    def run(self):
        print("🛠️ Running project status tracking task...")
        project_status = self.agent.track_project_status()
        return project_status

# Define Reporting Task
class ReportingTask(Task):
    def __init__(self):
        super().__init__("reporting_task")
        self.agent = ReportingAgent()

    def run(self, market_analysis, risk_score, project_status):
        print("📄 Generating report...")
        report_path = self.agent.compile_report(market_analysis, risk_score, project_status)
        return report_path
