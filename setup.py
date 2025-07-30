from setuptools import setup, find_packages

setup(
    name="imgpassgen",
    version="0.1.0",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=open("requirements.txt").read().splitlines(),
    python_requires='>=3.7',
)