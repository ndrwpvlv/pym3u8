# pym3u8

**pym3u8** is simple Python 3 lib for downloading online HLS streams and videos. 

You need only link to m3u8 file with list of ts-files.

pym3u8 working with direct connections and socks proxies.

## Installation
Install with pip:
```
pip install pym3u8
```

Or download source or clone repository and execute:
```
pip3 install git+https://github.com/ndrwpvlv/pym3u8.git
```
If you have some permissions errors try this one:
```
sudo -H pip3 install git+https://github.com/ndrwpvlv/pym3u8.git
```

## Basic usage from cli
Basic usage from command line
```
python3 -m pym3u8 [-h] [-u URL] [-r REFERER] [-f FILENAME] [-e EXTENSION]
              [-a USER_AGENT] [-p PROXY] [-m M3U8_EXT] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Url of m3u8
  -r REFERER, --referer REFERER
                        Referer url
  -f FILENAME, --filename FILENAME
                        File name for downloading
  -e EXTENSION, --extension EXTENSION
                        Extension of file for downloading
  -a USER_AGENT, --user_agent USER_AGENT
                        User-agent string
  -p PROXY, --proxy PROXY
                        Proxy url
  -m M3U8_EXT, --m3u8_ext M3U8_EXT
                        Custom m3u8 extension
  -s, --ssl_verify      Verify ssl certificates

```
Example:
```
python3 -m pym3u8 -u "https://example.com/hls/videos/000000/00/000000000/,720P_4000K,480P_2000K,240P_400K,_000000000.mp4.urlset/index-f1-v1-a1.m3u8" -p "socks5://127.0.0.1:1080"
```

## Basic usage from macros
```
from pym3u8 import Loader

url = 'https://example.com/videos/ts/0000/0001/playlist.m3u8'
referer = ''
proxy = 'socks5://127.0.0.1:1080'
filename = 'stream'
extension = 'ts'
user_agent='ExampleUA/0.0.1'

loader = Loader(url, referer, proxy=proxy, filename=filename, extension=extension, user_agent=user_agent)
loader.download()
``` 
## Requirements
```
Python 3.6+

certifi==2019.11.28
chardet==3.0.4
idna==2.8
PySocks==1.7.1
requests==2.22.0
socks==0
urllib3==1.25.8
```
