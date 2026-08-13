# test_novapivot.py
"""
Tests for NovaPivot module.
"""

import unittest
from novapivot import NovaPivot

class TestNovaPivot(unittest.TestCase):
    """Test cases for NovaPivot class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NovaPivot()
        self.assertIsInstance(instance, NovaPivot)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NovaPivot()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
