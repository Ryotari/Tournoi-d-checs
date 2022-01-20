

class PlayerDisplay:

    def __call__(self):
        """player_db = player_model.player_db"""

        for player in player_list:
            print(f"{player['Nom']} {player['Prénom']} {player['Classement']}")


class PlayerView:

    def __init__(self, player_controller):
        self.controller = player_controller
        self.last_name = None
        self.first_name = None
        self.birthdate = None
        self.gender = None
        self.ranking = None
        self.score = 0
        self.player_id = None


    def display_player_menu(self):
        player_menu = """
                Veuillez choisir une option :\n
                1 Créer un joueur\n
                2 Modifier un joueur existant\n
                0 Retour au menu\n"""
        option = input(player_menu)

        while option not in ['0', '1', '2']:
            option = input(player_menu)

        return option


    def display_player_search_menu(self):
        player_search_menu = """
                1 : Chercher par ordre alphabétique\n
                2 : Chercher par classement\n
                0 : Retour au menu\n"""

        option = input(player_search_menu)

        while option not in ['0', '1', '2']:
            option = input(player_menu)

        return option


    def display_all_players(self):
        PLAYERS_LIST = self.controller.get_all_players()
        for player in PLAYERS_LIST:
            print(f"{player['player_id']} - {player['last_name']} {player['first_name']}")

    def display_players_by_name(self):
        PLAYERS_LIST = self.controller.get_all_players()
        PLAYERS_LIST_BY_NAME = sorted(PLAYERS_LIST, key=lambda d: d['last_name'])
        for player in PLAYERS_LIST_BY_NAME:
            print(f"ID : {player['player_id']} - {player['last_name']} {player['first_name']} - Rank : {player['ranking']}")


    def display_players_by_rank(self):
        PLAYERS_LIST = self.controller.get_all_players()
        PLAYERS_LIST_BY_RANK = sorted(PLAYERS_LIST, key=lambda d: d['ranking'])
        for player in PLAYERS_LIST_BY_RANK:
            print(f"ID : {player['player_id']} - {player['last_name']} {player['first_name']} - Rank : {player['ranking']}")


    """
    def display_chosen_player(self):
        PLAYERS_LIST = self.controller.get_all_players()
        valid_id = False
        while not valid_id:
            id_choice = input('Entrez l\'id du joueur que vous recherchez : ')
            try:
                int(id_choice)
            except Exception:
                print('Vous devez entrer l\'id du joueur')
            else:
                valid_id = True
            id_choice = int(id_choice)
        if id_choice <= 0 or id_choice > len(PLAYERS_LIST):
            print('id de joueur non reconnu')
            self.display_chosen_player()
        player = next(item for item in PLAYERS_LIST if item['player_id'] == id_choice)
        print(player)
        """


    def display_create_player(self):
        self.last_name = self.add_last_name()
        self.first_name = self.add_first_name()
        self.birthdate = self.add_birthdate()
        self.gender = self.add_gender()
        self.ranking = self.add_ranking()
        self.player_id = self.controller.return_player_id()
        player_data = {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birthdate': self.birthdate,
            'gender': self.gender,
            'ranking': self.ranking,
            'score': self.score,
            'player_id': self.player_id
        }

        return player_data
        

    def add_last_name(self):
        last_name = input('Nom de famille : ')
        while last_name == '':
            last_name = input('Entrez un nom de famille : ')
        return last_name

    def add_first_name(self):
        first_name = input('Prénom : ')
        while first_name == '':
            first_name = input('Entrez un prénom : ')
        return first_name

    def add_birthdate(self):
        birth_day = input('Entrez un jour de naissance : ')
        while(True):
            if birth_day.isdigit() \
            and len(birth_day) == 2 \
            and int(birth_day) <= 31:
                break
            else:
                birth_day = input('Jour invalide. '
                                  'Entrez un jour de naissance : ')

        birth_month = input('Entrez un mois de naissance : ')
        while(True):
            if birth_month.isdigit() \
            and len(birth_month) == 2 \
            and int(birth_month) <= 12:
                break
            else:
                birth_month = input('Mois invalide. '
                                    'Entrez un mois de naissance en chiffres : ')

        birth_year = input('Entrez une année de naissance : ')
        while(True):
            if birth_year.isdigit() \
            and len(birth_year) == 4 \
            and int(birth_year) <= 2020:
                break
            else:
                birth_year = input('Année invlide. '
                                   'Entrez une année de naissance : ')

        return f'{birth_day}/{birth_month}/{birth_year}'

    def add_gender(self):
        gender = input('Choisissez le sexe du joueur (H ou F) : ')
        while(True):
            if gender == 'H' or gender == 'h':
                return 'Homme'
            elif gender == 'F' or gender == 'f':
                return 'Femme'
            else:
                gender = input('Sexe invalide. '
                               'Choisissez le sexe du joueur (H ou F) : ')

    def add_ranking(self):
        ranking = input('Entrez le classement du joueur : ')
        while(True):
            if ranking.isdigit() and int(ranking) >= 0:
                return ranking
            else:
                ranking = input('Classement invalide. '
                                'Entrez le classement du joueur : ')
