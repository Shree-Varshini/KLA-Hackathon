# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 09:31:40 2022

@author: rpshr
"""

import yaml
from yaml.loader import SafeLoader

import time

def type_task(function,ips):
    print('task')
    if function == 'TimeFunction':
        time.sleep(int(ips['ExecutionTime']))
    
def type_flow(execution,activities):
    print('flow')
    main_keys = list(activities.keys())

    for i in range(len(main_keys)):
        parameters = list(activities[main_keys[i]].keys())   
        #print(parameters)
        if activities[main_keys[i]][parameters[0]] == 'Task':
            type_task(activities[main_keys[i]][parameters[1]],activities[main_keys[i]][parameters[2]])
        elif activities[main_keys[i]][parameters[0]] == 'Flow':
            type_flow(activities[main_keys[i]][parameters[1]],activities[main_keys[i]][parameters[2]])
      
# Open the file and load the file
with open(r'Milestone1\Milestone1A.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    main_keys = list(data.keys())
    parameters = list(data[main_keys[0]].keys())
    if data[main_keys[0]][parameters[0]] == 'Flow':
        type_flow(data[main_keys[0]][parameters[1]],data[main_keys[0]][parameters[2]])