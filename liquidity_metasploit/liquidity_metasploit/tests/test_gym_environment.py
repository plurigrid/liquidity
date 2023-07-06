```python
import unittest
from liquidity_metasploit.gym_environment import GymEnvironment

class TestGymEnvironment(unittest.TestCase):

    def setUp(self):
        self.env = GymEnvironment()

    def test_reset(self):
        initial_state = self.env.reset()
        self.assertIsNotNone(initial_state, "Initial state should not be None")

    def test_step(self):
        initial_state = self.env.reset()
        action = self.env.sample_action()
        next_state, reward, done, info = self.env.step(action)
        self.assertIsNotNone(next_state, "Next state should not be None")
        self.assertIsNotNone(reward, "Reward should not be None")
        self.assertIsNotNone(done, "Done should not be None")
        self.assertIsNotNone(info, "Info should not be None")

    def test_sample_action(self):
        action = self.env.sample_action()
        self.assertIsNotNone(action, "Sampled action should not be None")

if __name__ == '__main__':
    unittest.main()
```