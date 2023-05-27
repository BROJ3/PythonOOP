class dimmer_switch():
    def __init__(self):
        self.switch_on = False
        self.brightness = 0
    
    def turn_on(self):
        self.switch_on=True

    def turnoff(self):
        self.switch_on=False

    def raise_level(self):
        if self.brightness < 10:
            self.brightness += 1
        
    def lower_level(self):
        if self.brightness > 0:
            self.brightness -= 1

    def show(self):
        print('Switch is on?', self.switch_on)
        if self.switch_on == True:
            print("Brightness is", self.brightness)

my_dimmer1=dimmer_switch()
my_dimmer2=dimmer_switch()

my_dimmer1.turn_on()
my_dimmer1.raise_level()
my_dimmer1.raise_level()
my_dimmer1.raise_level()
my_dimmer1.raise_level()
my_dimmer1.raise_level()

my_dimmer2.turn_on()
my_dimmer1.raise_level()
my_dimmer1.raise_level()
my_dimmer1.raise_level()


my_dimmer3=dimmer_switch()

my_dimmer1.show()
my_dimmer2.show()
my_dimmer3.show()

print(type(my_dimmer1))
print(my_dimmer1)

print(type(my_dimmer2))
print(my_dimmer2)

print(type(my_dimmer3))
print(my_dimmer3)

print('my_dimmer1 variables: ',vars(my_dimmer1))