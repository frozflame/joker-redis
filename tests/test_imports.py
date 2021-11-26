#!/usr/bin/env python3
# coding: utf-8

import importlib

import volkanic
from volkanic.introspect import find_all_plain_modules

dotpath_prefixes = [
    'joker.interfaces.',
    'tests.',
]


class _GI(volkanic.GlobalInterface):
    package_name = 'joker.interfaces'


def _check_prefix(path):
    for prefix in dotpath_prefixes:
        if path.startswith(prefix):
            return True
    return False


def test_module_imports():
    pdir = _GI.under_project_dir()
    for dotpath in find_all_plain_modules(pdir):
        if _check_prefix(dotpath):
            print('importing', dotpath)
            importlib.import_module(dotpath)


if __name__ == '__main__':
    test_module_imports()
