import pandas as pd
from fpdf import FPDF

# Read data from CSV
data = pd.read_csv('cricket_data.csv')

# Basic Analysis
total_rows = len(data)
total_columns = len(data.columns)
columns_list = ', '.join(data.columns)

# Summary Statistics (mean, max, min for numeric columns)
summary = data.describe().round(2)

# Create PDF Report
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", size=14, style="B")
        self.cell(0, 10, "Automated Data Report", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", size=8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

# Generate PDF
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add General Information
pdf.cell(0, 10, f"Total Rows: {total_rows}", ln=True)
pdf.cell(0, 10, f"Total Columns: {total_columns}", ln=True)
pdf.cell(0, 10, f"Columns: {columns_list}", ln=True)
pdf.ln(10)

# Add Summary Statistics
pdf.set_font("Arial", size=12, style="B")
pdf.cell(0, 10, "Summary Statistics:", ln=True)
pdf.set_font("Arial", size=10)

for col in summary.columns:
    pdf.ln(5)
    pdf.cell(0, 10, f"{col} - Mean: {summary[col]['mean']}, Max: {summary[col]['max']}, Min: {summary[col]['min']}", ln=True)

# Save the report
pdf.output("sample_report.pdf")
print("Report generated: sample_report.pdf")
