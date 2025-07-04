from setuptools import setup, find_packages

setup(
    name='loadifscator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'typer',
        'jinja2',
        'cryptography',
        'pycryptodome',
    ],
    entry_points={
        'console_scripts': [
            'loadifscator=cli:app',
        ],
    },
    author='Your Name',
    description='Red Team Payload Generator & Obfuscation Framework',
    license='MIT',
) 
