from unittest import TestSuite, TextTestRunner

from tests.test_sample import TestSample

def suite() -> TestSuite:

    suite = TestSuite()
    suite.addTest(TestSample())
    return suite

if __name__ == '__main__':
    runner = TextTestRunner()
    runner.run(suite())