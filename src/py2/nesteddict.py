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

try:
    from collections import OrderedDict as odict
except ImportError:
    # Only Python 2.7 supports OrderedDict. NestedDict kind of supports
    # older versions, but naturally ORDER CANNOT BE GUARANTEED!
    odict = dict

from errors import InvalidAssignmentError


def _is_container(obj):
    """
    Checks whether the object is container or not.

    Container is considered an object, which includes other objects,
    thus string is not qualified, even it implments iterator protocol.
    """
    if isinstance(obj, str):
        return False

    return getattr(obj, '__iter__', False)


def _has_dict_protocol(obj):
    """
    Checks whether object supports dict protocl.
    """
    return hasattr(obj, "__getitem__") and hasattr(obj, "__setitem__")


class NestedDict(odict):
    """
    Nested dictionary with support of maximum depth with default type.
    """
    def __init__(self, *items, **kwargs):
        depth = kwargs.get('depth', None)
        leaf_type = kwargs.get('leaf_type', list)
        assert depth is None or isinstance(depth, int) and depth > 0

        self.__depth = depth
        self.__leaf_type = leaf_type
        super(NestedDict, self).__init__(*items)

    def __next_level(self, key):
        try:
            # In case key exists, simply return it.
            return super(NestedDict, self).__getitem__(key)
        except KeyError:
            # Okay, there is no key. Need to do it hard way.
            if self.__depth == None:
                # Undefined depth means that depth is infinite, thus
                # and new nested dict after another.
                next_level = NestedDict()
            elif self.__depth > 1:
                next_level = NestedDict(depth=self.__depth - 1,
                                        leaf_type=self.__leaf_type)
            else:
                next_level = self.__leaf_type()

            super(NestedDict, self).__setitem__(key, next_level)
            return next_level

    def __build_sequence(self, node, key):
        leaf = self
        part = key

        # This allows us to use any iterable as a key to nested dict.
        if _is_container(key):
            assert not self.__depth or len(key) <= self.__depth

            for part in key[:-1]:
                leaf = leaf.__next_level(part)
            part = key[-1]

        if not _has_dict_protocol(leaf):
            raise InvalidAssignmentError

        return part, leaf

    def __iter__(self):
        """
        Iterates dictionary's leaf objects.

        >>> my_dict = NestedDict([((1, 2, 3, 4, 5), True),
        ...                       ((1, 2, 3, 4, 6), False)])
        >>> keys = list(my_dict)
        >>> keys[0]
        (1, 2, 3, 4, 5)

        >>> keys[1]
        (1, 2, 3, 4, 6)
        """
        for key in super(NestedDict, self).__iter__():
            next_level = super(NestedDict, self).__getitem__(key)
            if isinstance(next_level, NestedDict):
                # Need to yield key when next level dictionary is empty.
                if not len(next_level):
                    yield key,

                # if there is more sub-items, create a one tuple key
                # out of it. That way the keys are more handy to use.
                for next_key in next_level:
                    yield tuple((key,)) + next_key
            else:
                yield key,

    def __setitem__(self, key, value):
        """
        Assigns new value to nested dict.

        Works as normal dictionary access or chained access
        from iterable keys.

        Example:
        >>> my_dict = NestedDict([((1, 2, 3, 4, 5), True)])
        >>> my_dict[1, 2, 3, 4, 5] = False
        >>> my_dict[1, 2, 3, 4, 5]
        False

        >>> my_dict[1][2][3][4][5] = True
        >>> my_dict[1, 2, 3, 4, 5]
        True
        """
        key, leaf = self.__build_sequence(self, key)
        super(NestedDict, leaf).__setitem__(key, value)

    def __getitem__(self, key):
        """
        Retrieves item from the nested dict.

        Works as normal dictionary access or chained access
        from iterable keys. If depth is not specified, it is
        considered infinite.

        Example:
        >>> my_dict = NestedDict([((1, 2, 3, 4, 5), True)])
        >>> my_dict[1, 2, 3, 4, 5]
        True

        >>> my_dict[1][2][3][4][5]
        True
        """
        key, leaf = self.__build_sequence(self, key)
        return leaf.__next_level(key)

    def __repr__(self):
        """
        Returns string to instantinate similar object.
        """
        if not len(self):
            return "NestedDict()"

        args = []
        for key, value in self.items():
            args.append("(%s, %s)" % (key, repr(value)))

        return "NestedDict([%s])" % ", ".join(args)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
