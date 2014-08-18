#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
'''
   Copyright 2014 Teppo Perä

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

import os
import sys

try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO

write_screen = sys.stdout
sys.stdout = StringIO()

ROOT = os.path.dirname(__file__)

for filename in os.listdir(ROOT):
    if filename.startswith('_'):
        continue
    
    write_screen.write(filename + ' ... ')
    
    with open(filename, 'r') as fp:
        exec(fp.read())        
        
    msg = sys.stdout.read()
    if not len(msg):
        write_screen.write('OK\n')
    
write_screen.write("\nFinished: %d " % (len(os.listdir(ROOT)) - 1) + "examples run.\n\n")