import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chess.com", 
    version="1.6.1",
    author="Artur Saradzhyan",
    author_email="saradzhyanartur@gmail.com",
    description="Python Wrapper around Chess.com API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarartur/chess.com",
    packages=setuptools.find_packages(),
    install_requires=['requests==2.25.1', ],
    setup_requires=['requests==2.25.1', ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)