#!/usr/bin/python

'This application has been created for Python 2.7.11'

import json
import datetime
import time
import psutil
import configparser


config=configparser.ConfigParser()
config.read('conf.ini')
file=config.get('common', 'outputfile')
interval=config.get('common', 'interval')

cpu = psutil.cpu_times(percpu=True)
cpu_p = psutil.cpu_percent(percpu=True)
mem = psutil.virtual_memory()
disk = psutil.disk_usage('/')
disk_io = psutil.disk_io_counters()
net_count = psutil.net_io_counters(pernic=True)


counter = 1


def write_to_txt(counter):
    timestamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    f = open('write.txt', "a")
    f.write("\n!!!Counter {0} : {1}!!!\n".format(counter, timestamp))
    f.write("CPU: {0}\n".format(cpu[0]))
    f.write("CPU in percent: {0}%\n".format(cpu_p[0]))
    f.write("Memory usage: {0}Mb\n".format(mem[0] / 1048576))
    f.write("Disk {}Mb\n".format(disk[0] / 1048576))
    f.write("Disk IO {0}Mb\n".format(disk_io[0] / 1048576))
    f.write("Net_Counter {}\n".format(net_count))
    f.write("\n")
    f.close()

def json_dict(json_list):
    return dict(zip(list(json_list), json_list._fields))

def write_to_json(counter):
    timestamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    jsonf = open('write.json', "a")
    jsonf.write("\n!!!Counter {0} : {1}!!!\n".format(counter, timestamp))
    jsonf.write("\nCPU\n")
    json.dump(cpu, jsonf, indent=1)
    jsonf.write("\nCPU in percent\n")
    json.dump(cpu_p, jsonf, indent=1)
    jsonf.write("\nMemory usage\n")
    json.dump(mem, jsonf, indent=1)
    jsonf.write("\nDisk\n")
    json.dump(json_dict(disk), jsonf, indent=1)
    jsonf.write("\nDisk IO\n")
    json.dump(json_dict(disk_io), jsonf, indent=1)
    jsonf.write("\nNet_Counter\n")
    json.dump(net_count, jsonf, indent=1)
    jsonf.write("\n\n")
    jsonf.close()


while True:
    if file == "txt":
        write_to_txt(counter)
    elif file=="json":
        write_to_json(counter)
    else:
        print("Wrong file type configuration!")
    counter += 1
    time.sleep(int(interval))





