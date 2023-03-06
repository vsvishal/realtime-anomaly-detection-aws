import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="realtime-anomaly-detection-aws",
    version="1.0.0",

    description="An empty CDK Python app",
    long_description="Sample for carbon footprint.",
    long_description_content_type="text/markdown",

    author="Florian Mair",

    package_dir={"": "realtime-anomaly-detection-aws"},
    packages=setuptools.find_packages(where="realtime-anomaly-detection-aws"),

    install_requires=[
        "aws-cdk.core==1.65.0",

    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 1 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
