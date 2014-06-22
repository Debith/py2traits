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


class TraitContext(object):
    """
    Common interface for trait contexes
    """
    def __str__(self):
        return self.BINDER_ID
    
    def __nonzero__(self):
        return self.VALID
    
    @property
    def name(self):
        return self._name

    @property
    def as_trait(self):
        return self._source
    
    @property
    def as_target(self):
        return self._target


class NullContext(TraitContext):
    """
    Null context for invalid cases.
    """
    BINDER_ID = 'null'
    VALID = False
    
    def __init__(self, extra_message):
        print "PyTraits: NullContext:", extra_message
        self._extra_message = extra_message

    @property
    def error_message(self):
        return self._extra_message


class ClassContext(TraitContext):
    """
    Class context for class objects.

    This class encapsulates behavior for handling classes as trait source
    and target.
    """
    BINDER_ID = 'class'
    VALID = True
 
    def __init__(self, clazz):
        self._source = clazz
        self._target = clazz
        self._name = clazz.__name__

    def __iter__(self):
        for name, obj in vars(self._source).items():
            if isinstance(obj, staticmethod):
                yield DecoratedFunctionContext(obj)
            elif isinstance(obj, classmethod):
                yield DecoratedFunctionContext(obj)
            elif isinstance(obj, property):
                yield PropertyContext(obj, name)
            elif inspect.ismethoddescriptor(obj):
                yield UnboundMethodContext(obj)
            else:
                obj_via_getattr = getattr(self._source, name)
                if (inspect.ismethod(obj_via_getattr) or
                    inspect.ismethoddescriptor(obj_via_getattr)):
                    yield UnboundMethodContext(obj_via_getattr)


class InstanceContext(TraitContext):
    """
    Class context for class objects.

    This class encapsulates behavior for handling classes as trait source
    and target.
    """
    BINDER_ID = 'instance'
    VALID = True
    
    def __init__(self, instance):
        self._source = instance
        self._target = instance
        self._name = instance.__class__.__name__


class BoundMethodContext(TraitContext):
    BINDER_ID = 'bound method'
    VALID = True
    
    def __init__(self, bound_method):
        self._source = bound_method
        self._target = None
        self._name = bound_method.__name__


class UnboundMethodContext(TraitContext):
    BINDER_ID = 'unbound method'
    VALID = True
    
    def __init__(self, unbound_method):
        self._source = unbound_method
        self._target = None
        self._name = unbound_method.__name__
        

class DecoratedFunctionContext(TraitContext):
    BINDER_ID = 'function'
    VALID = True
    
    def __init__(self, function):
        self._source = function
        self._target = None
        self._name = function.__func__.__name__


class FunctionContext(TraitContext):
    BINDER_ID = 'function'
    VALID = True
    
    def __init__(self, function):
        self._source = function
        self._target = None
        self._name = function.__name__


class PropertyContext(TraitContext):
    BINDER_ID = 'property'
    VALID = True
    
    def __init__(self, prop, name):
        self._source = prop
        self._target = None
        self._name = name
