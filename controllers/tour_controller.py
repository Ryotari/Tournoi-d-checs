from models import tour_model
from views import tour_view


class TourController:


    def __init__(self, main_controller):
        self.view = tour_view.TourView(self)
        self.model = tour_model.Tour(self)
        self.main_controller = main_controller

    def run_tour_one(self):
        self.view.sort_player_by_ranking()
