import os
import shutil


class ProgressBar:

    def __init__(self):
        self.filters = {}
        self.add_filter('percents', self.progress_percents)
        self.add_filter('progress', self.progress_bar)

    def add_filter(self, name: str, func: object):
        self.filters[name] = func

    @staticmethod
    def progress_percents(idx: int, count: int) -> str:
        template = 'Downloaded => %3.1f %%'
        return template % (100.0 * float(idx) / float(count))

    @staticmethod
    def progress_bar(idx: int, count: int, num_symbols: int = 10) -> str:
        ratio = (idx / count) * num_symbols
        template = ''.join(['-' if ratio <= ii else '=' for ii in range(1, num_symbols + 1)])
        return '[%s]' % template


def join_files(files_list: list, filename: str):
    working_dir = os.getcwd()
    with open(filename, "wb") as output:
        for file in files_list:
            with open(os.path.join(working_dir, file), "rb") as part:
                shutil.copyfileobj(part, output)
    print('Files are merged')


def cleanup(files_list):
    working_dir = os.getcwd()
    for file in files_list:
        file_path = os.path.join(working_dir, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print('Cleanup is finished')
