#!/usr/bin/python

'This application has been created for Python 2.7.11'

import json
import datetime
import time
import psutil
import configparser

class Data(object):
    cpu = psutil.cpu_times(percpu=True)
    cpu_p = psutil.cpu_percent(percpu=True)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    disk_io = psutil.disk_io_counters()
    net_count = psutil.net_io_counters(pernic=True)

    @staticmethod
    def json_dict(json_list):
        return dict(zip(list(json_list), json_list._fields))

class WriteToTXT(Data):
    counter = 1
    def write_to_txt(self):
        timestamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        f = open('write.txt', "a")
        f.write("\n!!!Counter {0} : {1}!!!\n".format(self.counter, timestamp))
        f.write("CPU: {0}\n".format(Data.cpu[0]))
        f.write("CPU in percent: {0}%\n".format(Data.cpu_p[0]))
        f.write("Memory usage: {0}Mb\n".format(Data.mem[0] / 1048576))
        f.write("Disk {}Mb\n".format(Data.disk[0] / 1048576))
        f.write("Disk IO {0}Mb\n".format(Data.disk_io[0] / 1048576))
        f.write("Net_Counter {}\n".format(Data.net_count))
        f.write("\n")
        f.close()

class WriteToJSON(Data):
    counter = 1
    def write_to_json(self):
        timestamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        jsonf = open('write.json', "a")
        jsonf.write("\n!!!Counter {0} : {1}!!!\n".format(self.counter, timestamp))
        jsonf.write("\nCPU\n")
        json.dump(Data.cpu, jsonf, indent=1)
        jsonf.write("\nCPU in percent\n")
        json.dump(Data.cpu_p, jsonf, indent=1)
        jsonf.write("\nMemory usage\n")
        json.dump(Data.mem, jsonf, indent=1)
        jsonf.write("\nDisk\n")
        json.dump(Data.json_dict(Data.disk), jsonf, indent=1)
        jsonf.write("\nDisk IO\n")
        json.dump(Data.json_dict(Data.disk_io), jsonf, indent=1)
        jsonf.write("\nNet_Counter\n")
        json.dump(Data.net_count, jsonf, indent=1)
        jsonf.write("\n\n")
        jsonf.close()


config=configparser.ConfigParser()
config.read('conf.ini')
file=config.get('common', 'outputfile')
interval=config.get('common', 'interval')

txt_obj = WriteToTXT()
json_obj = WriteToJSON()
txt_obj.counter = 1
json_obj.counter = 1

while True:
    if file == "txt":
        txt_obj.write_to_txt()
        txt_obj.counter += 1
    elif file == "json":
        json_obj.write_to_json()
        json_obj.counter += 1
    else:
        print("Wrong file type configuration!")
    time.sleep(int(interval))





