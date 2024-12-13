# Ce module contient les instances de vos classes back et front end.
from backend.Draw import Draw
from frontend.pdf import PDF
from utils import load_json, teams_path_json, tirages_path_json

# 1.make draw

json_teams = load_json(path=teams_path_json)

# order teams by pots
dict_pots = Draw.sort_teams_by_pots(json_teams.copy())

# get list of pot
list_pots = Draw.get_list_of_pots(dict_pots.copy())

draw = Draw(pots=list_pots.copy())

draw.make_draw()

# 2. generate pdf after draw

# load samples success results from Draw
json_tirages = load_json(path=tirages_path_json)

pdf = PDF(tirages=json_tirages, json_teams=json_teams)

pdf.generate()

pdf.export()
