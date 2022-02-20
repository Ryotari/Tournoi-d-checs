import sys
from controllers import player_controller
from controllers import tournament_controller
from controllers import tour_controller
from views import main_view


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
        self.tour_controller = (tour_controller.
                                TourController(self, self.player_controller))
        self.tournament_ctrl = (tournament_controller.
                                TournamentController(self,
                                                     self.player_controller,
                                                     self.tour_controller))

    def run(self):
        while(True):
            option = self.view.display_home()

            if option == '0':
                sys.exit()
            elif option == '1':
                self.tournament_ctrl.create_tournament()
            elif option == '2':
                self.tournament_ctrl.load_tournament()
            elif option == '3':
                self.tournament_ctrl.run_tournament_search()
            elif option == '4':
                self.player_ctrl.run_display_player_menu()
            elif option == '5':
                self.player_ctrl.run_display_player_search_menu()
