import pyfirmata
import os
from datetime import datetime as dt
import time

#### SET THE EXPERIMENT CONDITIONS ##
saveInFolder = r'C:\Users\minel\iCloudDrive\Documents\Duke University\Naumann Lab\Gut-Brain\Gavage'
genotype = 'elavl3GCaMP6s'
age = 6 # in dpf
feed = 'compunfed' # compunfed, unfed, or fed
stimulus = 'fructose'
concentration = '500mM'
fish_id = 10

startBaselineDuration = 10 # in seconds, duration between the start and injection
###

file = open(os.path.join(saveInFolder, f'{genotype}_{age}dpf_{feed}_{stimulus}_{concentration}_{fish_id}_\
                                {dt.today().strftime("%Y%m%d")}.txt'), 'w')
board = pyfirmata.Arduino('COM3')
led = board.get_pin('d:13:o')
led.write(1)

input('Press Enter to continue...') # requires user input to start the experiment

time.sleep(startBaselineDuration)
led.write(0)
file.write(dt.now().strftime('%H:%M:%S.%f') + '\n')

file.close()
