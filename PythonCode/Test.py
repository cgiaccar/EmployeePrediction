"""
Unit testing of the methods in BackEnd
"""

import unittest
import BackEnd


class TransformCityTesting(unittest.TestCase):
    pass


class TransformEducationTesting(unittest.TestCase):
    def test_bachelor(self):
        self.assertEqual(BackEnd.transform_education("Bachelor"), 1,
                         "Bachelor should be transformed to 1")

    def test_master(self):
        self.assertEqual(BackEnd.transform_education("Master"), 2,
                         "Master should be transformed to 2")

    def test_PHD(self):
        self.assertEqual(BackEnd.transform_education("PHD"), 3,
                         "PHD should be transformed to 3")


class TransformEverBenchedTesting(unittest.TestCase):
    pass


class TransformGenderTesting(unittest.TestCase):
    pass


class TransformPaymentTierTesting(unittest.TestCase):
    pass


class PredictTesting(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
