import setuptools

with open("README.md") as file:
    long_description = file.read()

setuptools.setup(
    name="scraloud",
    version="0.0.1",
    author="Musab Gültekin",
    author_email="author@example.com",
    description="Scraloud Python Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scraloud/scraloud-python",
    packages=setuptools.find_packages(),
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
)