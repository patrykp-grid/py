#!/usr/bin/env python3

# A script for getting system information (CPU, Memory, Disk) using psutil library

import psutil
import argparse
import platform
import os
import socket

def get_distro_info():
    return platform.platform()

def get_memory_info():
    memory = psutil.virtual_memory()
    return {
        "total": memory.total,
        "used": memory.used,
        "free": memory.free
    }

def get_cpu_info():
    return {
        "model": platform.processor(),
        "physical_cores": psutil.cpu_count(logical=False),
        "total_cores": psutil.cpu_count(logical=True),
        "max_frequency": psutil.cpu_freq().max,
    }

def get_current_user():
    return os.getlogin()

def get_load_average():
    return os.getloadavg()

def get_ip_address():
    return socket.gethostbyname("localhost")


parser = argparse.ArgumentParser(description="System Information Script")

parser.add_argument("-d", "--distro", action="store_true", help="Show distribution information")
parser.add_argument("-m", "--memory", action="store_true", help="Show memory information")
parser.add_argument("-c", "--cpu", action="store_true", help="Show CPU information")
parser.add_argument("-u", "--user", action="store_true", help="Show current user information")
parser.add_argument("-l", "--load", action="store_true", help="Show system load average")
parser.add_argument("-i", "--ip", action="store_true", help="Show IP address")

args = parser.parse_args()

if args.distro:
    print(f"Distribution Info: {get_distro_info()}")

if args.memory:
    memory_info = get_memory_info()
    print(f"Memory Info: Total - {memory_info['total']} bytes, Used - {memory_info['used']} bytes, Free - {memory_info['free']} bytes")

if args.cpu:
    cpu_info = get_cpu_info()
    print(f"CPU Info: Model - {cpu_info['model']}, Physical Cores - {cpu_info['physical_cores']}, "
          f"Total Cores - {cpu_info['total_cores']}, Max Frequency - {cpu_info['max_frequency']} MHz")

if args.user:
    print(f"Current User: {get_current_user()}")

if args.load:
    load_avg = get_load_average()
    print(f"System Load Average: 1 min - {load_avg[0]}, 5 min - {load_avg[1]}, 15 min - {load_avg[2]}")

if args.ip:
    print(f"IP Address: {get_ip_address()}")

