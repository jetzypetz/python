#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:17:41 2023

@author: eugenio.animali
"""

def average(numlist):
    return round(sum(numlist)/len(numlist),2)
    
    
def string_floats_to_list(s):
    return [float(x) for x in s.split()]



def student_data(d):
    return (d[:d.index(' ')], string_floats_to_list(d[d.index(' '):]))


def student_data_to_string(name, results):
    rstring = ''
    for i in results:
        rstring += ' ' + str(i)
    return f"{name}{rstring}"


def read_student_data(filename):
    newlist = []
    with open(filename) as f:
        linelist = f.readlines()
    for i in linelist:
        newlist.append(student_data(i))
    return newlist


def extract_averages(filename):
    newlist = []
    with open(filename) as f:
        linelist = f.readlines()
    for i in linelist:
        newlist.append((student_data(i)[0], average(student_data(i)[1])))
    return newlist


def discard_scores(numlist):
    numlist = numlist[2:]
    for j in range(2):
        lowest = numlist[0]
        for i in numlist:
            if i < lowest:
                lowest = i
        numlist.remove(lowest)
    return numlist


def summary_per_student(infilename, outfilename):
    newlist = []
    tavg = []
    with open(infilename) as f:
        linelist = f.readlines()
    for student_info in linelist:
        name = student_data(student_info)[0]
        scores = discard_scores(student_data(student_info)[1])
        scoresum = round(sum(scores),2)
        newlist.append(f'{student_data_to_string(name, scores)} sum: {scoresum}')
        tavg.append(scoresum)
    newlist.append(f'total average: {average(tavg)}')
    with open(outfilename, 'w') as f:
        for i in newlist:
            f.write(i + '\n')


def summary_per_tutorial(infilename, outfilename):
    newlist = []
    with open(infilename) as f:
        linelist = f.readlines()
    with open(outfilename, 'w') as f:
        for i in linelist:
            newlist.append(student_data(i)[1])
        for i in range(len(newlist[0])):
            tdresults = [x[i] for x in newlist]
            avg = average(tdresults)
            lowest = tdresults[0]
            for j in tdresults:
                if j < lowest:
                    lowest = j
            maximum = tdresults[0]
            for j in tdresults:
                if j > maximum:
                    maximum = j
            f.write(f'TD{i + 1}: average: {avg} min: {lowest} max: {maximum}\n')