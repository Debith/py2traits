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

# In Python 3, we have single way to bind methods to class
if sys.version_info.major == 3:
    class MethodSource:
        def __init__(self, method, name=None):
            self._method = method
            self._name = name or method.__name__

        def for_class(self, clazz):
            # Rip out the original function from the class and set it also
            # as member of our new class.
            # TODO: Seems that we are getting wrong object type here. Need to work
            #       with factories to identify objects properly.
            try:
                clazz_function = self._method.__self__.__class__.__dict__[self._method.__name__]
                setattr(clazz, self._name, clazz_function)
            except:
                setattr(clazz, self._name, self._method)

        def for_instance(self, instance):
            try:
                clazz_function = self._method.__self__.__class__.__dict__[self._method.__name__]
                bound_method = clazz_function.__get__(instance, instance.__class__)
                instance.__dict__[self._name] = bound_method
            except:
                new_method = self._method.__get__(instance, instance.__class__)
                instance.__dict__[self._name] = new_method
else:
    class UnboundMethodSource:
        def __init__(self, method, name=None):
            self._method = method
            self._name = name or method.__name__

        def for_class(self, clazz):
            # For unbound methods, it is enough that we dig out the class function
            # and set it as a member of new class.
            clazz_function = self._method.im_class.__dict__[self._method.__name__]
            setattr(clazz, self._name, clazz_function)      

        def for_instance(self, instance):
            # For unbound methods, it is enough that we dig out the class function,
            # bind it to new instance and add it as a instance member.
            clazz_function = self._method.im_class.__dict__[self._method.__name__]
            bound_method = clazz_function.__get__(instance, instance.__class__)
            instance.__dict__[self._name] = bound_method

    class BoundMethodSource:
        def __init__(self, method, name=None):
            self._method = method
            self._name = name or method.__name__               

        def for_class(self, clazz):
            # Rip out the original function from the class and set it also
            # as member of our new class.
            clazz_function = self._method.__self__.__class__.__dict__[self._method.__name__]
            setattr(clazz, self._name, clazz_function)

        def for_instance(self, instance):
            clazz_function = self._method.__self__.__class__.__dict__[self._method.__name__]
            bound_method = clazz_function.__get__(instance, instance.__class__)
            instance.__dict__[self._name] = bound_method  
