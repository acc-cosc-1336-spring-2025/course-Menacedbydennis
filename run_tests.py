import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
from tests.homework.c_decisions import test_decisions

suite = unittest.TestLoader().loadTestsFromModule(test_decisions)
