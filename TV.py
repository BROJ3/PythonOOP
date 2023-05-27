#TV class

class TV():
    def __init__(self,brand,location):
        self.is_on=False
        self.brand=brand
        self.location=location
        self.is_muted=False
        #some default channels
        self.channel_list=[1,2,3,4,5,6,7,8,9]
        self.n_channels = len(self.channel_list)
        self.channel_index=0
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 10
        self.volume = self.VOLUME_MAXIMUM

    def power(self):
        self.is_on = not self.is_on #toggles it to opposite ofwhat it is - WOW

    def volume_up(self):
        if not self.is_on:
            return
        if self.is_muted:
            self.is_muted=False
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volume_down(self):
        if not self.is_on:
            return
        if self.is_muted:
            self.is_muted=False
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1
    
    def channel_up(self):
        if not self.is_on:
            return
        self.channel_index = self.channel_index + 1
        if self.channel_index > self.n_channels:
            self.channel_index = 0 # wraps around to first channel

    def channel_down(self):
        if not self.is_on:
            return
        self.channel_index = self.channel_index - 1
        if self.channel_index < 0:
            self.channel_index = self.n_channels - 1 

    def mute(self):
        if not self.is_on:
            return
        self.is_muted = not self.is_muted

    def set_channel(self, new_channel):
        if new_channel in self.channel_list:
            self.channel_index = self.channel_list.index(new_channel)
            
    def show_info(self):
        print()
        print('TV Status:')
        if self.is_on:
            print('TV ' + self.brand + ' in the ' + self.location +' is on')
            print('Channel is: ',self.channel_list[self.channel_index])
            if self.is_muted:
                print("TV is muted")
            else:
                print("Volume is: ", self.volume)

        else:
            print("TV is off")


#Running this
oTV1=TV('Samsung','Family room')
oTV2=TV('Sony','Bedroom')

oTV1.power()
oTV2.power()

oTV1.volume_up()
oTV2.volume_up()

oTV2.volume_up()
oTV2.volume_up()
oTV2.volume_up()
oTV2.volume_up()

oTV1.set_channel(4)
oTV1.mute()

oTV1.show_info()
oTV2.show_info()