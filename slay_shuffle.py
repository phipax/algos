#! /usr/bin/env python
import time
import sys
import random
import statistics

class SlayShuffle(object):
    median_list = []
    def __init__(self):
        pass

    def shuff_list(self,sample_list):
        for index,item in enumerate(sample_list):
            pos = random.randint(index,len(sample_list)-1)
            old_element = item
            if pos!=index:
                sample_list[index] = sample_list[pos]
                sample_list[pos] = old_element
            else:
                continue
        # print("final list: ",sample_list)

    def rev_list(self,sample_list):
        sample_list_new = ""
        # while(len(sample_list)>0):
        #     sample_list_new.append(sample_list.pop())
        for i in sample_list:
            if sample_list_new == "":
                sample_list_new = str(sample_list[i-1])
            else:
                sample_list_new = str(sample_list[i-1]) +","+sample_list_new
        sample_list = sample_list_new.split(",")
        # print(sample_list)


sla = SlayShuffle()
sample_u = []
sample_d = []
xx = int(sys.argv[1])

def prep_list(counter):
    SlayShuffle.median_list = []
    for num in range(0,counter):
        sample_u.append(num)
        sample_d.append(random.randint(0,counter))
    # print(len(sample_d),len(sample_u))

def formatter(count):
    endTime = round(statistics.median(SlayShuffle.median_list))
    etStr = '{message: >10}'.format(message=endTime)
    print('{message: >10}'.format(message=count),"\t",etStr)

# prep_list(xx)
# for i in range(0,50):
#     # print(sample_u)
#     stTime = time.time_ns()
#     sla.rev_list(sample_u)
#     SlayShuffle.median_list.append(time.time_ns()-stTime)
#     # print(SlayShuffle.median_list)
#     for num in range(0,xx):
#         sample_u.append(num)
# formatter(xx)

prep_list(xx)
for i in range(0,50):
    # print(sample_u)
    stTime = time.time_ns()
    sla.rev_list(sample_u)
    SlayShuffle.median_list.append(time.time_ns()-stTime)
    # print(SlayShuffle.median_list)
    # for num in range(0,xx):
    #     sample_d.append(random.randint(0,xx))
formatter(xx)

# prep_list(xx)
# for i in range(0,50):
#     stTime = time.time_ns()
#     sla.shuff_list(sample_u)
#     SlayShuffle.median_list.append(time.time_ns()-stTime)

# formatter(xx)
# prep_list(xx)

# for i in range(0,50):
#     stTime = time.time_ns()
#     sla.shuff_list(sample_d)
#     SlayShuffle.median_list.append(time.time_ns()-stTime)
# formatter(xx)


