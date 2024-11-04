from fpdf import FPDF

def generate_pdf(matches):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Résultats du Tirage", ln=True, align='C')
    
    for team, details in matches.items():
        pdf.cell(200, 10, txt=f"Équipe: {team} (Pot {details['pot']})", ln=True)
        pdf.cell(200, 10, txt="  À domicile:", ln=True)
        for opponent in details['home']:
            pdf.cell(200, 10, txt=f"    - {opponent['nom']} ({opponent['pays']}, Pot {opponent['pot']})", ln=True)
        pdf.cell(200, 10, txt="  À l'extérieur:", ln=True)
        for opponent in details['away']:
            pdf.cell(200, 10, txt=f"    - {opponent['nom']} ({opponent['pays']}, Pot {opponent['pot']})", ln=True)
    
    pdf.output("draw_results.pdf")
