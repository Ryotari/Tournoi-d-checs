from models import player_model
from views import player_view


class PlayerController:
    """Enter the player's informations and add him into the database"""
    def __init__(self, main_controller):
        self.model = player_model.Player(self)
        self.view = player_view.PlayerView(self)
        self.main_controller = main_controller

   
    def create_player(self):
        player_data = self.view.display_create_player()
        self.model.save_player(player_data)

   
    def get_all_players(self):

        return self.model.send_player_database()

    
    def return_player_id(self):

        return self.model.add_player_id()


    def run_display_player_menu(self):
        option = self.view.display_player_menu()
        if option == '0':
            return
        elif option == '1':
            self.create_player()
        elif option == '2':
            self.view.update_ranking()

    def run_display_player_search_menu(self):
        option = self.view.display_player_search_menu()
        if option == '0':
            return
        elif option == '1':
            player_database = self.view.display_players_by(sort_key = 'last_name')
            if len(player_database) == 0:
                print('Aucun joueur ne se trouve dans la base de données.')
            else:
                self.view.display_chosen_player()
        elif option == '2':
            player_database = self.view.display_players_by(sort_key = 'ranking')
            if len(player_database) == 0:
                print('Aucun joueur ne se trouve dans la base de données.')
            else:
                self.view.display_chosen_player()
