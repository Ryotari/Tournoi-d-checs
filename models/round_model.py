

class Round:

    def __init__(self, name=None, 
                 begin_time=None, 
                 end_time=None, 
                 list_of_finished_matchs=None
                 ):
        self.name = name
        self.begin_time = begin_time
        self.end_time = end_time
        self.list_of_matchs = list_of_finished_matchs
        self.list_of_tours = []

    def __repr__(self):
        return f'{self.name} - Début : {self.begin_time}. Fin : {self.end_time}.'

    def serialized(self):
        round_informations = {}
        round_informations['Nom'] = self.name
        round_informations['Debut'] = self.begin_time
        round_informations['Fin'] = self.end_time
        round_informations['Matchs'] = self.list_of_matchs
        return round_informations

    def unserialized(self, serialized_tour):
        name = serialized_tour['Nom']
        begin_time = serialized_tour['Debut']
        end_time = serialized_tour['Fin']
        list_of_finished_matchs = serialized_tour['Matchs']
        return Tour(name,
                    begin_time,
                    end_time,
                    list_of_matchs
                    )

