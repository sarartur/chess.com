import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chess.com",
    version="2.0.6",
    author="Artur Saradzhyan",
    author_email="sarartur.ruk@gmail.com",
    description="Python Wrapper for Chess.com API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarartur/chess.com",
    packages=setuptools.find_packages(),
    install_requires=["aiohttp==3.8.3", "requests==2.31.0"],
    setup_requires=["aiohttp==3.8.3", "requests==2.31.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
