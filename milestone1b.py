# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 12:05:41 2022

@author: rpshr
"""

import yaml
from yaml.loader import SafeLoader

import time
import threading
from datetime import datetime

def log_file(remark):
    string = str(datetime.now()) +';'+remark+'\n'
    f = open('log1b.txt', "a")
    f.write(string)
    f.close()
    
def type_task(remark,function,ips):
    if function == 'TimeFunction':
        remark = remark + ' ' + function + ' ' + '('+(ips['FunctionInput'])+', '+ips['ExecutionTime'] +')'
        log_file(remark)
        time.sleep(int(ips['ExecutionTime']))
    
def type_flow(flow,execution,activities):
    main_keys = list(activities.keys())
    if execution == 'Sequential':        
        for i in range(len(main_keys)):
            log_file(flow+'.'+main_keys[i] + ' Entry')
            parameters = list(activities[main_keys[i]].keys())   
            if activities[main_keys[i]][parameters[0]] == 'Task':
                remark = flow + '.' + main_keys[i] + ' Executing' 
                type_task(remark,activities[main_keys[i]][parameters[1]],activities[main_keys[i]][parameters[2]])
                log_file(flow+'.'+main_keys[i] + ' Exit')
                
            elif activities[main_keys[i]][parameters[0]] == 'Flow':
                type_flow(flow+'.'+main_keys[i],activities[main_keys[i]][parameters[1]],activities[main_keys[i]][parameters[2]])
                log_file(flow+'.'+main_keys[i] + ' Exit')
    
    elif execution == 'Concurrent':
        t,count,x = [],[],0
        for i in range(len(main_keys)):
            log_file(flow+'.'+ main_keys[i] + ' Entry')
            parameters = list(activities[main_keys[i]].keys()) 
            if activities[main_keys[i]][parameters[0]] == 'Task':
                temp = (threading.Thread(target=type_task,args=(flow + '.' + main_keys[i] + ' Executing',activities[main_keys[i]][parameters[1]],activities[main_keys[i]][parameters[2]])))
                count.append(i)
                t.append(temp)
            elif activities[main_keys[i]][parameters[0]] == 'Flow':
                type_flow(flow+'.'+main_keys[i],activities[main_keys[i]][parameters[1]],activities[main_keys[i]][parameters[2]])
                log_file(flow+'.'+main_keys[i] + ' Exit')  
            
        for thread in t:
            thread.start()
        for thread in t:
            thread.join()
            log_file(flow+'.'+main_keys[count[x]] + ' Exit')
            x += 1
                  
      
# Open the file and load the file
with open(r"C:\Users\rpshr\Desktop\kla hackathon\Milestone1\Milestone1B.yaml") as f:
    data = yaml.load(f, Loader=SafeLoader)
    main_keys = list(data.keys())
    log_file(main_keys[0] + ' Entry')
    parameters = list(data[main_keys[0]].keys())
    if data[main_keys[0]][parameters[0]] == 'Flow':
        type_flow(main_keys[0],data[main_keys[0]][parameters[1]],data[main_keys[0]][parameters[2]])
        log_file(main_keys[0] + ' Exit')