#main.py

import logging
from agents.project_risk_manager import ProjectRiskManager
from crew.crew_setup import ProjectRiskManagementCrew
from utils.logger import setup_logger
logger = setup_logger(enable_logging=False)


def main():
    logger.info("Project Risk Management System started.")

    try:
        # Initialize the ProjectRiskManager and run the risk analysis
        risk_manager = ProjectRiskManager()
        logger.info("Starting risk analysis process...")

        # Run the risk analysis and get the generated report
        report_path = risk_manager.run_risk_analysis()
        logger.info(f"Risk analysis complete. Report generated at {report_path}")

        # Optionally: Run the CrewAI tasks (async/parallel tasks)
        # crew = ProjectRiskManagementCrew()
        # crew.run_async_agents()  # Uncomment if asynchronous execution is desired

    except Exception as e:
        logger.error(f"Error occurred during project risk management process: {e}")

    finally:
        logger.info("Project Risk Management System finished.")


if __name__ == "__main__":
    main()
