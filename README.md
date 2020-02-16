# pym3u8

**pym3u8** is simple Python 3 lib for downloading online HLS streams and videos.
For example you can use it to download HLS streams and videos. 


## Basic usage
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
