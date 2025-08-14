from setuptools import setup, find_packages

setup(
    name="nimbuspost",
    version="0.1.0",
    description="A Python SDK for NimbusPost shipping platform API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/nimbuspost", 
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "requests>=2.25.1", 
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7", 
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    include_package_data=True,
)
