from setuptools import setup, find_packages

setup(
    name='liquidity_metasploit',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/user/liquidity_metasploit',
    license='MIT',
    author='Your Name',
    author_email='your.email@example.com',
    description='Liquidity is a Metasploit for Solidity - an easy to use by anyone library containing common Solidity vulnerabilities and ways of live learning a strategy for which compostions of attack tactics to use that get learned with reinforcement learning',
    install_requires=[
        'gym',
        'numpy',
        'tensorflow',
        'keras',
        'py-solc-x',
        'web3',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='solidity, metasploit, reinforcement learning, attack tactics, vulnerabilities',
    package_data={
        'liquidity_metasploit': ['*.py'],
    },
)