from models import player_model
from views import player_view
from controllers import main_controller

class PlayerController:
    """Enter the player's informations and add him into the database"""
    def __init__(self):
        self.model = player_model.Player()
        self.view = player_view.PlayerView()


    def create_player(self):
        player_data = self.view.display_create_player()
        self.model.save_player(player_data)

    def run_display_player_menu(self):
        option = self.view.display_player_menu()
        if option == '0':
            sys.exit()
        elif option == '1':
            self.view = player_view.PlayerView()
            self.create_player()
        elif option == '2':
            pass