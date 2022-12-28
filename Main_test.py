class Tests:
    def __init__(self):
        self.time = []
        self.place = []


    # method for collision's time
    def timer(self, object1_p, object2_p, object1_s, object2_s):
        t = int(object1_p + object2_p) / (object1_s + object2_s)
        print(f"Time of colision: {t} s")
        return t


    # method for collision's place
    def place_issue(self, object1_s, time):
        place1 = object1_s * time
        place = 1000 - int(place1)
        print(f"Place of colision: {place} m")
        return place