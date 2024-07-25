#!/usr/bin/env python3.12

import argparse

parser = argparse.ArgumentParser(description='This is an access log file parser')

parser.add_argument('file', type=str, help='The access log file to parse')

args = parser.parse_args()

user_agents = {}

with open(args.file) as f:
    f.readline()
    for line in f:
        user_agent = line.split('"')[5]
        if user_agent in user_agents:
            user_agents[user_agent] += 1 
        elif user_agent != "-":
            user_agents[user_agent] = 1
    
for user_agent, count in user_agents.items():    
    print(f'{user_agent}: {count}')

print(f'User Agents count: {len(user_agents.values())}')
