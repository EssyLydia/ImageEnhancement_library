from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'capturing images and enhancing package'


# Setting up
setup(
    name="camcapturepkg",
    version=VERSION,
    author="Nambogwe Lydia",
    author_email="<esterlydia4@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui'],
    keywords=['python', 'image', 'stream', 'camera stream'],
    classifiers=[
        "Development Status :: 1 - Implementation",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)