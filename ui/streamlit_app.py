import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from agents.project_risk_manager import ProjectRiskManager

# Path to the directory where reports are stored
REPORTS_DIR = "reports"


# Function to display the risk report
def display_risk_report():
    st.title("Project Risk Report Viewer")

    # Create a horizontal navigation bar (radio button style)
    section = st.radio("Choose Section", ["Generate New Report", "View Previous Report"])

    if section == "Generate New Report":
        # Section to generate a new report
        st.write("### Generate New Risk Report")
        if st.button("Generate Risk Report"):
            report_manager = ProjectRiskManager()
            report_path = report_manager.run_risk_analysis()
            st.write(f"📄 Report generated: {os.path.basename(report_path)}")

            # Open the report file with utf-8 encoding
            with open(report_path, "r", encoding="utf-8") as report_file:
                report_content = report_file.read()

                # Optionally, replace '*' with a more readable character, like '-'
                report_content = report_content.replace('*', '-')

                # Display the report with markdown rendering
                st.markdown(report_content)

            # Add a download button to allow the user to download the new report
            with open(report_path, "rb") as report_file:
                st.download_button(
                    label="Download Risk Report",
                    data=report_file,
                    file_name=os.path.basename(report_path),
                    mime="text/plain"
                )

    elif section == "View Previous Report":
        # Section to view previous reports
        st.write("### View Previous Risk Reports")

        # Check if the reports directory exists
        if os.path.exists(REPORTS_DIR):
            # List available reports in the reports directory
            report_files = [f for f in os.listdir(REPORTS_DIR) if f.endswith(".txt")]

            if report_files:
                selected_report = st.selectbox("Select a report", report_files)

                if selected_report:
                    # Display the selected report content
                    st.write(f"📄 Showing report: {selected_report}")
                    report_path = os.path.join(REPORTS_DIR, selected_report)

                    try:
                        with open(report_path, "r", encoding="utf-8") as report_file:
                            report_content = report_file.read()

                            # Optionally, replace '*' with a more readable character, like '-'
                            report_content = report_content.replace('*', '-')

                            # Display the report with markdown rendering
                            st.markdown(report_content)

                        # Add a download button to allow the user to download the selected report
                        with open(report_path, "rb") as report_file:
                            st.download_button(
                                label="Download Report",
                                data=report_file,
                                file_name=selected_report,
                                mime="text/plain"
                            )

                    except Exception as e:
                        st.error(f"Error reading the report: {e}")
            else:
                st.write("No previous reports found.")
        else:
            st.write("The reports directory does not exist.")


# Main function to display the report generation and viewing functionality
def main():
    display_risk_report()


if __name__ == "__main__":
    main()
