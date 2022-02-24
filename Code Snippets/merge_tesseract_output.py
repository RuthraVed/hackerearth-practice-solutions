#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Abhishek Dev
# Created Date: 24th Feb 2022
# version = '1.0'
# ---------------------------------------------------------------------------
""" 
The is a utility script to merge Tesseract HOCR files into .html.

To use the script, please provide with a single .zip file containing the HOCRs or 
a directory of multiple HOCR zip files.

Usage: path/to/merge_tesseract_output.py <dir_path/hocr.zip> --output <output_dir:opt.> --verbosity <verbose_flag:opt.>

"""
from zipfile import ZipFile
from pathlib import Path
import shutil
import argparse


def create_output_path_folder(output_path=""):
    # Deciding the output path
    # Whatever be the path, the outputs will always be inside folder "zip_contents_merged_output"
    if not output_path:
        output_path = Path.cwd() / 'zip_contents_merged_output'
    else:
        output_path = Path(output_path) / 'zip_contents_merged_output'
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path


def merge_zip_contents(zip_path, output_path="", verbose_flag=""):
    output_path = create_output_path_folder(output_path) if not output_path else output_path

    zip_file_name = Path(zip_path).stem
    # Opening the given zip file
    with ZipFile(zip_path, mode='r') as zip_obj:
        number_of_files = len(zip_obj.namelist())

        for i in range(1, number_of_files + 1):
            inner_file = zip_file_name + '-' + str(i) + '.cleaned.hocr'
            if verbose_flag == 'v':
                print(f'Merging... {inner_file}')
            contents = zip_obj.read(inner_file)
            merge_file_name = output_path / Path(zip_file_name + '.html')
            with open(merge_file_name, mode='ab') as out_file:
                out_file.write(contents)


def multiple_zips_merge(dir_path, output_path="", verbose_flag=""):
    output_path = create_output_path_folder(output_path)
    dir_path = Path(dir_path)
    if dir_path.is_file() and dir_path.name.split('.')[-1] == 'zip':
        merge_zip_contents(dir_path, output_path, verbose_flag)
    elif dir_path.is_dir():
        for file in dir_path.iterdir():
            if file.name.split('.')[-1] == 'zip':
                merge_zip_contents(file, output_path, verbose_flag)
            else:
                shutil.copy(file, output_path)
    else:
        raise FileNotFoundError()


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("dir_path", type=str,
                        help="Path to a single HOCR .zip file or a directory of multiple HOCR .zip files")
    parser.add_argument("--output", help="Specify a path to save the merged contents")
    parser.add_argument("--verbosity", help="increase output verbosity")
    args = parser.parse_args()

    multiple_zips_merge(dir_path=args.dir_path, output_path=args.output, verbose_flag=args.verbosity)
