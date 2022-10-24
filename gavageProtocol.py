import pyfirmata
import os
from datetime import datetime as dt
import time

#### SET THE EXPERIMENT CONDITIONS ##
data_folder = r'R:\data\minel\\'
genotype = 'elavl3H2BGCaMP8m'
age = 7 # in dpf
stimulus = 'glucose'
concentration = '500mM'
fish_id = 1

region = 'vagal'
side = 'R'

startBaselineDuration = 180 # in seconds, duration between the start and injection

###
exp_name = f'{genotype}_{age}dpf_{stimulus}_{concentration}_{fish_id}_{dt.today().strftime("%Y%m%d")}'
exp_folder = os.path.join(data_folder, exp_name)
os.mkdir(exp_folder)

if region == 'vagal':
    pregavage_folder = os.path.join(exp_folder, f'pregavage_{region}_{side}')
else:
    pregavage_folder = os.path.join(exp_folder, f'pregavage_{region}')
os.mkdir(pregavage_folder)
pregavage_anatomy_folder = os.path.join(pregavage_folder, os.path.basename(pregavage_folder)+'_anatomy')
os.mkdir(pregavage_anatomy_folder)

if region == 'vagal':
    postgavage_folder = os.path.join(exp_folder, f'postgavage_{region}_{side}')
else:
    postgavage_folder = os.path.join(exp_folder, f'postgavage_{region}')
os.mkdir(postgavage_folder)
postgavage_anatomy_folder = os.path.join(postgavage_folder, os.path.basename(postgavage_folder)+'_anatomy')
os.mkdir(postgavage_anatomy_folder)

file = open(os.path.join(exp_folder, 'injection.txt'), 'w')
board = pyfirmata.Arduino('COM9')
led = board.get_pin('d:13:o')
led.write(1)

input('Press Enter to continue...') # requires user input to start the experiment

time.sleep(startBaselineDuration)
led.write(0)
file.write(dt.now().strftime('%H:%M:%S.%f') + '\n')

file.close()
