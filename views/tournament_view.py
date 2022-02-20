

class TournamentMenus:
    """Display the tournament menus"""

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
        self.player_scores = {}
        self.list_of_tours = []
        # self.player_scores = {player_id:0 for player_id in self.players_ids}

    def display_create_tournament(self):
        self.tournament_name = self.add_tournament_name()
        self.location = self.add_location()
        self.date = self.add_tournament_date()
        self.number_of_rounds = self.add_number_of_tours()
        self.time_control = self.add_time_control()
        self.description = self.add_description()
        self.tournament_id = self.controller.return_tournament_id()
        self.add_players_to_tournament()
        self.player_scores = {player_id: 0 for player_id in self.players_ids}
        self.list_of_tours = []
        tournament_data = {
            'tournament_name': self.tournament_name,
            'location': self.location,
            'date': self.date,
            'number_of_tours': self.number_of_tours,
            'time_control': self.time_control,
            'description': self.description,
            'tournament_id': self.tournament_id,
            'players_ids': self.players_ids,
            'player_scores': self.player_scores,
            'list_of_tours': self.list_of_tours
        }

        return tournament_data

    def display_all_tournaments(self):
        tournament_database = self.controller.get_all_tournaments()
        for tournament in tournament_database:
            print(f"{tournament['tournament_id']} - \
                    {tournament['tournament_name']} - \
                    {tournament['location']}")

        return tournament_database

    def display_chosen_tournament(self):
        tournament_database = self.controller.get_all_tournaments()

        message = "Choisissez l'id d'un tournoi : "

        id_choice = input(message)

        while not (id_choice.isdigit()
                   or int(id_choice) not
                   in range(1, (len(tournament_database) + 1))):
            print('id non valide.\n')
            id_choice = input(message)

        id_choice = int(id_choice)
        tournament = tournament_database.get(doc_id=id_choice)
        for key in tournament:
            print(key, ' : ', tournament[key])

        print()
        input('Appuyez sur une touche pour revenir au menu.')

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
            if (tournament_day.isdigit()
               and len(tournament_day) == 2
               and int(tournament_day) <= 31):
                break
            else:
                tournament_day = input('Jour invalide. '
                                       'Entrez le jour du tournoi : ')

        tournament_month = input('Entrez le mois du tournoi : ')
        while(True):
            if (tournament_month.isdigit()
               and len(tournament_month) == 2
               and int(tournament_month) <= 12):
                break
            else:
                tournament_month = input('Mois invalide. '
                                         'Entrez le mois du '
                                         'tournoi en chiffres : ')

        tournament_year = input('Entrez l\'année du tournoi : ')
        while(True):
            if (tournament_year.isdigit()
               and len(tournament_year) == 4
               and int(tournament_year) >= 2021):
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
            tour_choice = input("Entrez 'Y' pour changer, "
                                "ou 'N' pour garder 4 : ")
            if tour_choice.upper() == 'Y':
                number_of_tours = input('Entrez le nombre de tours : ')
                if number_of_tours.isdigit():
                    valid_tours_number = True
                else:
                    print('Nombre de tours invalide. '
                          'Entrez le nombre de tours : ')
            if tour_choice.upper() == 'N':
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
        description = input('Entrez une description du tournoi : ')

        return description

    def add_players_to_tournament(self):

        while(True):
            add_player_choice = input("Voulez-vous ajouter un joueur ?\n"
                                      "Appuyer sur 'Y' pour confirmer, "
                                      "ou 'N' pour ignorer : ")

            if add_player_choice.upper() == 'Y':
                self.add_player_to_tournament()
            elif add_player_choice.upper() == 'N':
                return
            else:
                print('Commande non reconnue')

    def add_player_to_tournament(self):
        player_database = self.controller.return_all_players()

        valid_id = False
        while not valid_id:
            print('Liste de joueurs : ')
            for player in player_database:
                print(f"{player['player_id']} - \
                        {player['last_name']} \
                        {player['first_name']}")
            print('Joueurs dans le tournoi : \n')
            for player_id in self.players_ids:
                player = player_database.get(doc_id=player_id)
                print(f"{player['player_id']} - \
                        {player['last_name']} \
                        {player['first_name']}")
            print()
            id_choice = input("Entrez l'id du joueur à ajouter : \n")
            try:
                int(id_choice)
            except Exception:
                print("Vous devez entrer l'id du joueur\n")
            else:
                valid_id = True
        id_choice = int(id_choice)

        if id_choice <= 0 or id_choice > len(player_database):
            print('id de joueur non reconnu\n')

        elif id_choice in self.players_ids:
            print('Ce joueur participe déjà au tournoi\n')

        else:
            self.players_ids.append(id_choice)
            print(f"Le joueur avec l'id {id_choice} "
                  "a été ajouté au tournoi\n\n")

    def select_tournament(self):
        tournament_database = self.controller.get_all_tournaments()
        tournaments_in_progress = []
        tournaments_in_progress_id = []
        for tournament in tournament_database:
            if (len(tournament['list_of_tours']) <
               int(tournament['number_of_tours'])):
                tournaments_in_progress.append(tournament)

        for tournament in tournaments_in_progress:
            tournaments_in_progress_id.append(tournament['tournament_id'])
            print(f"{tournament['tournament_id']} - \
                    {tournament['tournament_name']} - \
                    {tournament['location']}")

        if len(tournaments_in_progress) == 0:
            print('Aucun tournoi en cours.')
            return None

        message = "Entrez l'id du tournoi choisi : "
        id_choice = input(message)

        while not (id_choice.isdigit()
                   or int(id_choice) not in tournaments_in_progress_id):
            print('id de tournoi non valide.\n')
            id_choice = input("Entrez l'id du tournoi choisi : ")

        id_choice = int(id_choice)

        tournament = tournament_database.get(doc_id=id_choice)
        print('Tournoi choisi : \n')
        for key in tournament:
            print(key, ' : ', tournament[key])
        print()
        return tournament
