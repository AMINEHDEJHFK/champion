import random
import json
from typing import List
from backend.Team import Team, Pot

class Draw:
    def __init__(self, pots: List[Pot]):
        self.pots = pots
        self.matches = {}

    def conduct_draw(self):
        for pot in self.pots:
            for team in pot.teams:
                home_opponents = []
                away_opponents = []
                chosen_pots_home = set()
                chosen_pots_away = set()

                for other_pot in self.pots:
                    if other_pot.pot_number != pot.pot_number:
                        available_opponents = [
                            opponent for opponent in other_pot.teams if opponent.pays != team.pays
                        ]
                        random.shuffle(available_opponents)

                        # Ensure unique pot for each opponent
                        if len(chosen_pots_home) < 4:
                            for opponent in available_opponents:
                                if other_pot.pot_number not in chosen_pots_home:
                                    home_opponents.append(opponent)
                                    chosen_pots_home.add(other_pot.pot_number)
                                    break

                        if len(chosen_pots_away) < 4:
                            for opponent in available_opponents:
                                if other_pot.pot_number not in chosen_pots_away:
                                    away_opponents.append(opponent)
                                    chosen_pots_away.add(other_pot.pot_number)
                                    break

                self.matches[team.nom] = {
                    'pot': pot.pot_number,
                    'home': [{'nom': opponent.nom, 'pays': opponent.pays, 'pot': self.get_pot_number(opponent)} for opponent in home_opponents],
                    'away': [{'nom': opponent.nom, 'pays': opponent.pays, 'pot': self.get_pot_number(opponent)} for opponent in away_opponents]
                }

    def get_pot_number(self, team: Team) -> int:
        for pot in self.pots:
            if team in pot.teams:
                return pot.pot_number
        return -1

    def to_json(self) -> str:
        return json.dumps(self.matches, ensure_ascii=False, indent=4)

    def save_to_file(self, filename: str):
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.matches, json_file, ensure_ascii=False, indent=4)
