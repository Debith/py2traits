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

import sys
import inspect

# TODO: Improve this by making sources to register themselves somehow. 
from .clazz import ClassSource
from .instance import InstanceSource
from .function import FunctionSource
from .decorated import DecoratedFunctionSource
from .method import *
from .prop import PropertySource

class TraitSource(object):
    """
    Creates trait source object.
    """
    def __new__(self, obj):
        if getattr(obj, '__module__', '') == 'builtins':
            return InvalidSource('Built-in objects can not used as traits!')
        elif inspect.ismethod(obj):
            if sys.version_info.major == 3:
                return MethodSource(obj)
            else:
                if obj.__self__:
                    return BoundMethodSource(obj)
                else:
                    return UnboundMethodSource(obj)

        elif inspect.isroutine(obj):
            try:
                first_arg = inspect.getargspec(obj)[0][0]
            except IndexError:
                first_arg = ""

            if first_arg == 'self':
                return FunctionSource(obj)
            elif first_arg == 'cls':
                return DecoratedFunctionSource(classmethod(obj))
            else: # static
                return DecoratedFunctionSource(staticmethod(obj))
        elif inspect.isdatadescriptor(obj):
            return PropertySource(obj)
        elif not isinstance(obj, type):
            return InstanceSource(obj)
        elif inspect.isclass(obj):
            return ClassSource(obj)
        else:
            return InvalidSource('Properties can not be extended!')