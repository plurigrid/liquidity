```python
import unittest
from liquidity_metasploit.attack_tactics import AttackTactics

class TestAttackTactics(unittest.TestCase):

    def setUp(self):
        self.attack_tactics = AttackTactics()

    def test_attack_tactic_1(self):
        result = self.attack_tactics.tactic_1()
        self.assertTrue(result)

    def test_attack_tactic_2(self):
        result = self.attack_tactics.tactic_2()
        self.assertTrue(result)

    def test_attack_tactic_3(self):
        result = self.attack_tactics.tactic_3()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```