class Boxer_Information:

    def __init__(self, boxerName, boxerAge, boxerWeightKg,):
        self.boxerName = boxerName
        self.boxerAge = boxerAge
        self.boxerWeightKg = boxerWeightKg

    def readBoxerWeightKg(self):
       print(self.boxerWeightKg)

class WeightConversion:

     def __init__(self, boxer_Information):
        self.boxer = boxer_Information

     def kiloToPound(self):
        if isinstance(self.boxer.boxerWeightKg,int):
            print(self.boxer.boxerWeightKg / 0.45)


boxer_Information = Boxer_Information("Conor", 24, 73)

weightConversion = WeightConversion(boxer_Information)
weightConversion.kiloToPound()