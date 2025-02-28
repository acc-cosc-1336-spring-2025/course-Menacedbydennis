import unittest

the files in /test/homework/b_in_proc_out/test_in_proc_out
has the test function

from test.homework.e_functions import test_functions 

suite = unittest.TestLoader().loadTestsFromModule(test_functions)
unittest.TextTestRunner(verbosity=2).run(suite)
