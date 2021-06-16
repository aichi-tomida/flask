#! /home/aichitommy/.linuxbrew/bin/python3
# -*- coding: utf-8 -*-
from wsgiref.handlers import CGIHandler
from top import app

CGIHandler().run(app)