import re
import sys
from urllib.parse import urlparse

import requests

from .helpers import ProgressBar


class Loader:

    def __init__(self, url: str, referer: str, filename: str = 'file', extension: str = 'ts',
                 user_agent: str = 'WebHTML5Player/1.0.0', proxy: str = None, ssl_verify=True, m3u8_ext: str = 'm3u8',
                 max_retries: int = 5):
        kwargs = dict(locals())
        self.url = kwargs['url']
        self.referer = kwargs['referer']
        self.origin = '%s:\/\/%s' % (urlparse(self.referer)[0], urlparse(self.referer)[1])
        self.filename = kwargs['filename']
        self.extension = kwargs['extension']
        self.user_agent = kwargs['user_agent']
        self.ssl_verify = kwargs['ssl_verify']
        self.m3u8_ext = kwargs['m3u8_ext']
        if proxy:
            self.proxies = {'http': kwargs['proxy'], 'https': kwargs['proxy'], }
        else:
            self.proxies = None
        self.playlist = None
        self.session = requests.Session()
        self.session_adapter = requests.adapters.HTTPAdapter(max_retries=max_retries)
        self.session.mount('http://', self.session_adapter)
        self.session.mount('https://', self.session_adapter)
        self.chunk_size = 8192
        self.progress_bar = ProgressBar().filters['percents']

    def get_playlist(self):
        response = self.session.get(self.url, verify=self.ssl_verify, headers={
            'Referer': self.referer,
            'Origin': self.origin,
            'User-Agent': self.user_agent, }, proxies=self.proxies)
        return [line if line[0:2] != './' else line[2:] for line in response.text.split('\n') if
                line and '#' not in line]

    def get_files(self):
        filename = '%s.%s' % (self.filename, self.extension)
        with open(filename, 'wb', buffering=self.chunk_size) as file:
            for idx, item in enumerate(self.playlist):
                url_parse = urlparse(self.url)
                url = '%s://%s%s/%s' % (
                    url_parse[0], url_parse[1], re.sub('/[a-zA-Z0-9~_\-]+.%s' % self.m3u8_ext, '', url_parse[2]), item)
                with self.session.get(url, stream=True, headers={
                    'Referer': self.referer,
                    'Origin': self.origin,
                    'User-Agent': self.user_agent,
                    'Host': url_parse[1],
                    'Connection': 'keep-alive',
                }, proxies=self.proxies) as response:
                    if response.status_code == 200:
                        for chunk in response.iter_content(chunk_size=self.chunk_size):
                            file.write(chunk) if chunk else None
                        print(self.progress_bar(idx, len(self.playlist)), end='\r', flush=True)
                    else:
                        print(url)
                        print(response.text)
                        sys.exit()
        print('\nFinished')
        return True

    def download(self):
        self.playlist = self.get_playlist()
        self.get_files()
