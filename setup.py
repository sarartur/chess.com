import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    "aiohttp>=3", 
    "requests>=2",
]

setuptools.setup(
    name="chess.com",
    version="3.1.0",
    author="Artur Saradzhyan",
    author_email="sarartur.ruk@gmail.com",
    description="Python Wrapper for Chess.com API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarartur/chess.com",
    packages=setuptools.find_packages(),
    install_requires=requires,
    setup_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
