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

import inspect
from trait_contexts import (NullContext,
                            ClassContext,
                            StaticFunctionContext,
                            ClassFunctionContext,
                            FunctionContext,
                            BoundMethodContext,
                            UnboundMethodContext,
                            PropertyContext)


class TraitTarget(object):
    """
    Creates context object as trait target.

    Supported extendable contexts:
        - class
    """
    def __new__(self, obj):
        if getattr(obj, '__module__', '') == 'builtins':
            return NullContext('Built-in objects can not be extended!')
        elif inspect.isroutine(obj):
            return NullContext('Function objects can not be extended')
        elif not isinstance(obj, type):
            return NullContext('Instances are not supported yet! Hold on!')
        elif inspect.isclass(obj):
            return ClassContext(obj)
        else:
            return PropertyContext(obj)


class TraitSource(object):
    """
    Creates context object as trait source

    Supported source contexts:
        - class
    """
    def __new__(self, obj):
        if getattr(obj, '__module__', '') == 'builtins':
            return NullContext('Built-in are not supported as traits!')
        elif inspect.ismethod(obj):
            if not obj.__self__:
                return UnboundMethodContext(obj)
            else:
                return BoundMethodContext(obj)
        elif inspect.isfunction(obj):
            try:
                mode = inspect.getargspec(obj)[0][0]

                if mode == 'self':
                    return FunctionContext(obj)
                elif mode == 'cls':
                    return ClassFunctionContext(classmethod(obj))
                else:
                    return StaticFunctionContext(staticmethod(obj))
            except IndexError:
                return StaticFunctionContext(staticmethod(obj))
        elif isinstance(obj, property):
            return NullContext('Properties are not supported yet directly! Use class instead!')
        elif not isinstance(obj, type):
            return NullContext('Instances are not supported yet! Hold on!')
        elif inspect.isclass(obj):
            return ClassContext(obj)
        else:
            return NullContext('Only classes and class instances can be extended')


if __name__ == '__main__':
    pass
