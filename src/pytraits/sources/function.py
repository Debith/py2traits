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

class FunctionSource:
    """
    Encapsulate Python module level function into a class.
    """
    def __init__(self, function, name = None):
        self._function = function
        self._name = name

    @property
    def function_name(self):
        """
        Retrieves name of the function.

        >>> def example_function(anything):
        ...     pass
        ...
        >>> source = FunctionSource(example_function)
        >>> source.function_name
        'example_function'

        >>> source = FunctionSource(example_function, "custom_name")
        >>> source.function_name
        'custom_name'
        """
        return self._name or self._function.__name__

    def for_class(self, clazz):
        setattr(clazz, self.function_name, self._function)

    def for_instance(self, instance):
        # Functions are always descriptors. To bind function to instance,
        # we need to invoke descriptor through its __get__, providing
        # target instance as a new owner for this function descriptor.
        # This creates a clone of the function with its new master. After
        # that this new function is assigned as a part of the instance's dict.
        #
        # See more: http://users.rcn.com/python/download/Descriptor.htm
        new_function = self._function.__get__(instance, instance.__class__)
        instance.__dict__[self.function_name] = new_function

if __name__  == "__main__":
    import doctest
    doctest.testmod()