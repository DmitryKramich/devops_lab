import psutil
import json
import argparse
import time
from datetime import datetime

numberSnapshot = 0

parser = argparse.ArgumentParser(description="Monitoring script for Host")
parser.add_argument(
    "data_type",
    type=str,
    nargs="?",
    const=1,
    help="Output file format: txt or json",
    default="txt"
    )
parser.add_argument(
    "time_interval",
    type=int,
    nargs="?",
    const=1,
    help="Time interval in which you will get data",
    default=30
    )
args = parser.parse_args()

class PCInfo:
    def __init__(self):
        self.cpu = self.get_cpu()
        self.mem = self.get_mem()
        self.vmem = self.get_vmem()

    def get_cpu(self):
        return psutil.cpu_percent()

    def get_mem(self):
        return psutil.disk_usage("/").percent

    def get_vmem(self):
        return psutil.virtual_memory().percent

def ctime():
    return str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def output_json():
    to_json = {
        "SNAPSHOT": str(numberSnapshot),
        "Time stamp": ctime(),
        "MEMORY": PCInfo().mem,
        "VIRTUAL_MEMORY": PCInfo().vmem
        }
    with open("info.json", "a") as f:
        json.dump(to_json, f, indent=3)
        f.write("\n")
    print("info.json created")
    return None

def output_txt():
    stringPattern = "SNAPSHOT {num}: TIME STAMP: {time} \
    CPU: {cpu} % MEMORY: {mem} % VIRTUAL_MEMORY: {vmem} % \
    ".format(
        num=numberSnapshot,
        time=ctime(),
        cpu=PCInfo().cpu,
        mem=PCInfo().mem,
        vmem=PCInfo().vmem
        )
    with open("info.txt", "a") as f:
        f.write(stringPattern+"\n")
    print("info.txt created")
    return None

while True:
    numberSnapshot += 1
    if args.data_type == "txt":
        output_txt()
    elif args.data_type == "json":
        output_json()
    else:
        print("Avaliable format type: txt or json")
    time.sleep(args.time_interval)
