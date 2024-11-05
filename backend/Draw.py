import random
import json
from typing import List
from backend.models.Team import Team, Pot

class Draw:
    def __init__(self, pots: List[Pot]):
        self.pots = pots
        self.matches = {}

    def conduct_draw(self):
        for pot in self.pots:
            for team in pot.teams:
                home_opponents = self._draw_opponents(team, avoid_team=team, is_home=True)
                away_opponents = self._draw_opponents(team, avoid_team=team, is_home=False)

                self.matches[team.nom] = {
                    'pot': pot.pot_number,
                    'home': [{'nom': opp.nom, 'pays': opp.pays, 'pot': self.get_pot_number(opp)} for opp in home_opponents],
                    'away': [{'nom': opp.nom, 'pays': opp.pays, 'pot': self.get_pot_number(opp)} for opp in away_opponents]
                }

    def _draw_opponents(self, team, avoid_team, is_home):
    chosen_opponents = []
    chosen_pots = set()

    while len(chosen_opponents) < 4:
        for other_pot in self.pots:
            if other_pot.pot_number == self.get_pot_number(avoid_team) or other_pot.pot_number in chosen_pots:
                continue

            available_opponents = [
                opp for opp in other_pot.teams
                if opp.pays != team.pays and opp not in chosen_opponents
            ]
            random.shuffle(available_opponents)

            if available_opponents:
                chosen_opponents.append(available_opponents.pop())
                chosen_pots.add(other_pot.pot_number)
            else:
                # Si aucun adversaire n'est disponible, tenter une autre configuration
                chosen_opponents.clear()
                chosen_pots.clear()
                break

        return chosen_opponents

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
