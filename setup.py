from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Juniper Command System is a Micro CLI Tool that allows you to manage your files, launch applications, as well as providing extra tools for OS Management.'
LONG_DESCRIPTION = 'Juniper Command System is a Micro CLI Tool that allows you to manage your files, launch applications, as well as providing extra tools for OS Management.'

# Setting up
setup(
    name="junipertest",
    version=VERSION,
    author="Juan Carlos Juárez",
    author_email="<jc.juarezgarcia@outlook.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['Python', 'CLI', 'Tool'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)