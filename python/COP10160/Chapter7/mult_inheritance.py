class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed

    def vocalize(self):
        print("Chuff")

    def __str__(self):
        return f"The {type(self).__name__.lower()} "\
            f"weighs {self.mass_in_kg}kg,"\
            f" has a lifespan of {self.lifespan_in_years} years and "\
            f"can run at a maximum speed of {self.speed_in_kph}kph."

class Lion(Cat):
    def __init__(self, mass=190, lifespan=14, speed=80):
        super().__init__(mass, lifespan, speed)
        self.is_social = True

    def vocalize(self):
        print("ROAR")

class Tiger(Cat):
    def __init__(self, mass=310, lifespan=26, speed=65):
        super().__init__(mass, lifespan, speed)
        self.coat_pattern = "striped"
    def swim(self):
        print("Splash splash")

    def vocalize(self):
        print("ROAR")

class Liger(Lion,Tiger):
    pass

##########

class MobilePhone:
    def __init__(self, memory):
        self.memory = memory

class Camera:
    def take_picture(self):
        print("Say cheese!")

class CameraPhone(MobilePhone, Camera):
    pass

liger=Liger()
print(liger.swim())
print(liger.is_social)
print(liger.coat_pattern)

##########

cameraphone = CameraPhone("200KB")
cameraphone.take_picture()
print(cameraphone.memory)

