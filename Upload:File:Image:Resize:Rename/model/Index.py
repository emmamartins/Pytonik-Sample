from pytonik.Model import Model
from pytonik.Functions.iteration import iteration

class Index(Model, iteration):

    def __getattr__(self, item):
        return item

    def __init__(self):
        return None

