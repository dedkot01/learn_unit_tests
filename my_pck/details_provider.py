class DetailsProvider:
    def __init__(self, name, cost, destination):
        self.name = name
        self.cost = cost
        self.destination = destination

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def get_destination(self):
        return self.destination
