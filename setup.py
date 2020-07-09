import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="boring_logger",  # Replace with your own username
    version="0.0.2",
    author="Alex Newman",
    author_email="boringlogger@wuli.nu",
    description="I have to make this thing over and over again and I bet so do you",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/posix4e/boring_logger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
