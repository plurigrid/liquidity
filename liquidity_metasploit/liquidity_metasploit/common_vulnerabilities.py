```python
class Vulnerability:
    def __init__(self, name, description, severity):
        self.name = name
        self.description = description
        self.severity = severity

class CommonVulnerabilities:
    def __init__(self):
        self.vulnerabilities = []

    def add_vulnerability(self, name, description, severity):
        self.vulnerabilities.append(Vulnerability(name, description, severity))

    def get_vulnerabilities(self):
        return self.vulnerabilities

common_vulnerabilities = CommonVulnerabilities()

# Adding some common Solidity vulnerabilities
common_vulnerabilities.add_vulnerability("Reentrancy", "Allows for nested calls to external contracts", "High")
common_vulnerabilities.add_vulnerability("Arithmetic Over/Under Flows", "Allows for integer overflow and underflow", "Medium")
common_vulnerabilities.add_vulnerability("Unchecked External Call", "External calls may fail silently or be maliciously manipulated", "High")
common_vulnerabilities.add_vulnerability("Short Address/Parameter Mismatch", "If the address is short, Solidity fills missing bytes with zeros", "Low")
common_vulnerabilities.add_vulnerability("Timestamp Dependence", "Miners can manipulate timestamps", "Medium")
```