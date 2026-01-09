from data import InputData

class Proses:
    def __init__(self, data: InputData):
        self.data = data
    
    def bagi(self):
        try:
            if self.data.b == 0:
                raise ValueError("Pembagi tidak boleh nol.")
            return self.data.a / self.data.b
        except ValueError as e:
            return str(e)   