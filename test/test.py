import unittest
import code.datamunger as datamunger


class TestData(unittest.TestCase):
    
    #UNIT TEST 1: Check calculated total correct
    def test_CheckTotal(self):
        testArr = [100, 20, 10, 15, 15, 5, 10, 5, 20, 0]
        result = datamunger.calc_total(testArr)
        self.assertEqual(result, 100)

    #UNIT TEST 2: Check calculated total incorrect
    def test_CheckTotalWrong(self):
        testArr = [100, 20, 10, 10, 15, 5, 10, 5, 20, 0]
        result = datamunger.calc_total(testArr)
        self.assertNotEqual(result, 100)

    #UNIT TEST 3: Check monotonic no error
    def test_CheckMono(self):
        testPrev = [200, 10, 10, 20, 20, 50, 20, 20, 50, 0]
        testCurr = [208, 11, 11, 21, 21, 51, 21, 21, 51, 0]
        result = datamunger.check_monotonic(testPrev, testCurr)
        self.assertEqual(result, "")  

    #UNIT TEST 4: Check monotonic error
    def test_CheckMonoError(self):
        testPrev = [200, 10, 10, 20, 20, 50, 20, 20, 50, 0]
        testCurr = [206, 9, 11, 21, 21, 51, 21, 21, 51, 0]
        result = datamunger.check_monotonic(testPrev, testCurr)
        self.assertEqual(result, "Monotonic error at column 1 comparing lines 57 and 58 values 9 and 10")       

    #UNIT TEST 5: Check missing data success
    def test_CheckMissing(self):
        testPrev = [0,0,0,0,0,0,0,0,0,0]
        testCurr = [0,0,0,0,0,0,0,0,0,0]
        result = datamunger.check_row(1, testPrev, testCurr)
        check = True
        self.assertEqual(result, check)

    #UNIT TEST 6: Check missing data fail
    def test_CheckMissingFail(self):
        testPrev = [0,0,0,0,0,0,0,0,0,0]
        testCurr = [100,20,10,"","","","","","",""]
        result = datamunger.check_row(1, testPrev, testCurr)
        check = False
        self.assertEqual(result, check)

    #UNIT TEST 7: Check missing data empty OTHER column
    def test_CheckMissingOther(self):
        testPrev = [0,0,0,0,0,0,0,0,0,0]
        testCurr = [100,20,10,5,5,6,7,8,9,""]
        result = datamunger.check_row(1, testPrev, testCurr)
        check = True
        self.assertEqual(result, check)

if __name__ == '__main__':
    unittest.main()
