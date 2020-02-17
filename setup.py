# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='pym3u8',
    version='0.1.3',
    packages=['pym3u8', ],
    url='https://github.com/ndrwpvlv/pym3u8',
    license='MIT',
    author='Andrei S. Pavlov',
    author_email='ndrw.pvlv@gmail.com',
    description='Simple Python 3 lib for downloading online HLS streams and videos',
    download_url='https://github.com/ndrwpvlv/pym3u8/archive/0.1.3.tar.gz',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['M3U8', 'HLS', 'STREAM', 'VIDEO', ],

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=['certifi==2019.11.28', 'chardet==3.0.4', 'idna==2.8', 'PySocks==1.7.1', 'requests==2.22.0',
                      'socks==0', 'urllib3==1.25.8'],
)
