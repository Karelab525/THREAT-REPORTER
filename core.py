import csv
import pandas


def start(PathToFile, PathToFolder):
    print_ip_port(PathToFile)


def open_csv(PathToFile):
    IOC = []
    with open(PathToFile) as data:
        reader = csv.reader(data)
        for line in reader:
            IOC.append(line)
    return IOC


def print_ip_port(PathToFile):
    i = 1
    IOC = open_csv(PathToFile)
    while i < len(IOC) - 1:
        IOCVal = IOC[i][2].split(":")
        i += 1
        print(IOCVal)
