# Liquidity Metasploit

Liquidity is a Metasploit for Solidity - an easy to use library containing common Solidity vulnerabilities and ways of live learning a strategy for which compositions of attack tactics to use that get learned with reinforcement learning.

## Features

- Collection of common Solidity vulnerabilities
- Attack tactics for exploiting vulnerabilities
- Reinforcement learning for optimizing attack tactics
- Gym environment for training the reinforcement learning algorithm

## Installation

To install the library, run the following command:

```
pip install -r requirements.txt
```

## Usage

To use the library, import the necessary modules:

```python
from liquidity_metasploit.common_vulnerabilities import CommonVulnerabilities
from liquidity_metasploit.attack_tactics import AttackTactics
from liquidity_metasploit.reinforcement_learning import ReinforcementLearning
from liquidity_metasploit.gym_environment import GymEnvironment
```

## Testing

To run the tests, execute the following command:

```
python -m unittest discover -s liquidity_metasploit/tests
```

## Contributing

Contributions are welcome. Please submit a pull request.

## License

MIT
