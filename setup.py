from setuptools import setup, find_packages

setup(
    name="amrit-core",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "python>=3.10",
        "jupyter>=1.0.0",
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "scikit-learn>=1.0.0",
        "ipython>=7.0.0",
    ],
    author="gurpreetsingh2009-cmyk",
    description="Naam-conscious learning platform that integrates spiritual wisdom with machine learning",
    long_description="A platform designed to integrate spiritual wisdom with state-of-the-art machine learning techniques",
    url="https://github.com/gurpreetsingh2009-cmyk/amrit-core-dna",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.10",
)
