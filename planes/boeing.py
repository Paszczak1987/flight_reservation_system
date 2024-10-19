from .airplane import Airplane


class Boeing(Airplane):
    def __init__(self, model, seating_plan):
        super().__init__(seating_plan)
        self.model = model
        self.name = 'Boeing'
        