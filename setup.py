import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chess.com", 
    version="1.4.1",
    author="Artur Saradzhyan",
    author_email="saradzhyanartur@gmail.com",
    description="Python Wrapper around Chess.com API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarartur/chess.com",
    packages=setuptools.find_packages(),
    install_requires=['urllib3==1.25.9', 'certifi==2020.4.5.1'],
    setup_requires=['urllib3==1.25.9', 'certifi==2020.4.5.1'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)