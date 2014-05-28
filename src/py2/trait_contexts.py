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
import binders


class NullContext(object):
    """
    Null context for invalid cases.
    """
    def __init__(self, extra_message):
        self._extra_message = extra_message

    def __str__(self):
        return "null"

    @property
    def error_message(self):
        return self._extra_message

    def __nonzero__(self):
        return False


class ClassContext(object):
    """
    Class context for class objects.

    This class encapsulates behavior for handling classes as trait source
    and target.
    """
    def __init__(self, clazz):
        self._class = clazz

    def __str__(self):
        return "class"

    def __iter__(self):
        for name, obj in vars(self._class).items():
            if isinstance(obj, staticmethod):
                yield FunctionContext(obj)
            elif isinstance(obj, classmethod):
                yield FunctionContext(obj)
            elif isinstance(obj, property):
                yield PropertyContext(obj, name)
            elif inspect.ismethoddescriptor(obj):
                yield UnboundMethodContext(obj)
            else:
                obj_via_getattr = getattr(self._class, name)
                if (inspect.isfunction(obj_via_getattr) or
                    inspect.ismethoddescriptor(obj_via_getattr)):
                    yield UnboundMethodContext(obj)

    @property
    def name(self):
        return self._class.__name__

    @property
    def as_target(self):
        return self._class

    def __nonzero__(self):
        return True


class InstanceContext(object):
    """
    Class context for class objects.

    This class encapsulates behavior for handling classes as trait source
    and target.
    """
    def __init__(self, clazz):
        self._class = clazz

    def __str__(self):
        return "instance"

    def __iter__(self):
        for name, obj in vars(self._class).items():
            if isinstance(obj, staticmethod):
                yield FunctionContext(obj)
            elif isinstance(obj, classmethod):
                yield FunctionContext(obj)
            elif isinstance(obj, property):
                yield PropertyContext(obj, name)
            elif inspect.ismethoddescriptor(obj):
                yield BoundMethodContext(obj)
            else:
                obj_via_getattr = getattr(self._class, name)
                if (inspect.isfunction(obj_via_getattr) or
                    inspect.ismethoddescriptor(obj_via_getattr)):
                    yield BoundMethodContext(obj)

    @property
    def name(self):
        return self._class.__name__

    @property
    def as_target(self):
        return self._class

    def __nonzero__(self):
        return True


class BoundMethodContext(object):
    def __init__(self, method):
        self._method = method

    def __str__(self):
        return "bound method"

    @property
    def name(self):
        return self._method.__name__

    @property
    def as_trait(self):
        return self._method

    @property
    def as_target(self):
        raise NotImplementedError("Cannot be a trait target!")


class UnboundMethodContext(object):
    def __init__(self, method):
        self._method = method

    def __str__(self):
        return "unbound method"

    @property
    def name(self):
        return self._method.__name__

    @property
    def as_trait(self):
        return self._method

    @property
    def as_target(self):
        raise NotImplementedError("Cannot be a trait target!")


class FunctionContext(object):
    def __init__(self, function):
        self._function = function

    def __str__(self):
        return "function"

    def __nonzero__(self):
        return True

    @property
    def name(self):
        return self._function._name

    @property
    def as_trait(self):
        return self._function

    @property
    def as_target(self):
        raise NotImplementedError("Cannot be a trait target!")


class PropertyContext(object):
    def __init__(self, prop, name):
        self._property = prop
        self._name = name

    def __str__(self):
        return "property"

    def __nonzero__(self):
        return True

    @property
    def name(self):
        return self._name

    @property
    def as_trait(self):
        return self._property

    @property
    def as_target(self):
        raise NotImplementedError("Cannot be a trait target!")
