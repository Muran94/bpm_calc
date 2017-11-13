import unittest
from bpm_calc import BPMCalc

class TestBPMCalc(unittest.TestCase):
    def test_init(self):
        bpm_calc = BPMCalc(100)
        self.assertEqual(bpm_calc.original_bpm, 100)

    def test_calc(self):
        bpm_calc = BPMCalc(100)
        bpm_calc.calc()
        expected_result = [50, 75, 100, 125, 150, 175, 200]
        self.assertListEqual(bpm_calc.bpm_list, expected_result)

    def test_get_result(self):
        bpm_calc = BPMCalc(100)
        bpm_calc.calc()
        expected_result = """
        0.50倍速:  50BPM
        0.75倍速:  75BPM
        1.00倍速: 100BPM
        1.25倍速: 125BPM
        1.50倍速: 150BPM
        1.75倍速: 175BPM
        2.00倍速: 200BPM
        """
        self.assertEqual(bpm_calc.get_result(), expected_result)

if __name__ == "__main__":
    unittest.main()
