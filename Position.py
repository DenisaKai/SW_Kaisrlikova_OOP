import random
class Position:
    # generate positions of objects
    def generate_position(self):
        position_1 = []
        position_2 = []
        # position of first object
        for j in range(0, 10):
            position_1.append(random.randint(0, 500))
        # position of second object
        for j in range(0, 10):
            h = random.randint(0, 500)
            if h == position_1:
                h2 = random.randint(0, 500)
                if h2 == h:
                    print("Error position")
                else:
                    position_2.append(h2)
            else:
                position_2.append(h)
        #print((position_1, position_2))
        return position_1, position_2

position = Position().generate_position()