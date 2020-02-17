import os
import re
import shutil
import sys
from urllib.parse import urlparse

import requests


class Loader:

    def __init__(self, url: str, referer: str, filename: str = 'tmp', extension: str = 'ts',
                 user_agent: str = 'WebHTML5Player/1.0.0', proxy: str = None, ssl_verify=True, m3u8_ext: str = 'm3u8'):
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

    def get_playlist(self):
        response = requests.get(self.url, verify=self.ssl_verify, headers={
            'Referer': self.referer,
            'Origin': self.origin,
            'User-Agent': self.user_agent, }, proxies=self.proxies)
        return [line for line in response.text.split('\n') if line and '#' not in line]

    def get_files(self):
        files_list = []
        for idx, item in enumerate(self.playlist):
            url_parse = urlparse(self.url)
            url = '%s://%s%s/%s' % (
            url_parse[0], url_parse[1], re.sub('/[a-zA-Z0-9~_\-]+.%s' % self.m3u8_ext, '', url_parse[2]), item)
            response = requests.get(url, stream=True, headers={
                'Referer': self.referer,
                'Origin': self.origin,
                'User-Agent': self.user_agent,
                'Host': url_parse[1],
                'Connection': 'keep-alive',
            }, proxies=self.proxies)
            if response.status_code == 200:
                filename = '%s_%i.%s' % (self.filename, idx, self.extension)
                files_list.append(filename)
                with open(filename, 'wb') as file:
                    file.write(response.content)
                print('Written file %i of %i files' % (idx + 1, len(self.playlist)))
            else:
                print(url)
                print(response.text)
                sys.exit()
        return files_list

    def join_files(self, files_list: list):
        working_dir = os.getcwd()
        filename = '%s.%s' % (self.filename, self.extension)
        with open(filename, "wb") as output:
            for file in files_list:
                with open(os.path.join(working_dir, file), "rb") as part:
                    shutil.copyfileobj(part, output)
        print('Files is merged')

    @staticmethod
    def cleanup(files_list):
        working_dir = os.getcwd()
        for file in files_list:
            file_path = os.path.join(working_dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print('Cleanup is finished')

    def download(self):
        self.playlist = self.get_playlist()
        _ = self.get_files()
        self.join_files(_)
        self.cleanup(_)
