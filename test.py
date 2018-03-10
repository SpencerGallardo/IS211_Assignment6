#! usr/bin/env python
# *-* coding: utf-8 *-*
"""Conversion Testing"""


import conversions
import unittest


class KelvinToFahrenheit(unittest.TestCase):
    
    def test_positive(self):
        results = conversions.convertKelvinToFahrenheit(500)
        self.assertEqual(440.33, results)
        

    def test_negative(self):
        results = conversions.convertKelvinToFahrenheit(-500)
        self.assertEqual(-1359.67, results)
        

    def test_zero(self):
        results = conversions.convertKelvinToFahrenheit(0)
        self.assertEqual(-459.67, results)
        

    def test_decimal(self):
        results = conversions.convertKelvinToFahrenheit(2.50)
        self.assertEquals(-455.17, results)
        

    def test_large(self):
        results = conversions.convertKelvinToFahrenheit(512453)
        self.assertEqual(921955.73, results)

    
class CelsiusToFahrenheit(unittest.TestCase):
    
    def test_positive(self):
        results = conversions.convertCelsiusToFahrenheit(500)
        self.assertEqual(932.0, results)
        

    def test_negative(self):
        results = conversions.convertCelsiusToFahrenheit(-500)
        self.assertEqual(-868, results)
        

    def test_zero(self):
        results = conversions.convertCelsiusToFahrenheit(0)
        self.assertEqual(32.0, results)
        

    def test_decimal(self):
        results = conversions.convertCelsiusToFahrenheit(2.50)
        self.assertEquals(36.5, results)
        

    def test_large(self):
        results = conversions.convertCelsiusToFahrenheit(512453)
        self.assertEqual(922447.4, results)

class FharenheitToKelvin(unittest.TestCase):

    def test_positive(self):
        results = conversions.convertFahrenheitToKelvin(500)
        self.assertEqual(533.15, results)
        

    def test_negative(self):
        results = conversions.convertFahrenheitToKelvin(-500)
        self.assertEqual(-22.406, results)
        

    def test_zero(self):
        results = conversions.convertFahrenheitToKelvin(0)
        self.assertEqual(255.372, results)
        

    def test_decimal(self):
        results = conversions.convertFahrenheitToKelvin(2.50)
        self.assertEquals(256.761, results)
        

    def test_large(self):
        results = conversions.convertFahrenheitToKelvin(512453)
        self.assertEqual(284951.483, results)

class FahrenheitToCelsius(unittest.TestCase):

    def test_positive(self):
        results = conversions.convertFahrenheitToCelsius(500)
        self.assertEqual(260, results)
        

    def test_negative(self):
        results = conversions.convertFahrenheitToCelsius(-500)
        self.assertEqual(-295.556, results)
        

    def test_zero(self):
        results = conversions.convertFahrenheitToCelsius(0)
        self.assertEqual(-17.778, results)
        

    def test_decimal(self):
        results = conversions.convertFahrenheitToCelsius(2.50)
        self.assertEquals(-16.389, results)
        

    def test_large(self):
        results = conversions.convertFahrenheitToCelsius(512453)
        self.assertEqual(284678.333, results)
        
class KelvinToCelsius(unittest.TestCase):

    def test_positive(self):
        results = conversions.convertKelvinToCelsius(500)
        self.assertEqual(226.85, results)
        

    def test_negative(self):
        results = conversions.convertKelvinToCelsius(-500)
        self.assertEqual(-773.15, results)
        

    def test_zero(self):
        results = conversions.convertKelvinToCelsius(0)
        self.assertEqual(-273.15, results)
        

    def test_decimal(self):
        results = conversions.convertKelvinToCelsius(2.50)
        self.assertEquals(-270.65, results)
        

    def test_large(self):
        results = conversions.convertKelvinToCelsius(512453)
        self.assertEqual(512179.85, results)
        


class CelsiusToKelvin(unittest.TestCase): 

    def test_positive(self):
        results = conversions.convertCelsiusToKelvin(500)
        self.assertEqual(773.15, results)
        

    def test_negative(self):
        results = conversions.convertCelsiusToKelvin(-500)
        self.assertEqual(-226.85, results)
        

    def test_zero(self): 
        results = conversions.convertCelsiusToKelvin(0)
        self.assertEqual(273.15, results)
        

    def test_decimal(self): 
        results = conversions.convertCelsiusToKelvin(2.50)
        self.assertEqual(275.65, results)
        

    def test_large(self):
        results = conversions.convertCelsiusToKelvin(512453)
        self.assertEqual(512726.15, results)

    
if __name__ == "__main__":
    unittest.main()