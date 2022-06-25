#!/bin/bash
sed -i "s/xssor.io/`echo $DOMAIN`/g" payload/probe.js
python3 manage.py runserver 0.0.0.0:8000