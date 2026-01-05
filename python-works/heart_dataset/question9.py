# Find patients with Chest pain type = 4 and Heart Disease = Presence.

import csv

class Heart:

    data : list

    def __init__(self):

        file_path = "heart_dataset\\Heart_Disease_Prediction.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def chest_pain(self):

        chest_pains = [ i for i in self.data if int(i.get("Chest pain type"))==4 and i.get("Heart Disease")=="Presence"]

        print(chest_pains)

instance =Heart()

instance.chest_pain()