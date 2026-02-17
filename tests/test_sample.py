"""Sample test file for CI/CD pipeline."""
import pytest


def test_sample_addition():
    """Test basic addition."""
    assert 1 + 1 == 2


def test_sample_subtraction():
    """Test basic subtraction."""
    assert 5 - 3 == 2


def test_sample_multiplication():
    """Test basic multiplication."""
    assert 3 * 4 == 12


def test_sample_division():
    """Test basic division."""
    assert 10 / 2 == 5


def test_string_concatenation():
    """Test string operations."""
    assert "Hello" + " " + "World" == "Hello World"


class TestDataProcessing:
    """Test class for data processing functions."""
    
    def test_list_length(self):
        """Test list operations."""
        data = [1, 2, 3, 4, 5]
        assert len(data) == 5
    
    def test_dict_keys(self):
        """Test dictionary operations."""
        data = {"a": 1, "b": 2, "c": 3}
        assert "a" in data
        assert data["b"] == 2
