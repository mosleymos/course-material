#! /usr/bin/python
# -*- coding:utf-8 -*-

print(reduce(lambda x,y : x+y, map(chr, range(97,123))))
