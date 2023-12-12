import os
import glob
import time

os.system("modprobe w1-gpio")
os.system("modprobe w1-therm")

base_dir = "/sys/bus/w1/devices/"
device_folder = glob.glob(base_dir + "28*")[0]
temp1 = device_folder + "/w1_slave"
device_folder = glob.glob(base_dir + "28*")[1]
temp2 = device_folder + "/w1_slave"
device_folder = glob.glob(base_dir + "28*")[2]
temp3 = device_folder + "/w1_slave"
temps = [temp1, temp2, temp3]
print("GO")


def read_temp_raw(i):
    f = open(temps[i], "r")
    lines = f.readlines()
    f.close()
    return lines


def read_temp(i):
    lines = read_temp_raw(i)
    while lines[0].strip()[-3:] != "YES":
        time.sleep(0.2)
        lines = read_temp_raw(i)
    equals_pos = lines[1].find("t=")
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2 :]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f


while True:
    print(str(read_temp(0)) + "\t" + str(read_temp(1)) + "\t" + str(read_temp(2)))
    time.sleep(1)
