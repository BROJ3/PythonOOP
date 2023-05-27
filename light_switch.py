class light_switch():
    def __init__(self):
        self.switchisOn = False

    def turn_on(self):
        self.switchisOn = True

    def turn_off(self):
        self.switchisOn = False

    def show(self):
        print(self.switchisOn)

aLightSwitch=light_switch()
aLightSwitch2=light_switch()

aLightSwitch.show()
aLightSwitch.turn_on()
aLightSwitch.show()
aLightSwitch.turn_off()
aLightSwitch.show()
aLightSwitch.turn_on()
aLightSwitch.show()
aLightSwitch.turn_off()
aLightSwitch.show()
aLightSwitch2.turn_on()
