"""
Unit testing of the methods in BackEnd

The Transform methods are if/then/else only, so the unit testing is actually
 unnecessary, but this can change in time
"""

import unittest
import BackEnd


class TransformCityTesting(unittest.TestCase):
    def test_bangalore(self):
        self.assertEqual(BackEnd.transform_city("bangalore"), 1,
                         "Bangalore should be transformed to 1")

    def test_new_delhi(self):
        self.assertEqual(BackEnd.transform_city("New Delhi"), 2,
                         "New Delhi should be transformed to 2")

    def test_pune(self):
        self.assertEqual(BackEnd.transform_city("Pune"), 3,
                         "Pune should be transformed to 3")


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
    def test_not_benched(self):
        self.assertEqual(BackEnd.transform_ever_benched("No"), 0,
                         "No should be transformed to 0")

    def test_benched(self):
        self.assertEqual(BackEnd.transform_ever_benched("Yes"), 1,
                         "Yes should be transformed to 1")


class TransformGenderTesting(unittest.TestCase):
    def test_male(self):
        self.assertEqual(BackEnd.transform_gender("Male"), 0,
                         "Male should be transformed to 0")

    def test_female(self):
        self.assertEqual(BackEnd.transform_gender("Female"), 1,
                         "Female should be transformed to 1")


class TransformPaymentTierTesting(unittest.TestCase):
    def test_three(self):
        self.assertEqual(BackEnd.transform_payment_tier(3), 1,
                         "3 should be transformed to 1")

    def test_two(self):
        self.assertEqual(BackEnd.transform_payment_tier(2), 2,
                         "2 should be transformed to 2")

    def test_one(self):
        self.assertEqual(BackEnd.transform_payment_tier(1), 3,
                         "1 should be transformed to 3")


if __name__ == '__main__':
    unittest.main()
