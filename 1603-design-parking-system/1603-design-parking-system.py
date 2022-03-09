class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking_system = {}
        self.parking_system[1] = big
        self.parking_system[2] = medium
        self.parking_system[3] = small

    def addCar(self, carType: int) -> bool:
        if self.parking_system[carType] > 0:
            self.parking_system[carType] -= 1
            return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)