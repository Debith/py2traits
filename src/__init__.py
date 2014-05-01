import sys

if sys.version_info.major == 3:
    from .py3 import combine_class, add_traits, extendable, Singleton, NestedDict
else:
    from py2 import combine_class, add_traits, extendable, Singleton, NestedDict
    
del sys