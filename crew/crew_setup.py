# crew/crew_setup.py
from crewai import Crew
from agents.project_risk_manager import ProjectRiskManager
from agents.market_analysis_agent import MarketAnalysisAgent
from agents.risk_scoring_agent import RiskScoringAgent
from agents.project_tracking_agent import ProjectTrackingAgent
from agents.reporting_agent import ReportingAgent
import asyncio


class ProjectRiskManagementCrew:
    def __init__(self):
        # Initialize CrewAI with specific agents
        self.crew = Crew()

        # Create agent instances
        self.project_risk_manager = ProjectRiskManager()
        self.market_analysis_agent = MarketAnalysisAgent()
        self.risk_scoring_agent = RiskScoringAgent()
        self.project_tracking_agent = ProjectTrackingAgent()
        self.reporting_agent = ReportingAgent()

    async def run_async_agents(self):
        """Asynchronously run agents for full risk analysis"""
        print("🌐 Running agents asynchronously...")

        # Execute tasks asynchronously using CrewAI
        market_analysis_task = asyncio.create_task(self.market_analysis_agent.analyze_market())
        risk_score_task = asyncio.create_task(self.risk_scoring_agent.score_risks())
        project_status_task = asyncio.create_task(self.project_tracking_agent.track_project_status())

        # Await the results
        market_analysis = await market_analysis_task
        risk_score = await risk_score_task
        project_status = await project_status_task

        # Generate final report
        print("⚙️ Compiling final report...")
        report_path = self.reporting_agent.compile_report(market_analysis, risk_score, project_status)
        print(f'✅ Report path: {report_path}')
        print(f"✔️ Full risk analysis completed. Report saved at {report_path}")
        return report_path


    def run(self):
        """Run the risk management tasks sequentially"""
        print("🛠️ Running risk management tasks...")

        # If you want to run it sequentially instead of async
        self.project_risk_manager.run_risk_analysis()


# Example usage
if __name__ == "__main__":
    # Initialize Crew
    crew_setup = ProjectRiskManagementCrew()

    # For asynchronous execution
    asyncio.run(crew_setup.run_async_agents())

    # For sequential execution (use one or the other)
    # crew_setup.run()
