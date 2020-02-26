# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-02-26 10:33:48
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-02-26 11:38:32
import glob
import os
import sys
import fileinput
import pathlib
import tempfile
import shutil

from progress.bar import Bar

SEP = os.sep
FILE_SUFFIX = "py"

def remove_linespace(dir_path):

    pattern = f"{dir_path}{SEP}**{SEP}*.{FILE_SUFFIX}"
    target_files = glob.glob(pattern, recursive=True)

    if len(target_files) == 0:
        print(f"[-] Target folder({dir_path}) is empty")
        sys.exit(1)

    with Bar("Removing linespace: ", fill="=", max=len(target_files), suffix="%(percent)d%%") as bar:
        for file in target_files:
            
            fd, temp_file_path = tempfile.mkstemp()
            os.close(fd)

            with open(temp_file_path, 'w', encoding="utf-8") as t:
                with fileinput.FileInput(file, openhook=fileinput.hook_encoded("utf-8")) as input_file:
                    for line in input_file:
                        if line == "\n":
                            pass
                        else:
                            t.write(line)

            pathlib.Path(file).unlink()
            shutil.copyfile(temp_file_path, file)

            bar.next(1)
        bar.finish()

    empty_lines = 0
    with Bar("Checking: ", fill="=", max=len(target_files), suffix="%(percent)d%%") as bar:
        for file in target_files:
            with open(file, "r", encoding="utf-8") as f:
                linenumber = 0
                for line in f.readlines():
                    linenumber += 1
                    if line == "\n":
                        print(f"[-] {file} line({linenumber}) is empty!")
                        empty_lines += 1
            bar.next(1)
        bar.finish()

    if empty_lines == 0:
        print("[+] Finish remove linespaces")
