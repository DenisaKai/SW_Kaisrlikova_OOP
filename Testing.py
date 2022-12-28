import Objects
import Position
Rider = Objects.Rider
Pedestrian = Objects.Pedestrian
Vehicle = Objects.Vehicle
position = Position.position
ob = Objects.Object

class Testing:
    # generate objects
    def generate_data(self):
        data = []
        for i in range(0, 10):
            r = Rider(position[0][i], Rider.generate_weight(ob, 20, 130), Rider.generate_speed(ob, 1, 45), Rider)
            data.append(r)
            v = Vehicle(position[0][i], Vehicle.generate_weight(ob, 1100, 2700), Vehicle.generate_speed(ob, 1, 180), Vehicle)
            data.append(v)
            p = Pedestrian(position[0][i], Pedestrian.generate_weight(ob, 10, 90), Pedestrian.generate_speed(ob, 1, 6), Pedestrian)
            data.append(p)
        return data

    # dataset of objects
data = Testing().generate_data()