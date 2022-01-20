import time


class TourView:
    def __init__(self, tour_controller):
        self.controller = tour_controller
        self.tour_name = None
        self.begin_time = None
        self.end_time = None

    def display_tour(self):
        print(f'{tour_name}\n')

        for match in list_of_matchs:
            print(f'{match}\n')

    def display_begin_time(self):
        input('Appuyez sur une touche pour lancer le tour')
        begin_time = time.strftime(format('%d/%m/%Y - %Hh%Mm%Ss'))
        print(f'Début du tour : {begin_time}')

        return begin_time


    def display_end_time(self):
        input('Appuyez sur une touche pour terminer le tour')
        end_time = time.strftime(format('%d/%m/%Y - %Hh%Mm%Ss'))
        print(f'Début du tour : {end_time}')

        return end_time

    def sort_players_by_ranking(self):
        players_entry = self.tournament_view.return_players_entry()
        sorted_players = sorted(players_entry, key=lambda d: d['ranking'])

        lenght = len(players_entry)
        index = lenght // 2

        first_half = sorted_players[:index]
        second_half = sorted_players[index:]

        for i in range(index):
            print(f'Match {i+1} : {first_half[i]} vs {second_half[i]}')