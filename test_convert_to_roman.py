import unittest
import pytest

from convert_to_roman import to_roman

def test_to_roman():
    assert to_roman(1000) == "M"
    assert to_roman(900) == "CM"
    assert to_roman(500) == "D"
    assert to_roman(400) == "CD"
    assert to_roman(100) == "C"
    assert to_roman(90) == "XC"
    assert to_roman(50) == "L"
    assert to_roman(40) == "XL"
    assert to_roman(10) == "X"
    assert to_roman(9) == "IX"
    assert to_roman(5) == "V"
    assert to_roman(4) == "IV"
    assert to_roman(1) == "I"
    assert to_roman(0) == "I" #expect an input of 0 to be changed to 1 by default
    assert to_roman(-1) == "I" #expect a negative value to use the absolute value of the input instead
