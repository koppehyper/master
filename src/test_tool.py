#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('setting.conf') as s: lines = s.read()


is_setting_ok = 'OK' in lines

if is_setting_ok:
    print 'Test passed!'
else:
    print 'Test FAILED!!!'

exit(0 if is_setting_ok else 1)
