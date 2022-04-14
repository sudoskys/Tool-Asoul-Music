from pathlib import Path
import yaml


class yamler(object):
    # sudoskys@github
    def __init__(self):
        self.debug = True
        self.home = Path().cwd()

    def debug(self, log):
        if self.debug:
            print(log)

    def rm(self, top):
        Path(top).unlink()

    def read(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            result = yaml.load(f.read())
        return result

    def save(self, path, Data):
        with open(path, 'w+', encoding='utf-8') as f:
            yaml.dump(data=Data, stream=f, allow_unicode=True)
