from models import tournament_model

class TournamentDisplay:
    """Display the upcoming tournament's details"""

    def __call__(self):
        tournaments_db = tournament_model.tournament_db

        for tournament in tournaments_db:
            if tournament['Tours'] == []:
                print(f"Nom: {tournament['Nom du tournoi']} - \
                		Lieu: {tournament['Lieu']}")


class TournamentMenus:
    tournament_menu = [('1', 'Afficher tous les tournois'),
                       ('2', 'Choisir un tournoi'),
                       ('3', 'Retour au menu')]

    chosen_tournament_menu = [('1', 'Afficher les joueurs par ordre alphabétique'),
                              ('2', 'Afficher les joueurs par classement'),
                              ('3', 'Afficher les tours'),
                              ('4', 'Afficher les matchs'),
                              ('5', 'Retour au menu')]