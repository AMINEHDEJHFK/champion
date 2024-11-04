from backend.Draw import Draw
from utils import load_teams_from_json
from frontend.pdf import generate_pdf

if __name__ == "__main__":
    # Charger les équipes depuis le fichier JSON
    pots = load_teams_from_json('data/teams.json')

    # Création du tirage
    draw = Draw(pots)
    draw.conduct_draw()

    # Générer le PDF avec les résultats
    generate_pdf(draw.matches)

    print("Le fichier JSON et le fichier PDF ont été créés.")
