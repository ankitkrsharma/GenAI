import os

def write_test_report():
    output_dir = "reports"
    filename = "test_report.txt"
    content = (
        "📊 Test Report\n\n"
        "This is a test report to ensure writing to file works properly.\n"
        "Includes: 📈, 📉, 📋 emojis to check UTF-8 compatibility.\n"
    )

    try:
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        file_path = os.path.join(output_dir, filename)

        # Write content to the file using utf-8 encoding
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ Test report written successfully to: {file_path}")
        return True

    except Exception as e:
        print(f"❌ Failed to write test report: {e}")
        return False


if __name__ == "__main__":
    write_test_report()
