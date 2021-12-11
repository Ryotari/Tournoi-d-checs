from models import tournament_model

class TournamentDisplay:
    """Display the upcoming tournament's details"""

    def __call__(self):
        tournaments_db = tournament_model.tournament_db

        for tournament in tournaments_db:
            if tournament['Tours'] == []:
                print(f"Nom: {tournament['Nom du tournoi']} - \
                		Lieu: {tournament['Lieu']}")
