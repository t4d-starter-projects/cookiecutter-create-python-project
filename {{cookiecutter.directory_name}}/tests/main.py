import unittest

from tests.test_sample import TestSample

def suite():

    suite = unittest.TestSuite()
    suite.addTest(TestSample())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())