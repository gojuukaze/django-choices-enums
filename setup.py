from os import path

import setuptools

setuptools.setup(
    name="django-choices-enums",
    version='1.0.0',
    description="The enum type used for Django choices enables Django's choices to support code prompts!!",
    long_description=open("README.rst").read(),

    url="https://github.com/gojuukaze/django-choices-enum",
    author="gojuukaze",
    author_email="ikaze_email@163.com",
    packages=setuptools.find_packages(exclude=['tests']),
    python_requires='>=3',
    platforms=['Any'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        "Framework :: Django",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)
