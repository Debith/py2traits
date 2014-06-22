#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

from pytraits import add_traits


class ExampleClass(object):
    pass


class ExampleTrait(object):
    def trait_method(self):
        return 42


# Combine an instance with other instance.
example_instance = ExampleClass()
my_trait_instance = ExampleTrait()
add_traits(example_instance, my_trait_instance.trait_method)

assert hasattr(example_instance, 'trait_method'), "Method must be found from the instance"
assert not hasattr(ExampleClass, 'trait_method'), "Method must not found from the class!"
assert not issubclass(ExampleClass, ExampleTrait)
assert example_instance.trait_method() == 42, "composition incomplete"

