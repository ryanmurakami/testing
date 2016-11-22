#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import pystache

with open('out/index.csv') as index:
  index_csv = filter(lambda line: line, index.read().split('\n'))

items = []

for line in reversed(index_csv):
    jscov, cxxcov, date, sha = line.split(',')
    jscov = round(float(jscov), 2)
    cxxcov = round(float(cxxcov), 2)
    date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%fZ').strftime("%d/%m/%Y %H:%M")
    items.append({ 'date': date, 'sha': sha, 'jscov': jscov, 'cxxcov': cxxcov })

template = open('index.mustache').read()

rendered = pystache.render(template, { 'items': items })

open('out/index.html', 'w').write(rendered)
