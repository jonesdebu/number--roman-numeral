import unittest
import pytest

from convert_to_roman import to_roman

def test_to_roman():
    assert to_roman(1) == "I"
    assert to_roman(1000) == "M"
