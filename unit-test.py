import unittest
import test_jenkins


class MyFunTest(unittest.TestCase):

    def test_positive(self):
        self.assertEquals(myFun(self), "Jenkins working!")

if __name__ == '__main__':
    unittest.main()
