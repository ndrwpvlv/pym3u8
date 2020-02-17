# -*- coding: utf-8 -*-

import argparse
import sys

from pym3u8 import Loader


def args_get() -> dict:
    parser = argparse.ArgumentParser(prog='pym3u8',
                                     description='Simple Python 3 lib for downloading online HLS streams and videos', )
    parser.add_argument('-u', '--url', help="Url of m3u8", type=str, )
    parser.add_argument('-r', '--referer', help="Referer url", default='', type=str)
    parser.add_argument('-f', '--filename', help="File name for downloading", default='file', type=str)
    parser.add_argument('-e', '--extension', help="Extension of file for downloading", default='ts', type=str)
    parser.add_argument('-a', '--user_agent', help="User-agent string", default='WebHTML5Player/1.0.0', type=str)
    parser.add_argument('-p', '--proxy', help="Proxy url", default=None, type=str)
    parser.add_argument('-m', '--m3u8_ext', help="Custom m3u8 extension", default='m3u8', type=str)
    parser.add_argument('-s', '--ssl_verify', action='store_true', help='Verify ssl certificates',
                        default=False)
    parser.add_argument('-c', '--max_retries', help="Maximum retries to download", default=5, type=int)

    args = parser.parse_args(sys.argv[1:])

    return {
        'url': args.url,
        'referer': args.referer,
        'filename': args.filename,
        'extension': args.extension,
        'user_agent': args.user_agent,
        'proxy': args.proxy,
        'm3u8_ext': args.m3u8_ext,
        'ssl_verify': args.ssl_verify,
        'max_retries': args.max_retries,
    }


def main():
    args = args_get()
    print('-----------------\npym3u8. Stream and video downloader\n-----------------\n')
    print('Variables:')
    for key in args:
        print('{}: {}'.format(key, args[key]))
    print('-----------------\n')

    loader = Loader(args['url'], args['referer'], args['filename'], args['extension'], args['user_agent'],
                    args['proxy'], args['ssl_verify'], args['m3u8_ext'], args['max_retries'], )
    loader.download()


if __name__ == '__main__':
    main()
