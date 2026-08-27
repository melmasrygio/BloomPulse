# test_bloompulse.py
"""
Tests for BloomPulse module.
"""

import unittest
from bloompulse import BloomPulse

class TestBloomPulse(unittest.TestCase):
    """Test cases for BloomPulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BloomPulse()
        self.assertIsInstance(instance, BloomPulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BloomPulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
