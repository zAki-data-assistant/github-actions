# test_calculator.py

from calculator import add

def test_add():
    """Test case for add function."""
    assert add(2, 3) == 5, "Should be 5"

def test_add_negative():
    """Test case for add function with negative numbers."""
    assert add(-2, -3) == -5, "Should be -5"

def test_add_zero():
    """Test case for add function with zero."""
    assert add(0, 0) == 0, "Should be 0"
