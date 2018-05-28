from pyo import *
from threading import Thread

class Audio:

    def __init__(self):
        self.SNDS_PATH = 'camera/python-sound-lib/audioFiles/'
        # pa_list_devices()
        self.server = Server(audio='portaudio', sr=44100, nchnls=2, duplex=0)
        # self.server.setOutputDevice(6)
        self.server.boot()
        while(not self.server.getIsBooted()):
            pass

        self.player = SfPlayer(self.SNDS_PATH + "afstand.wav").out()
        self.lfo = LFO(freq=0)
        self.pan = Pan(self.lfo, spread=0)

    def emit(self, frequency, pan):
        if(self.STATE == 'RUNNING'):
            self.lfo.setFreq(frequency)
            self.pan.setPan(pan)

    def stop(self):
        self.server.stop()
        self.STATE = 'STOPPED'

    def start(self):
        if not self.server.getIsStarted():
            self.server.start()
            while not self.server.getIsStarted():
                pass

        self.pan.out()
        self.STATE = 'RUNNING'

    def playSample(self, name, pan):
        self.player.setPath(self.SNDS_PATH + name + '.wav')
        self.player.out()


