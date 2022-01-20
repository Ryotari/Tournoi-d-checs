from controllers import player_controller
from controllers import tournament_controller
from controllers import tour_controller
from views import player_view
from views import tournament_view
from views import tour_view
from views import main_view
from models import player_model
from models import tournament_model
from models import tour_model


class MainMenuController:
    """Main Controller for the application"""
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
        self.player_controller = player_controller.PlayerController(self)
        self.tour_controller = tour_controller.TourController(self)
        self.tournoi_ctrl = tournament_controller.TournamentController(self, self.player_controller, tour_controller)
        
    def run(self):
        option = self.view.display_home()

        if option == '0':
            sys.exit()
        elif option == '1':
            self.tournoi_ctrl.create_tournament()
            self.run()
        elif option == '2':
            self.tournoi_ctrl.start_tournament()
            self.run()
        elif option == '3':
            pass
        elif option == '4':
            self.player_controller.run_display_player_menu()
            self.run()
        elif option == '5':
            self.player_controller.run_display_player_search_menu()
            self.run()
