#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Filip Stefanak <f.stefanak@rare-technologies.com>
# Copyright (C) 2017 Rare Technologies
#
# This code is distributed under the terms and conditions
# from the MIT License (MIT).

import unittest

from bounter import HashTable


class HashTableInitTest(unittest.TestCase):
    def test_buckets_init(self):
        """
        Test that the table initializes itself with the number of buckets equal to the greatest power of 2 lower than the argument
        """
        self.assertEqual(HashTable(4).buckets(), 4)
        self.assertEqual(HashTable(5).buckets(), 4)
        self.assertEqual(HashTable(16).buckets(), 16)
        self.assertEqual(HashTable(17).buckets(), 16)
        self.assertEqual(HashTable(31).buckets(), 16)
        self.assertEqual(HashTable(2 ** 16 - 1).buckets(), 2 ** 15)
        self.assertEqual(HashTable(2 ** 16).buckets(), 2 ** 16)
        self.assertEqual(HashTable(2 ** 24 - 1).buckets(), 2 ** 23)

    def test_invalid_buckets_init(self):
        """
        Negative test for initialization with too few buckets
        """
        for invalid_bucket_count in [0, 1, 2, 3, -3, 2 ** 32]:
            with self.assertRaises(ValueError,
                                   msg=("Constructor should throw ValueError for count %d" % invalid_bucket_count)):
                HashTable(invalid_bucket_count)


if __name__ == '__main__':
    unittest.main()
