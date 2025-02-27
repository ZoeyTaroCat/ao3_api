import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
with open("requirements.txt", "r") as fh:
    requires = [line for line in fh.read().splitlines() if line != ""]

setuptools.setup(
    name="ao3-api",
    version="1.0",
    author="ZoeyTaroCat",
    author_email="zoeytarocat+ao3api@gmail.com",
    description="An unofficial AO3 (archiveofourown.org) API. Updated to v2.2.1 from the upstream repo.",
    python_requires='>=3.8',
    install_requires=requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZoeyTaroCat/ao3_api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
