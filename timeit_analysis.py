# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-02-25 11:24:53
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-02-26 10:34:24
import timeit

t = timeit.Timer("input_analysis(r'F:\\git')", "from obfuscator_analysis import input_analysis")
print(t.timeit(number=1000))