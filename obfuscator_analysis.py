# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-02-25 10:54:02
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-02-26 10:52:29
import os
import sys
import glob
import pathlib
import shutil
from time import ctime
from progress.bar import Bar

SEP = os.sep
FILE_SUFFIX = "py"

SIZE = "Size"
PERMISSIONS = "Permissions" 
OWNER = "Owner" 
DEVICE = "Device" 
CREATED = "Created" 
LAST_MODIFIED = "Last modified" 
LAST_ACCESSED = "Last accessed" 

def input_analysis(input_dir, verbose=False):
    '''
    1. gather all py files
    2. is there any py file empty
    3. show all not empty file information
    '''
    
    if not os.path.exists(input_dir):
        print(f'[-] {input_dir} not exists')

    pattern = f"{input_dir}{SEP}**{SEP}*.{FILE_SUFFIX}"

    files = glob.glob(pattern, recursive=True)

    input_files_found = []
    input_files_empty = []

    with Bar("Input Analysing: ", fill="=", max=len(files), suffix="%(percent)d%%") as bar:
        for file_path in files:
            file_info = pathlib.Path(file_path)
            file_stat = file_info.stat()

            if file_stat.st_size <= 0:
                # empty file
                input_files_empty += [file_path]
            else:
                # valid file
                input_files_info = {
                    SIZE : file_stat.st_size,
                    PERMISSIONS : file_stat.st_mode,
                    OWNER : file_stat.st_uid,
                    DEVICE : file_stat.st_dev,
                    CREATED : ctime(file_stat.st_ctime),
                    LAST_MODIFIED : ctime(file_stat.st_mtime),
                    LAST_ACCESSED : ctime(file_stat.st_atime),
                    }
                input_files_found += [(file_path, input_files_info)]

            bar.next(1)
        bar.finish()

    if verbose:
        if len(files) == 0:
            print(f"[*] {input_dir} is empty")

        print(f"{len(input_files_found)} none empty files found")
        print()

        for path, info in input_files_found:
            print(f"[*] {path}")
            print(f">   {SIZE}          : {info.get(SIZE)}")
            print(f">   {PERMISSIONS}   : {info.get(PERMISSIONS)}")
            print(f">   {OWNER}         : {info.get(OWNER)}")
            print(f">   {DEVICE}        : {info.get(DEVICE)}")
            print(f">   {CREATED}       : {info.get(CREATED)}")
            print(f">   {LAST_MODIFIED} : {info.get(LAST_MODIFIED)}")
            print(f">   {LAST_ACCESSED} : {info.get(LAST_ACCESSED)}")
            print()

        print(f"{len(input_files_empty)} empty files found")
        print()
        for path in input_files_empty:
            print(f"[*] {path} file is empty")
            print()

def output_analysis(input_dir, output_dir, verbose=False):
    '''
    1. is output dir exists, delete it
    2. copy input to output dir
    '''

    if os.path.exists(output_dir):
        remove_dir = input("[!] Output dir exists, do you want remove it? (y/n): ")
        if remove_dir.lower() != 'y':
            print("[-] Failed to remove output dir")
            sys.exit(1)
        shutil.rmtree(output_dir)

    shutil.copytree(input_dir, output_dir)

    input_analysis(output_dir, verbose)


