#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 6 assignment - Temprature Conversions"""


def convertCelsiusToKelvin(temp):
    total = temp + 273.15
    return float("%.3f" % total)

def convertCelsiusToFahrenheit(temp):
    total = (1.8 * temp) + 32
    return float("%.3f" % total)

def convertKelvinToCelsius(temp):
    total = temp - 273.15
    return float("%.3f" % total)

def convertKelvinToFahrenheit(temp):
    total = (temp - 273.15) * 1.8 + 32
    return float("%.3f" % total)

def convertFahrenheitToKelvin(temp):
    total = ((temp - 32) / 1.8) + 273.15
    return float("%.3f" % total)

def convertFahrenheitToCelsius(temp):
    total = (temp - 32) / 1.8
    return float("%.3f" % total)