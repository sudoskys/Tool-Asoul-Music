# encoding: utf-8
import os
import tarfile
import gzip
from pathlib import Path
import yaml


class yamler(object):
    # sudoskys@github
    def __init__(self):
        self.debug = False
        self.home = Path().cwd()

    def debug(self, log):
        if self.debug:
            print(log)

    def rm(self, top):
        Path(top).unlink()

    def read(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            result = yaml.full_load(f.read())
        return result

    def save(self, path, Data):
        with open(path, 'w+', encoding='utf-8') as f:
            yaml.dump(data=Data, stream=f, allow_unicode=True)



class doTarGz(object):
    # csdn paisen110/article/details/124188478
    def __init__(self):
        self.debug = False
        self.home = Path().cwd()
        # 如果只打包不压缩，将"w:gz"参数改为"w:"或"w"即可。

    def mkTarAll(self, output_filename, source_dir):
        with tarfile.open(output_filename, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))
        return output_filename

    # 逐个添加
    def mkTarCareful(self, output_filename, source_dir):
        tar = tarfile.open(output_filename, "w:gz")
        for root, dir, files in os.walk(source_dir):
            for file in files:
                pathfile = os.path.join(root, file)
                tar.add(pathfile)
        tar.close()
        return output_filename

    def unGz(self, file_name):
        """ungz zip file"""
        f_name = file_name.replace(".gz", "")
        g_file = gzip.GzipFile(file_name)
        open(f_name, "wb+").write(g_file.read())
        g_file.close() 
    
    def unTar(self, file_name):
        """untar zip file"""
        tar = tarfile.open(file_name)
        names = tar.getnames()
        if os.path.isdir(file_name + "_files"):
            pass
        else:
            os.mkdir(file_name + "_files")
        for name in names:
            tar.extract(name, file_name + "_files/")
        tar.close()