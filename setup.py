from setuptools import setup, find_packages # type: ignore

setup(
    name="securelib",
    version="1.0.0",
    description="A comprehensive security utility library for encryption, scanning, and vulnerability detection",
    author="Your Name",
    author_email="your_email@example.com",
    url="",  # 必要に応じて変更
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pycryptodome",
        "requests"
    ],
    python_requires='>=3.6',
)
