# -*- coding: utf-8 -*-
import re


def str2unicode(str):
    # str='你好'
    res = (re.sub('.', lambda x: r'\u%04X' % ord(x.group()), str))
    return res


def unicode2str(unicode):
    # unicode = b'\\u4f60\\u597d'
    # unicode = b'\u4f60\u597d'
    res = unicode.decode("unicode_escape")
    return res


if __name__ == '__main__':
    str = '123'
    print(str2unicode(str))
    unicode = b'\u0031\u0032\u0033'
    print(unicode2str(unicode))
