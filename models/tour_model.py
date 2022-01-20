

class Tour:

    def __init__(self, tour_controller):
        self.controller = tour_controller
        self.tour_name = None
        self.begin_time = None
        self.end_time = None
        self.finished_matchs = []
        self.list_of_tours = []

    def __repr__(self):
        return f'{self.tour_name} - Début : {self.begin_time}. Fin : {self.end_time}.'

    def serialized_tour(self, tour):
        tour_informations = {
            'tour_name': tour['tour_name'],
            'begin_time': tour['begin_time'],
            'end_time': tour['end_time'],
            'finished_matchs': tour['finished_matchs']
        }
        return tour_informations

    def unserialized_tour(self, serialized_tour):
        tour_name = serialized_tour['tour_name']
        begin_time = serialized_tour['begin_time']
        end_time = serialized_tour['end_time']
        finished_matchs = serialized_tour['finished_matchs']
        return Tour(tour_name,
                    begin_time,
                    end_time,
                    finished_matchs
                    )

