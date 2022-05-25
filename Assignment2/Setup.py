

from imports import pd

class SetUp: 

    def __init__(self, file, types):
        self.df = self.load_csv(file, types)

    def load_csv(self, file, types):
        self.df = pd.read_csv(file, parse_dates = True, dtype = types)
        return self.df

    