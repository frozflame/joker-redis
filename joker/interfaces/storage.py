#!/usr/bin/env python3
# coding: utf-8

import os.path


class FileStorageInterface:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir

    def read_as_chunks(self, path: str, chunksize=65536):
        path = os.path.join(self.base_dir, path)
        with open(path, 'rb') as fin:
            while True:
                chunk = fin.read(chunksize)
                if not chunk:
                    break
                yield chunk

    def read_as_binary(self, path):
        with open(path, 'rb') as fin:
            return fin.read()

    def save_as_file(self, path: str, chunks):
        path = os.path.join(self.base_dir, path)
        with open(fullpath, 'wb') as fout:
            for chunk in chunks:
                fout.write(chunk)
