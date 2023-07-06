```python
import unittest
from liquidity_metasploit.common_vulnerabilities import CommonVulnerabilities

class TestCommonVulnerabilities(unittest.TestCase):

    def setUp(self):
        self.vulnerabilities = CommonVulnerabilities()

    def test_reentrancy(self):
        self.assertTrue(self.vulnerabilities.reentrancy())

    def test_arithmetic_overflow(self):
        self.assertTrue(self.vulnerabilities.arithmetic_overflow())

    def test_unchecked_external_call(self):
        self.assertTrue(self.vulnerabilities.unchecked_external_call())

    def test_short_address_attack(self):
        self.assertTrue(self.vulnerabilities.short_address_attack())

    def test_force_send(self):
        self.assertTrue(self.vulnerabilities.force_send())

if __name__ == '__main__':
    unittest.main()
```