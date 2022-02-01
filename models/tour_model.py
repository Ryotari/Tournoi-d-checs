

class Tour:

    def __init__(self, tour_controller):
        self.controller = tour_controller


    def serialized_tour(self, tour):
        tour_informations = {
            'tour_name': tour['tour_name'],
            'begin_time': tour['begin_time'],
            'end_time': tour['end_time'],
            'list_of_finished_matchs_': tour['list_of_finished_matchs']
        }
        return tour_informations

    def unserialized_tour(self, serialized_tour):
        tour_name = serialized_tour['tour_name']
        begin_time = serialized_tour['begin_time']
        end_time = serialized_tour['end_time']
        list_of_finished_matchs = serialized_tour['list_of_finished_matchs']
        return Tour(tour_name,
                    begin_time,
                    end_time,
                    list_of_finished_matchs
                    )
