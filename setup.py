# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt') as fr:
    required = fr.read().splitlines()

setup(
    name='pym3u8',
    version='0.1.1',
    packages=['pym3u8', ],
    url='https://github.com/ndrwpvlv/pym3u8',
    license='MIT',
    author='Andrei S. Pavlov',
    author_email='ndrw.pvlv@gmail.com',
    description='Simple Python 3 lib for downloading online HLS streams and videos',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['M3U8', 'HLS', 'STREAM', 'VIDEO', ],

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=required,
)
