import random

# Define the pots
pot_1 = {'Chelsea FC': 'ENG', 'FC København': 'DEN', 'KAA Gent': 'BEL', 'ACF Fiorentina': 'ITA',
         'Linzer ASK': 'AUT', 'Real Betis Balompié': 'ESP'}

pot_2 = {'İstanbul Başakşehir FK': 'TUR', 'Molde FK': 'NOR', 'LEGIA WARSZAWA': 'POL', '1.FC Heidenheim': 'GRE',
         'Djurgårdens IF': 'SWE', 'APOEL': 'CYP'}

pot_3 = {'SK Rapid Wiedeń': 'AUT', 'AS Omónia Lefkossías': 'CYP', 'HJK': 'FIN', 'Vitória SC Guimarães': 'POR',
         'FK Astana': 'KAZ', 'NK Olimpija': 'SVN'}

pot_4 = {'Cercle Brugge KSV': 'BEL', 'Shamrock Rovers FC': 'IRL', 'The New Saints FC': 'WAL', 'FC Lugano': 'SUI',
         'Heart of Midlothian FC': 'SCO', 'FK Mladá Boleslav': 'CZE'}

pot_5 = {'Petrocub Hîncești': 'MDA', 'FC Sankt Gallen': 'SUI', 'Panathinaïkós AO': 'GRE', 'FK TSC':'SRB',
         'FK Borac': 'BIH', 'JAGIELLONIA BIAŁYSTOK': 'POL'}

pot_6 = {'NK Celje': 'SVN', 'Larne FC': 'NIR', 'Dinamo Mińsk': 'BLR', 'Páfos FC':'CYP', 'Víkingur Reykjavík': 'ISL',
         'Noa Erewan':'ARM'}

# Combine all teams into one dictionary
all_teams = {**pot_1, **pot_2, **pot_3, **pot_4, **pot_5, **pot_6}


def draw_simplified():
    matches = {team: [] for team in all_teams}
    pots = [pot_1, pot_2, pot_3, pot_4, pot_5, pot_6]  # Include all 6 pots
    num_opponents = 8  # Adjust this value based on the number of opponents you want

    for team in all_teams:
        while len(matches[team]) < num_opponents:
            possible_opponents = []
            for pot in pots:
                if team in pot:
                    continue
                possible_opponents += [
                    opponent for opponent in pot
                    if all_teams[opponent] != all_teams[team] and len(matches[opponent]) < num_opponents
                       and opponent not in matches[team]  # Ensure no duplicate opponents
                ]

            if not possible_opponents:
                return draw_simplified()

            opponent = random.choice(possible_opponents)
            matches[team].append(opponent)
            matches[opponent].append(team)

    return matches


def print_matches(matches):
    for team, opponents in matches.items():
        print(f"{team} zagra przeciwko: {', '.join(opponents)}\n")

