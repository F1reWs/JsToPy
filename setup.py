import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="JsToPy",
    version="0.1.5",
    author="Firew",
    author_email="road.of.programming@gmail.com",
    description=(
        "A library that add to python some js functions."
    ),
    install_requires=None,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/F1reWs/JsToPy",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
