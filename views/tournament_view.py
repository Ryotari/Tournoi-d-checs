from models import tournament_model
from controllers import tournament_controller


class TournamentDisplay:
    """Display the upcoming tournament's details"""

    def __call__(self):
        tournaments_db = tournament_model.tournament_db

        for tournament in tournaments_db:
            if tournament['Tours'] == []:
                print(f"Nom: {tournament['Nom du tournoi']} - \
                		Lieu: {tournament['Lieu']}")


class TournamentMenus:
    tournament_menu = """
                    Veuillez choisir une option :\n
                    1 : Afficher tous les tournois\n
                    2 : Choisir un tournoi\n
                    0 : Retour au menu\n"""

    chosen_tournament_menu = """
                            1 : Afficher les joueurs par ordre alphabétique\n
                            2 : Afficher les joueurs par classement\n
                            3 : Afficher les tours\n
                            4 : Afficher les matchs\n
                            0 : Retour au menu\n"""


class TournamentView:
    def __init__(self):
        self.model = tournament_model.Tournament()
        self.tournament_name = None
        self.location = None
        self.date = None
        self.number_of_rounds = 4
        self.time_control = None
        self.description = None
        self.tournament_id = None

    def display_create_tournament(self):
        self.tournament_name = self.add_tournament_name()
        self.location = self.add_location()
        self.date = self.add_tournament_date()
        self.number_of_rounds = self.add_number_of_rounds()
        self.time_control = self.add_time_control()
        self.description = self.add_description()
        self.tournament_id = self.model.add_tournament_id()
        tournament_data = {
            'tournament_name': self.tournament_name,
            'location': self.location,
            'date': self.date,
            'number_of_rounds': self.number_of_rounds,
            'time_control': self.time_control,
            'description': self.description,
            'tournament_id': self.tournament_id
        }

        return tournament_data

    def add_tournament_name(self):
        tournament_name = input('Nom du tournoi : ')
        while tournament_name == '':
            tournament_name = input('Nom invalide. '
                                    'Entrez le nom du tournoi : ')
        return tournament_name


    def add_location(self):
        tournament_location = input('Lieu du tournoi : ')
        while tournament_location == '':
            tournament_location = input('Lieu invalide. '
                                        'Entrez le lieu du tournoi : ')
        return tournament_location


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


    def add_number_of_rounds(self):
        number_of_rounds = 4
        print('Le nombre de tours par défaut est de 4. \n'
              'Souhaitez vous changer ce nombre ?')

        valid_rounds_number = False
        while not valid_rounds_number:
            round_choice = input("Entrez 'Y' pour changer, ou 'N' pour garder 4 : ")
            if round_choice == 'Y':
                number_of_rounds = input('Entrez le nombre de tours : ')
                if number_of_rounds.isdigit():
                    valid_rounds_number = True
                else:
                    print('Nombre de tours invalide. '
                          'Entrez le nombre de tours : ')
            if round_choice == 'N':
                valid_rounds_number = True
        return number_of_rounds


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
