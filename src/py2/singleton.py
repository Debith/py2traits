'''
Created on 8.2.2014

@author: teppo_000
'''

class Singleton(type):
    """
    Turn the class to immutable singleton.

    >>> class Example(object, metaclass=Singleton):
    ...     pass
    ...
    >>> a = Example()
    >>> b = Example()
    >>> id(a) == id(b)
    True

    Having your instance as a singleton is faster than creating from scratch
    >>> import timeit
    >>> class MySingleton(object, metaclass=Singleton):
    ...    def __init__(self):
    ...        self._store = dict(one=1, two=2, three=3, four=4)
    ...
    >>> class NonSingleton(object):
    ...    def __init__(self):
    ...        self._store = dict(one=1, two=2, three=3, four=4)
    ...
    >>> #timeit.timeit(NonSingleton) > timeit.timeit(MySingleton)
    True

    >>> MySingleton().new_item = False
    Traceback (most recent call last):
    ...
    NotImplementedError: Singletons are immutable
    """
    def __call__(self, *args, **kwargs):
        try:
            return self.__instance
        except AttributeError:
            def immutable_object(*args):
                raise NotImplementedError('Singletons are immutable')

            self.__instance = super(Singleton, self).__call__(*args, **kwargs)
            self.__setitem__ = immutable_object
            self.__setattr__ = immutable_object
            return self.__instance