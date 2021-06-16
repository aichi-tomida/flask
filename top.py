#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# システム
import os
# 日付
import time
import datetime
# datetime
from datetime import datetime as dtime
# pathlib
import pathlib

from flask import Flask, render_template , redirect, request

app = Flask(__name__)

indexpage = './index.html'

# アクセス日時を表示する
displaydate = datetime.datetime.now()

@app.route('/')
def index():
  return render_template(indexpage , displaydate=displaydate)

if __name__ == '__main__':
  app.run()
