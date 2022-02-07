import time


class TourView:
    def __init__(self, tour_controller):
        self.controller = tour_controller
        self.tour_name = None
        self.begin_time = None
        self.end_time = None
        self.list_of_matchs = []
        self.list_of_finished_matchs = []
        self.list_of_tours = []


    def display_run_tour_one(self, tournament):
        self.sort_players_by_ranking(tournament)
        self.begin_time = self.display_begin_time()
        self.tour_name = self.display_tour(tournament)
        self.display_entry_scores(tournament)
        self.end_time = self.display_end_time()
        self.list_of_tours.append(self.list_of_finished_matchs)
        tournament['list_of_tours'] = self.list_of_tours

        return tournament

    def display_run_other_tours(self, tournament):
        self.sort_players_by_score(tournament)
        self.begin_time = self.display_begin_time()
        self.display_tour(tournament)
        self.display_entry_scores(tournament)
        self.end_time = self.display_end_time()
        self.list_of_tours.append(self.list_of_finished_matchs)
        tournament['list_of_tours'] = self.list_of_tours

        return tournament


    def display_begin_time(self):
        input('Appuyez sur une touche pour lancer le tour')
        begin_time = time.strftime(format('%d/%m/%Y - %Hh%Mm%Ss'))
        print()
        print(f'Début du tour : {begin_time}')
        print()

        return begin_time


    def display_end_time(self):
        input('Appuyez sur une touche pour terminer le tour')
        end_time = time.strftime(format('%d/%m/%Y - %Hh%Mm%Ss'))
        print(f'Fin du tour : {end_time}')

        return end_time

    def sort_players_by_ranking(self, tournament):
        player_database = self.controller.get_player_database()
        player_instances = []
        for player_id in tournament['players_ids']:
            player = next(item for item in player_database if item['player_id'] == player_id)
            player_instances.append(player)
        sorted_players = sorted(player_instances, key=lambda d: d['ranking'])

        lenght = len(player_instances)
        index = lenght // 2

        first_half = sorted_players[:index]
        second_half = sorted_players[index:]

        MATCH_NUMBER = 1
        for i in range(index):
            match_name = 'Match' + str(MATCH_NUMBER)
            player_1 = first_half[i]
            player_2 = second_half[i]
            match_instance = (match_name, player_1['player_id'], player_2['player_id'])
            MATCH_NUMBER += 1
            self.list_of_matchs.append(match_instance)


    def sort_players_by_score(self, tournament):
        self.list_of_matchs.clear()
        self.list_of_finished_matchs.clear()
        player_instances = tournament['player_scores']
        """sorted_players = sorted(player_instances.items(), key=lambda d:d[1], reverse=True)
        print(sorted_players)"""
        sorted_players = list({player_id: player_score for player_id, player_score in sorted(player_instances.items(), key=lambda item: item[1], reverse = True)})



        MATCH_NUMBER = 1
        while sorted_players != []:
            match_name = 'Match' + str(MATCH_NUMBER)
            player_1 = sorted_players[0]
            player_2 = sorted_players[1]
            del sorted_players[0:2]
            match_instance = (match_name, player_1, player_2)
            MATCH_NUMBER += 1
            self.list_of_matchs.append(match_instance)


    def display_tour(self, tournament):
        list_of_matchs = self.list_of_matchs
        tour_name = "Tour" + str(len(tournament['list_of_tours']) + 1)
        print(f'{tour_name} :')
        print()
        for match in list_of_matchs:
            print(f'{match[0]} : {match[1]} vs {match[2]}')

        return tour_name

    def display_entry_scores(self, tournament):
        list_of_matchs = self.list_of_matchs
        for match in list_of_matchs: 
            player_1 = str(match[1])
            player_2 = str(match[2])
            valid_match_score = False
            while not valid_match_score:
                score_player_1 = input(f'Entrez le score de {match[1]} : ')

                while not score_player_1.isdigit() and score_player_1 not in [0, 0.5, 1]:
                    print('Score non valide.\n')
                    score_player_1 = input(f'Entrez le score de {match[1]} : ')
                score_player_1 = int(score_player_1)

                score_player_2 = input(f'Entrez le score de {match[2]} : ')
                while not score_player_2.isdigit() and score_player_2 not in [0, 0.5, 1]:
                    print('Score non valide.\n')
                    score_player_2 = input(f'Entrez le score de {match[2]} : ')
                score_player_2 = int(score_player_2)
                if float(score_player_1) + float(score_player_2) == float(1):
                    valid_match_score = True
                    tournament['player_scores'][player_1] += score_player_1
                    tournament['player_scores'][player_2] += score_player_2
                    print('Score enregistré. \n')
        
            self.list_of_finished_matchs.append(([match[1], score_player_1],
                                                 [match[2], score_player_2]))
        print(self.list_of_finished_matchs)
