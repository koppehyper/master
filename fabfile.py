#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import run, put, local, env, get, execute, settings, hide, task, abort
from fabric.colors import *

@task
def test_task():
    local('hostname')
    # abort('ERROR!!!! TEST FAILED!!!')
