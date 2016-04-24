#!/usr/local/bin/python

import sys
import os

from jinja2 import Template

with open('./file.template', 'r') as file:
    template = file.read()

e=os.environ
e['value'] = 'foo'
e['KAFKA_START'] = 'monkey'
e['KAFKA_END'] = 'bar'
e['KAFKA_MID'] = 'poo'
print e

print Template(template).render(env=e)

sys.exit(0);