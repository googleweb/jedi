#!/usr/bin/env python
import os
import sys
import unittest

os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
sys.path.append('.')

import functions
#functions.set_debug_function(functions.debug.print_to_stdout)


class TestRegression(unittest.TestCase):
    def get_def(self, src, pos):
        return functions.get_definition(src, pos[0], pos[1], '')

    def test_get_definition_cursor(self):

        s = ("class A():\n"
             "    def _something(self):\n"
             "        return\n"
             "    def different_line(self,\n"
             "                   b):\n"
             "        return\n"
             "A._something\n"
             "A.different_line"
             )


        in_name = 2, 9
        under_score = 2, 8
        cls = 2, 7
        should1 = 7, 10
        diff_line = 4, 10
        should2 = 8, 10

        get_def = lambda pos: [d.description for d in self.get_def(s, pos)]
        in_name = get_def(in_name)
        under_score = get_def(under_score)
        should1 = get_def(should1)
        should2 = get_def(should2)

        diff_line = get_def(diff_line)

        assert should1 == in_name
        assert should1 == under_score

        #print should2, diff_line
        assert should2 == diff_line

        self.assertRaises(functions.NotFoundError, get_def, cls)


if __name__ == '__main__':
    unittest.main()
