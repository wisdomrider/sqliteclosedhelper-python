from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.MD')) as f:
    long_description = f.read()


setup(
    name="sqliteclosedhelper",
    version="1.0.2",
    long_description=long_description,
    long_description_content_type='text/markdown',
    description="Sqlite helper module",
    url="https://github.com/wisdomrider/sqliteclosedhelper-python",
    author="wisdomrider",
    author_email="avishekzone@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["sqliteclosedhelper"],
    include_package_data=True,
    
)
