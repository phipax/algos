#! /usr/bin/env python
import time
import sys
import random
import statistics

median_val = []
dstr = ""

def prepareArray(cnt):
    prepared_array = []
    for i in range(cnt):
        prepared_array.append(i)
    return prepared_array

def callLast(larray):
    global median_val
    sysTime = time.time_ns()
    larray[-1]
    et = time.time_ns() - sysTime
    median_val.append(et)
    # print(median_val)

def callReverseArray(larray):
    global median_val
    sysTime = time.time_ns()
    larray.reverse()
    et = time.time_ns() - sysTime
    median_val.append(et)

def callShuffle(larray):
    global median_val
    sysTime = time.time_ns()
    random.shuffle(larray)
    et = time.time_ns() - sysTime
    median_val.append(et)

def callSortArray(larray):
    global median_val
    random.shuffle(larray)
    l1 = larray
    sysTime = time.time_ns()
    l1.sort()
    et = time.time_ns() - sysTime
    median_val.append(et)

def callSortArrayDsc(larray):
    global median_val
    random.shuffle(larray)
    l2 = larray
    sysTime = time.time_ns()
    l2.sort(reverse=True)
    et = time.time_ns() - sysTime
    median_val.append(et)

# def cusSort(larray):

def dump_data(tag,local_array):
    global median_val
    strLen = '{message: >10}'.format(message=str(len(local_array)))
    msg = '{message: <10}'.format(message=tag)
    endTime = round(statistics.median(median_val))
    etStr = '{message: <10}'.format(message=endTime)
    dstr = msg+","+strLen+","+etStr+"\n"
    # print(dstr)
    data.write(dstr)
    dstr=""
    median_val = []
    local_array = []

try:
    data = open("/Users/phipax/Projects/algos/chart.csv","at")
    local_array = []
    for par_var in sys.argv[1:]:
        local_array = prepareArray(int(par_var))
        for x in range(50):
            callLast(local_array)
        dump_data("LASTITEM",local_array)

    for par_var in sys.argv[1:]:
        local_array = prepareArray(int(par_var))
        for x in range(50):
            callReverseArray(local_array)
        dump_data("REVERSE",local_array)

    for par_var in sys.argv[1:]:
        local_array = prepareArray(int(par_var))
        for x in range(50):
            callShuffle(local_array)
        dump_data("SHUFFLE",local_array)

    for par_var in sys.argv[1:]:
        local_array = prepareArray(int(par_var))
        for x in range(50):
            callSortArray(local_array)
        dump_data("SORTASC",local_array)

    for par_var in sys.argv[1:]:
        local_array = prepareArray(int(par_var))
        for x in range(50):
            callSortArrayDsc(local_array)
        dump_data("SORTDSC",local_array)

finally:
    data.close()