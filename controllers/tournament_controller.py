from models import tournament_model
from views import tournament_view
from controllers import main_controller


class TournamentController:
    """Enter the tournament's informations and add it into the database"""
    def __init__(self):
        self.view = tournament_view.TournamentView()
        self.model = tournament_model.Tournament()


    def create_tournament(self):

        tournament_data = self.view.display_create_tournament()
        self.model.save_tournament(tournament_data)

