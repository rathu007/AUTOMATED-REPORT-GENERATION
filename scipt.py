import pandas as pd
from fpdf import FPDF

def generate_report(data_file, output_file):
        df = pd.read_csv(data_file)
        summary = df.describe().to_string()
        
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Times", style='B', size=16)
        pdf.cell(200, 10, "Data Summary Report", ln=True, align="C")
        
        pdf.set_font("Arial", size=12)
        pdf.ln(10)  # Space before the summary
        pdf.multi_cell(0, 10, summary)
        
        pdf.output(output_file)
        print(f"Report saved as {output_file}")

# Example usage
generate_report(r"C:\Users\Rathinavel\OneDrive\文档\o.csv", "report1.pdf")
