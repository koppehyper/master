#!/usr/bin/env python
# -*- coding: utf-8 -*-

def f(x):
    return 1 if x <= 1 else f(x-1) + f(x-2)

print 'Deploy test!'
for x in range(1, 30):
    print "f(%d) = %d" % (x, f(x))

print 'Deploy end!'
