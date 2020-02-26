# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-02-25 10:42:10
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-02-26 10:54:37
import pathlib

from obfuscator_remove import remove_linespace

from obfuscator_analysis import input_analysis
from obfuscator_analysis import output_analysis


if __name__ == "__main__":
    input_dir_path = input("Input the dir you wanna obfuscate: ")
    input_dir_path = pathlib.Path(input_dir_path).resolve()
    input_dir_path = str(input_dir_path)
    input_analysis(input_dir_path, True)

    output_dir_path = input("Input the output dir: ")
    output_dir_path = pathlib.Path(output_dir_path).resolve()
    output_dir_path = str(output_dir_path)
    output_analysis(input_dir_path, output_dir_path, True)

    remove_linespace(output_dir_path)