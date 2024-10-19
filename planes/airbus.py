from .airplane import Airplane


class Airbus(Airplane):
    def __init__(self, model, seating_plan):
        super().__init__(seating_plan)
        self.model = model
        self.name = 'Airbus'
