from models import tournament_model
from views import tournament_view


class TournamentController:
    """Enter the tournament's informations and add it into the database"""
    def __init__(self, main_controller, player_controller, tour_controller):
        self.view = tournament_view.TournamentView(self)
        self.model = tournament_model.Tournament(self)
        self.main_controller = main_controller
        self.player_controller = player_controller
        self.tour_controller = tour_controller

    def create_tournament(self):
        """Create a tournament and add it to the database"""
        tournament_data = self.view.display_create_tournament()
        self.model.save_tournament(tournament_data)

    def return_tournament_id(self):

        return self.model.add_tournament_id()


    def return_all_players(self):

        return self.player_controller.get_all_players()


    def return_unserialized_player(self):

        return self.player_controller.return_unserialized_player()


    def return_tournaments_list(self):
        TOURNAMENTS_LIST = self.model.send_tournaments_list()

        return TOURNAMENTS_LIST


    def start_tournament(self):
        tournament = self.view.select_tournament()
        self.tour_controller.run_tour_one()
        self.tour_controller.run_other_tours()
