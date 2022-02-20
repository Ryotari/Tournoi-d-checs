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

    def run_tournament_search(self):
        tournament_database = self.view.display_all_tournaments()
        if len(tournament_database) == 0:
            print('Aucun tournoi ne se trouve dans la base de données.')
        else:
            self.view.display_chosen_tournament()

    def return_all_players(self):

        return self.player_controller.get_all_players()

    def return_unserialized_player(self):

        return self.player_controller.return_unserialized_player()

    def get_all_tournaments(self):

        return self.model.send_tournament_database()

    def load_tournament(self):
        tournament = self.view.select_tournament()
        if tournament is None:
            return
        tournament = self.model.unserialized_tournament(tournament)

        if len(tournament['list_of_tours']) == 0:
            tournament = self.tour_controller.run_tour_one(tournament)
            self.save_tour(tournament)

            while (len(tournament['list_of_tours']) <
                   tournament['number_of_tours']):
                tournament = self.tour_controller.run_other_tours(tournament)
                self.save_tour(tournament)
        else:
            while (len(tournament['list_of_tours']) <
                   tournament['number_of_tours']):
                tournament = self.tour_controller.run_other_tours(tournament)
                self.save_tour(tournament)

    def save_tour(self, tournament):
        self.model.update_tournament(tournament)
