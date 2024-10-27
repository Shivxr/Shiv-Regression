from setuptools import setup, find_packages

setup(
    name='sreg',
    version='0.1',
    description='A simple linear regression library',
    author='Shiv Shankar N',
    author_email='shivshankar11a@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=['numpy'],
)
