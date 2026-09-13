#!/usr/bin/env python3

import random
import unittest
from unittest.mock import patch

from src.interleave import interleave


class TestInterleave(unittest.TestCase):

    def test_first(self):
        L1 = [1, 2, 3]
        L2 = [20, 30, 40]
        L3 = ['a', 'b', 'c']
        result = interleave(L1, L2, L3)
        self.assertIsInstance(
            result, list,
            msg=f"interleave should return a list. Got {type(result)}.")
        self.assertEqual(
            result, [1, 20, 'a', 2, 30, 'b', 3, 40, 'c'],
            msg="Incorrect result for input lists %s, %s, %s! Elements "
                "should be taken one at a time from each list in turn, not "
                "one whole list at a time." % (L1, L2, L3))

    def test_random(self):
        n = 4
        size = 50
        LL = []
        for _ in range(n):
            L = [random.randint(-100, 100) for _ in range(size)]
            LL.append(L)
        result = interleave(*LL)
        self.assertEqual(
            len(result), n * size,
            msg="Incorrect result list length!")
        for i in range(n):
            self.assertEqual(
                LL[i], result[i::n],
                msg="Input lists are not correctly interleaved!")

    def test_calls(self):
        L1 = [1, 2, 3]
        L2 = [20, 30, 40]
        L3 = ['a', 'b', 'c']
        with patch("builtins.zip", wraps=zip) as pzip:
            interleave(L1, L2, L3)
            pzip.assert_called_once()


if __name__ == '__main__':
    unittest.main()
