from weasyprint import HTML

def generate_proposal_pdf(analysis_dict):
    html_content = f"""
    <html>
    <head>
        <style>
            @page {{
                size: A4;
                margin: 30px;
            }}

            body {{
                font-family: Arial;
            }}

            h1 {{
                color: #2c3e50;
            }}

            .box {{
                border: 1px solid #ddd;
                padding: 10px;
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>

        <h1>Project Proposal</h1>

        <div class="box">
            <h2>Client Name</h2>
            <p>{analysis_dict.get("client_name", "N/A")}</p>
        </div>

        <div class="box">
            <h2>Budget</h2>
            <p>{analysis_dict.get("budget", "N/A")}</p>
        </div>

        <div class="box">
            <h2>Timeline</h2>
            <p>{analysis_dict.get("timeline", "N/A")}</p>
        </div>

    </body>
    </html>
    """

    pdf_bytes = HTML(string=html_content).write_pdf()
    return pdf_bytes