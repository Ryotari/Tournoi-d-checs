class PlayerView:

    def __init__(self, player_controller):
        self.controller = player_controller
        self.last_name = None
        self.first_name = None
        self.birthdate = None
        self.gender = None
        self.ranking = None
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
            option = input(player_search_menu)

        return option

    def update_ranking(self):
        player_database = self.controller.get_all_players()
        if len(player_database) == 0:
            print('Aucun joueur dans la base de données')
        else:
            self.display_all_players()
            id_choice = self.display_chose_player()
            message = 'Entrez le nouveau classement du joueur : '

            new_ranking = input(message)
            while not new_ranking.isdigit() or not int(new_ranking) >= 1:
                print('Classement non valide.\n')
                new_ranking = input(message)
            new_ranking = int(new_ranking)

            player_database.update({'ranking': new_ranking},
                                   doc_ids=[id_choice])

    def display_all_players(self):
        player_database = self.controller.get_all_players()
        for player in player_database:
            print(f"ID : {player['player_id']} - \
                {player['last_name']} {player['first_name']}")

    def display_players_by(self, sort_key='ranking'):
        assert (sort_key in ['ranking', 'last_name'])

        player_database = self.controller.get_all_players()
        PLAYERS_LIST = sorted(player_database, key=lambda d: d[sort_key])
        for player in PLAYERS_LIST:
            print(f"ID : {player['player_id']} - {player['last_name']} {player['first_name']} \
                - Rank : {player['ranking']}")

        return player_database

    def display_player_by_id(self, player_id):
        player_database = self.controller.get_all_players()
        lenght = len(player_database) + 1
        assert(str(player_id).isdigit() and player_id in range(0, lenght))
        player = player_database.get(doc_id=player_id)
        for key in player:
            print(key, ' : ', player[key])

    def display_chose_player(self):
        player_database = self.controller.get_all_players()

        text = "Choisissez l'id d'un joueur : "

        id_choice = input(text)
        while (not id_choice.isdigit()
               or int(id_choice) not in range(1, (len(player_database) + 1))):
            print('id non valide.\n')
            id_choice = input(text)

        id_choice = int(id_choice)

        return id_choice

    def display_chosen_player(self):
        id_choice = self.display_chose_player()
        self.display_player_by_id(id_choice)
        input('Appuyez sur une touche pour revenir au menu.')

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
            if (birth_day.isdigit()
               and len(birth_day) == 2
               and int(birth_day) <= 31):
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
                                    'Entrez un mois de naissance : ')

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
            if ranking.isdigit() and int(ranking) > 0:
                ranking = int(ranking)
                return ranking
            else:
                ranking = input('Classement invalide. '
                                'Entrez le classement du joueur : ')
