from A import solve
import unittest

class test_A(unittest.TestCase):

    def testSolveCase1(self):
       self.assertEqual(solve(200, 1, 200), 39800)
    
    def testSolveCase2(self):
        self.assertEqual(solve(5, 3, 3), 7)

    def testSolveCase3(self):
        self.assertEqual(solve(4, 7, 5), -1)

    def testSolveCase4(self):
        self.assertEqual(solve(4, 2, 28), 57)

    def testSolveCase5(self):
       self.assertEqual(solve(4, 7, 10), -1)
    
    def testSolveCase6(self):
        self.assertEqual(solve(3, 2, 1), 2)

    def testSolveCase7(self):
        self.assertEqual(solve(2, 2, 1), 1)

    def testSolveCase8(self):
        self.assertEqual(solve(12, 10, 6), -1)

    def testSolveCase9(self):
        self.assertEqual(solve(57, 51, 122), 2007)



unittest.main()