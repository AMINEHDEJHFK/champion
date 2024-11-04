import json
from typing import List
from backend.Team import Team, Pot

def load_teams_from_json(file_path: str) -> List[Pot]:
    with open(file_path, 'r', encoding='utf-8') as file:
        teams_data = json.load(file)

    pots = {1: [], 2: [], 3: [], 4: []}
    for team in teams_data:
        pots[team['chapeau']].append(Team(team['nom'], team['pays']))

    return [Pot(pot_number, teams) for pot_number, teams in pots.items()]
