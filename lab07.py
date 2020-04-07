#!/usr/bin/env python
"""
CMPS 3500 
Lab07
date: 4/4/20
username:mmercado
name: Ma Mikaela Mercado
description: lab07.py

Execute with:

     ./lab07.py lab07.data

lab07.data is structured like this:

      10
      15
      20
      0
      17
"""
import sys
from sys import argv

"""  
my_map takes a function and a list, and returns the result of the
function applied to the every element in the list; e.g.,

    my_map(lambda x: x + 1, [1, 2, 3]) 

returns [2, 3, 4]
"""

def my_map(func, list):
    new_list = []
    for item in list:
        new_list.append(func(item))
    return new_list

def my_mean(list):
    return sum(list)/len(list) 

"""
PART II COROUTINES
"""
def printjob(name):
    task,jobID = name
    sys.stdout.write(task + ',' + str(jobID) + ' ')

def consumer(jobs):
    print "Consumer starting."
    i = -1 
   # as long as something is in the jobs list keep processing requests
    while jobs:
        i = (i + 1) % len(jobs)
      # yield passes control back to producer with the ith job name
        getRequest = yield jobs[i]    # waits for request from producer
        if getRequest:    # if getRequest is not empty process it
            request, name, jobID = getRequest
            if request == "add":
                jobs.append((name, jobID))
                sys.stdout.write("\nADD ") 
            elif request == "remove":
                del jobs[[y[0] for y in jobs].index(name)]
                buf = "\nREMOVE " + name + "\n"
                sys.stdout.write(buf)

    print "\nNo jobs left to do!\n"

def producer(jobs):
    print "Producer starting."
    con = consumer(jobs)                   # start the consumer 

    buf = "Initial job list (" + str(len(jobs)) + "): "
    sys.stdout.write(buf)
    for i in range(len(jobs)): 
        printjob(con.next())            # next sends job to consumer w/ no msg 

    printjob(con.send(("add", "iron", 44)))  # send sends job to consumer w/ msg
    sys.stdout.write("\n")
    for i in range(len(jobs)): 
        printjob(con.next())               

    printjob(con.send(("add", "mend", 55)))   
    sys.stdout.write("\n")
    for i in range(len(jobs)): 
        printjob(con.next())               

    con.send(("remove","fold", 33))         
    for i in range(len(jobs)): 
        printjob(con.next())

    con.send(("remove","wash", 11))
    for i in range(len(jobs)): 
        printjob(con.next())

    print "\nProducer Done." 


if len(argv) < 2:
    print "Usage: %s <filename>" % argv[0]
else:
    input = file(argv[1])
    values = []
    for line in input:
        values.append(int(line))

print "PART I"
print "original list:", values 

odds = filter(lambda x: x % 2 != 0, values)
print "odds: ", odds

evens = filter(lambda x: x % 2 == 0, values)
print "evens: ", evens

squared = my_map(lambda x: x * x, values)
print "squared:", squared

successor = my_map(lambda x: x + 1, values)
print "successor:", successor

avg = filter(lambda x: x>0, values)
print "mean: ", my_mean(avg)

print "PART II"
n = int(raw_input("Cmdline arg: "))
jobs = [("wash", 11+n),("dry",22+n),("fold",33+n)]
producer(jobs)
