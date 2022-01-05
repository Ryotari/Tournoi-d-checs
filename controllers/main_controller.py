from controllers import player_controller
from controllers import tournament_controller
from views import player_view
from views import tournament_view
from views import main_view
from models import player_model
from models import tournament_model


"""class CreateMenus:
    Create the main menu and all the navigation throughout the application

    def __call__(self, menu_to_display):
        Display the menu and ask the user where he wants to navigate to

        for line in menu_to_display:
            print(line[0] + ' : ' + line[1])

        while(True):
            choice = input('Entrez le chiffre correspondant à votre choix : ')
            for line in menu_to_display:
                if choice == line[0]:
                    return str(line[0])
            print('Choix non valide.')


class MainMenuController:

    def __init__(self):
        self.main_view = main_view.MainMenu()
        self.create_menu = CreateMenus()
        self.chosen_controller = None


    def __call__(self):
        choice = self.create_menu(self.main_view.main_menu)

        if choice == '1':
            self.chosen_controller = tournament_controller.CreateTournament()

        if choice == '2':
            pass

        if choice == '3':
            pass

        if choice == '4':
            self.chosen_controller = player_controller.CreatePlayer()

        if choice == '5':
            pass
"""

class MainMenuController:
    """Main Controller for the aplication"""
    """
            Veuillez choisir une option :\n
            1: Créer un tournoi\n
            2: Charger un tournoi\n
            3: Chercher un tournoi\n
            4: Créer ou modifier un joueur\n
            5: Chercher un joueur\n
            0: Sortir du programme
        """
    def __init__(self):
        self.view = main_view.MainMenu()
        self.tournoi_ctrl = tournament_controller.TournamentController()
        self.player_controller = player_controller.PlayerController()


    def run(self):
        option = self.view.display_home()

        if option == '0':
            sys.exit()
        elif option == '1':
            self.tournoi_ctrl.create_tournament()
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            self.player_controller.run_display_player_menu()
        elif option == '5':
            pass

"""
class TournamentMenuController(MainMenuController):

    def __init__(self):
        super().__init__()
        


class PlayerMenuController(MainMenuController):

    def __init__(self):
        super().__init__()
"""