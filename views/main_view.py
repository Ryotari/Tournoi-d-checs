

class MainMenu:

    def display_home(self):
        home_menu = '''
            Veuillez choisir une option :\n
            1: Créer un tournoi\n
            2: Charger un tournoi\n
            3: Chercher un tournoi\n
            4: Créer ou modifier un joueur\n
            5: Chercher un joueur\n
            0: Sortir du programme\n'''

        option = input(home_menu)

        while option not in ['0', '1', '2', '3', '4', '5']:
            option = input(home_menu)

        return option
