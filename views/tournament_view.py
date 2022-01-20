

class TournamentMenus:
    """Display the tournament menus"""
    tournament_menu = """
                    Veuillez choisir une option :\n
                    1 : Afficher tous les tournois\n
                    2 : Choisir un tournoi\n
                    0 : Retour au menu\n"""

    chosen_tournament_menu = """
                            Veuillez choisir une option :\n
                            1 : Afficher les joueurs par ordre alphabétique\n
                            2 : Afficher les joueurs par classement\n
                            3 : Afficher les tours\n
                            4 : Afficher les matchs\n
                            0 : Retour au menu\n"""


class TournamentView:
    """Display the inputs to create a tournament"""
    def __init__(self, tournament_controller):
        self.controller = tournament_controller
        self.tournament_name = None
        self.location = None
        self.date = None
        self.number_of_tours = 4
        self.time_control = None
        self.description = None
        self.tournament_id = None
        self.players_ids = []
        self.players_entry = []

    def display_create_tournament(self):
        self.tournament_name = self.add_tournament_name()
        self.location = self.add_location()
        self.date = self.add_tournament_date()
        self.number_of_rounds = self.add_number_of_tours()
        self.time_control = self.add_time_control()
        self.description = self.add_description()
        self.tournament_id = self.controller.return_tournament_id()
        self.players_entry = self.add_players_to_tournament()
        tournament_data = {
            'tournament_name': self.tournament_name,
            'location': self.location,
            'date': self.date,
            'number_of_tours': self.number_of_tours,
            'time_control': self.time_control,
            'description': self.description,
            'tournament_id': self.tournament_id,
            'players_entry': self.players_entry
        }

        return tournament_data


    def display_all_tournaments(self):
        TOURNAMENTS_LIST = self.controller.return_tournaments_list()
        for tournament in TOURNAMENTS_LIST:
            print(f"{tournament['tournament_id']} - {tournament['tournament_name']} - {tournament['location']}")

    def add_tournament_name(self):
        tournament_name = input('Nom du tournoi : ')
        while tournament_name == '':
            tournament_name = input('Nom invalide. '
                                    'Entrez le nom du tournoi : ')
        return tournament_name


    def add_location(self):
        location = input('Lieu du tournoi : ')
        while location == '':
            location = input('Lieu invalide. '
                                        'Entrez le lieu du tournoi : ')
        return location


    def add_tournament_date(self):
        tournament_day = input('Entrez le jour du tournoi : ')
        while(True):
            if tournament_day.isdigit() \
            and len(tournament_day) == 2 \
            and int(tournament_day) <= 31:
                break
            else:
                tournament_day = input('Jour invalide. '
                                       'Entrez le jour du tournoi : ')

        tournament_month = input('Entrez le mois du tournoi : ')
        while(True):
            if tournament_month.isdigit() \
            and len(tournament_month) == 2 \
            and int(tournament_month) <= 12:
                break
            else:
                tournament_month = input('Mois invalide. '
                                         'Entrez le mois du tournoi en chiffres : ')

        tournament_year = input('Entrez l\'année du tournoi : ')
        while(True):
            if tournament_year.isdigit() \
            and len(tournament_year) == 4 \
            and int(tournament_year) >= 2021:
                break
            else:
                tournament_year = input('Année invlide. '
                                        'Entrez l\'année du tournoi : ')
        date = f'{tournament_day}/{tournament_month}/{tournament_year}'

        return date


    def add_number_of_tours(self):
        number_of_tours = 4
        print('Le nombre de tours par défaut est de 4. \n'
              'Souhaitez vous changer ce nombre ?')

        valid_tours_number = False
        while not valid_tours_number:
            tour_choice = input("Entrez 'Y' pour changer, ou 'N' pour garder 4 : ")
            if tour_choice == 'Y' or tour_choice == 'y':
                number_of_tours = input('Entrez le nombre de tours : ')
                if number_of_tours.isdigit():
                    valid_tours_number = True
                else:
                    print('Nombre de tours invalide. '
                          'Entrez le nombre de tours : ')
            if tour_choice == 'N' or tour_choice == 'n':
                valid_tours_number = True
        return number_of_tours


    def add_time_control(self):
        print('Choisissez le contrôle du temps.\n'
              'Entrez 1 pour le Bullet \n'
              'Entrez 2 pour le Blitz \n'
              'Entrez 3 pour le Coup Rapide')

        valid_time_control = False
        while not valid_time_control:
            time_control = input('Entrez votre choix : ')
            if time_control == '1':
                time_control = 'Bullet'
                valid_time_control = True
            elif time_control == '2':
                time_control = 'Blitz'
                valid_time_control = True
            elif time_control == '3':
                time_control = 'Coup Rapide'
                valid_time_control = True
            else:
                print('Choix invalide')
        return time_control


    def add_description(self):
        description = input('Entrez une description du tournoi : \n')
        return description

    def add_players_to_tournament(self):
        PLAYERS_LIST = self.controller.return_all_players()

        valid_add_player_choice = False
        while not valid_add_player_choice:
            add_player_choice = input("Voulez-vous ajouter un joueur ?\n"
                                      "Appuyer sur 'Y' pour confirmer, ou 'N' pour ignorer : ")
            if add_player_choice == 'Y' or add_player_choice == 'y':
                valid_add_player_choice = True
            elif add_player_choice == "N" or add_player_choice == 'n':
                return self.players_entry
            else:
                print("Entrez sur 'Y' ou 'N'")


        valid_id = False
        while not valid_id:
            print(f'Liste de joueurs : \n{PLAYERS_LIST}\n\n')
            print('Joueurs dans le tournoi : \n')
            for player in self.players_entry:
                print(f"{player['player_id']} - {player['last_name']} {player['first_name']}")
            id_choice = input('Entrez l\'id du joueur à ajouter : \n')
            try:
                int(id_choice)
            except Exception:
                print('Vous devez entrer l\'id du joueur')
            else:
                valid_id = True
        id_choice = int(id_choice)
        
        if id_choice <= 0 or id_choice > len(PLAYERS_LIST):
            print('id de joueur non reconnu')
            self.add_players_to_tournament()

        if id_choice in self.players_ids:
            print('Ce joueur participe déjà au tournoi')
            self.add_players_to_tournament()

        self.players_ids.append(id_choice)


        id_choice = str(id_choice)
        player = next(item for item in PLAYERS_LIST if item['player_id'] == id_choice)
        print(player)
        self.players_entry.append(player)
        print(f'Le joueur avec l\'id {id_choice} a été ajouté au tournoi')
        self.add_players_to_tournament()


    def select_tournament(self):
        TOURNAMENTS_LIST = self.controller.return_tournaments_list()

        for tournament in TOURNAMENTS_LIST:
            print(f"{tournament['tournament_id']} - {tournament['tournament_name']} - {tournament['date']}")

        valid_id = False
        while not valid_id:
            id_choice = input('Entrez l\'id du tournoi choisi : ')

            try:
                int(id_choice)
            except Exception:
                print('Vous devez entrer l\'id du tournoi')
            else:
                valid_id = True
        id_choice = int(id_choice)

        if id_choice <= 0 or id_choice > len(TOURNAMENTS_LIST):
            print('id de tournoi non reconnu')
            self.select_tournament()

        tournament = next(item for item in TOURNAMENTS_LIST if item['tournament_id'] == id_choice)
        print(tournament)

        return tournament