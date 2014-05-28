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

import unittest

from pytraits import NestedDict as ndict
from utils import examples, print_details

print_details()


class TestNestedDict(unittest.TestCase):
    def test_can_be_set_item_using_normal_dictionary_access(self):
        my_dict = ndict()
        my_dict['a']['b']['d'] = 5

        self.assertEqual(my_dict['a']['b']['d'], 5)
        self.assertEqual(my_dict['a', 'b', 'd'], 5)

    def test_can_be_set_item_using_list_of_keys(self):
        my_dict = ndict()
        my_dict['f', 'g', 'h'] = 42

        self.assertEqual(my_dict['f']['g']['h'], 42)
        self.assertEqual(my_dict['f', 'g', 'h'], 42)

    def test_can_be_iterated_on_leaf_level(self):
        my_dict = ndict()
        my_dict['a'] = 1
        my_dict['b', 'c'] = 2
        my_dict['b', 'd'] = 3
        my_dict['e', 'f', 'g'] = 4
        my_dict['h', 'i', 'j'] = 5
        my_dict['h', 'k', 'l'] = 6

        self.assertEqual(list(my_dict.items()), [(('a',), 1),
                                                 (('b', 'c'), 2),
                                                 (('b', 'd'), 3),
                                                 (('e', 'f', 'g'), 4),
                                                 (('h', 'i', 'j'), 5),
                                                 (('h', 'k', 'l'), 6)])

    def test_does_not_support_values_and_dictionaries_for_same_key(self):
        my_dict = ndict()
        my_dict['a'] = 1

        with self.assertRaisesRegexp(Exception, "Not possible to assign a key"):
            my_dict['a', 'b'] = 2

    def test_can_be_created_using_list_of_keys(self):
        my_dict = ndict([(('a', 'b', 'c'), 1),
                         (('d', 'e', 'f'), 2)])

        self.assertEqual(my_dict['a']['b']['c'], 1)
        self.assertEqual(my_dict['d', 'e', 'f'], 2)

    def test_can_be_one_level_deep(self):
        my_dict = ndict(depth=1, leaf_type=list)
        my_dict[1].append('value')
        my_dict[1].append(True)

        self.assertEquals(my_dict[1], ['value', True])

    def test_supports_leaf_to_be_dictionary(self):
        my_dict = ndict(depth=1, leaf_type=dict)
        my_dict[1][1] = 'a'
        my_dict[1][2] = 'b'

        self.assertEquals(my_dict[1][1], 'a')
        self.assertEquals(my_dict[1][2], 'b')

    def test_can_contain_multiple_levels(self):
        my_dict = ndict(depth=3, leaf_type=int)
        my_dict[1, 2, 3] += 4
        my_dict[1, 2, 3] += 12

        self.assertEquals(my_dict[1, 2, 3], 16)

    @examples(('a',       ndict(), "NestedDict([(('a',), NestedDict())])"),
            ((('a', 'b'), ndict(), "NestedDict([(('a', 'b'), NestedDict())])")),
            ((('a', 'b'), True,   "NestedDict([(('a', 'b'), True)])")))
    def test_repr_with_levels(self, key, value, representation):
        my_dict = ndict()
        my_dict[key] = value
        self.assertEqual(repr(my_dict), representation)

    @examples(((1, 2, 3),    True, [(1, 2, 3)]),
              ((2, 3, 4),    None, [(2, 3, 4)]),
              ((3, 4, 5),      {}, [(3, 4, 5)]),
              ((4, 5, 6),      [], [(4, 5, 6)]),
              ((5, 6, 7), ndict(), [(5, 6, 7)]))
    def test_shows_keys_properly_for_empty_values(self, key, value, keys):
        my_dict = ndict()
        my_dict[key] = value

        self.assertEqual(list(my_dict.keys()), keys)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
