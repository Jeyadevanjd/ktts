import os
import sys
from configparser import ConfigParser
configr = ConfigParser()
from subprocess import Popen as pop
pp = os.getcwd()
config = ConfigParser()
val = []
path = pp
para = path + "/det.ini"
print(para)
val2 = []
config.read(para)
ad = config['installation']['installation']
print(pp)
if ad == "False":
    pas = input("pleae enter your password for root permission:")
ll = "echo " + pas + " |" +  " sudo -S -k apt-get install flite"
if ad == "False":
    print("starting")
    os.system(ll)
    config['installation'] = {
    "installation" : "true"
    }
    with open(para, 'w') as f:
        config.write(f)
    print("done")
def say(x):
    print(x)
    xr = '"' + x + '"'
    exe = "cd " + path + " && " + "flite -voice ./cmu_us_eey.flitevox -t" + " " + xr
    os.system(exe)
#say("a quick brown fox jumps over the lazy dog")
