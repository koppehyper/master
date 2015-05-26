#!/usr/bin/env python
# -*- coding: utf-8 -*-


memory = {}

def f(x):
    if str(x) in memory: return memory[str(x)]
    memory[str(x)] = (1 if x <= 1 else f(x-1)+f(x-2))
    return memory[str(x)]

print 'Deploy test!'

with open('output.data') as fp: output_data = fp.read()

print output_data

for x in range(0, 30):
    print "f(%d) = %d" % (x+1, f(x+1))


print 'Deploy end!'
