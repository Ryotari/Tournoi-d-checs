from models import tour_model
from views import tour_view


class TourController:


    def __init__(self, main_controller, player_controller):
        self.view = tour_view.TourView(self)
        self.model = tour_model.Tour(self)
        self.main_controller = main_controller
        self.player_controller = player_controller


    def run_tour_one(self, tournament):
        self.view.display_run_tour_one(tournament)

    def run_other_tours(self, tournament):
        self.view.display_run_other_tours(tournament)

    def get_player_database(self):

        return self.player_controller.get_all_players()
