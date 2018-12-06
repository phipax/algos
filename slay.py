#! /usr/bin/env python
import time
import sys
import random
import statistics

class Slay(object):
    median_list = []
    def __init__(self):
        pass

    def ch_dup(self,sample_list,mode):
        
        if mode == "uf":
            if (len(sample_list) <= 0):
                return "Empty List"
            else:
                stTime = time.time_ns()
                for item in sample_list:
                    if(sample_list.count(item)>1):
                        # print("(User Method using for loop) Duplicate found in : ",str(time.time_ns()-stTime)," Nano Secs")
                        Slay.median_list.append(time.time_ns()-stTime)
                        return True
                    else:
                        # print("(User Method using for loop) Duplicate Not Found in : ",str(time.time_ns()-stTime)," Nano Secs")
                        Slay.median_list.append(time.time_ns()-stTime)
                        return False
        elif mode == "uw":
            if (len(sample_list) <= 0):
                return "Empty List"
            else:
                stTime = time.time_ns()
                while (len(sample_list)>0):
                    item = sample_list.pop()
                    if item in sample_list:
                        # print("(User Method using while loop) Duplicate found in : ",str(time.time_ns()-stTime)," Nano Secs")
                        Slay.median_list.append(time.time_ns()-stTime)
                        return True
                else:
                    # print("(User Method using while loop) Duplicate Not Found in : ",str(time.time_ns()-stTime)," Nano Secs")
                    Slay.median_list.append(time.time_ns()-stTime)
                    return False
        elif mode == "s":
            if(len(sample_list)>0):
                new_list = set(sample_list)
                stTime = time.time_ns()
                if(len(sample_list) == len(new_list)):
                    # print("(System Method using set([list])) Duplicate Not Found in : ",str(time.time_ns()-stTime)," Nano Secs")
                    Slay.median_list.append(time.time_ns()-stTime)
                    return False
                else:
                    # print("(System Method using set([list])) Duplicate found in : ",str(time.time_ns()-stTime)," Nano Secs")
                    Slay.median_list.append(time.time_ns()-stTime)
                    return True
            else:
                return "Empty List"
        else:
            return "Invalid Mode"

    def formatter(self,count,str_1,str_2):
        endTime = round(statistics.median(Slay.median_list))
        etStr = '{message: >10}'.format(message=endTime)
        print('{message: >10}'.format(message=count),"\t",'{message: >10}'.format(message=str_1),"\t",'{message: >10}'.format(message=str_2),"\t",etStr)


sla = Slay()
sample_u = []
sample_d = []
xx = int(sys.argv[1])

def prep_list(counter):
    Slay.median_list = []
    for num in range(0,counter):
        sample_u.append(num)
        sample_d.append(random.randint(0,counter))

for num in range(0,xx):
    sample_u.append(num)
    sample_d.append(random.randint(0,xx))

for i in range(0,50):
    sla.ch_dup(sample_d,"uw")
sla.formatter(xx,"Random List","WHILE")
prep_list(xx)


for i in range(0,50):
    sla.ch_dup(sample_d,"uf")
sla.formatter(xx,"Random List","FOR")
prep_list(xx)

for i in range(0,50):
    sla.ch_dup(sample_d,"s")
sla.formatter(xx,"Random List","SET")
prep_list(xx)

for i in range(0,50):
    sla.ch_dup(sample_u,"uw")
sla.formatter(xx,"Uniform List","WHILE")
prep_list(xx)

for i in range(0,50):
    sla.ch_dup(sample_u,"uf")
sla.formatter(xx,"Uniform List","FOR")
prep_list(xx)

for i in range(0,50):
    sla.ch_dup(sample_u,"s")
sla.formatter(xx,"Uniform List","SET")
prep_list(xx)