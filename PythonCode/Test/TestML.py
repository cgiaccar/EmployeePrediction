"""
Unit testing of the methods in MachineLearning
"""

import unittest
import MachineLearning as ml


class PredictTesting(unittest.TestCase):
    def test_predict_false(self):
        education = 1
        joining_year = 2012
        city = 1
        payment_tier = 1
        age = 18
        gender = 0
        ever_benched = 0
        experience = 0
        expected_result = False
        result = ml.predict(education, joining_year, city, payment_tier,
                            age, gender, ever_benched, experience)
        self.assertEqual(result, expected_result,
                         "The prediction should be False")

    def test_predict_true(self):
        education = 1
        joining_year = 2014
        city = 3
        payment_tier = 2
        age = 37
        gender = 1
        ever_benched = 0
        experience = 5
        expected_result = True
        result = ml.predict(education, joining_year, city, payment_tier,
                            age, gender, ever_benched, experience)
        self.assertEqual(result, expected_result,
                         "The prediction should be True")


if __name__ == '__main__':
    unittest.main()
