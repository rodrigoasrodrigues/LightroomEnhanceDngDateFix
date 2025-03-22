import sys
import exiftool
import os
import pprint
import argparse

def fix_date(filepath, date, fieldName, dryrun):
    print("Fixing date in file: " + filepath + " to: " + date)
    if not dryrun:
        set_date(filepath, fieldName, date)
    
def get_date(filepath, fieldName):
    "gets date from dng file"
    with exiftool.ExifToolHelper() as et:
        metadata = et.get_metadata(filepath)[0]
        return metadata[fieldName]
        
def set_date(filepath, fieldName, date):
    "sets date in dng file"
    with exiftool.ExifToolHelper() as et:
        et.execute(f"-{fieldName}=" + date, filepath)
        print(f"{fieldName} set to: " + date)
        et.terminate()

def file_exists(filepath):
    return os.path.isfile(filepath)

def get_original_filename(filepath, suffix):
    parts = filepath.split(suffix)
    ogfile = "".join(parts)
    return ogfile

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='ProgramName',
        description='What the program does',
        epilog='Text at the bottom of help'
        )
    parser.add_argument('--input', help='Input path', required=True)
    parser.add_argument('--suffix', help='Suffix for the new files (e.g: -Enhanced-NR)', required=True)
    parser.add_argument('--dryrun', help='Display changes but do not alter the files', action='store_true')
    parser.add_argument('--fieldName', help='Field to change, default=EXIF:DateTimeOriginal', required=False, default='EXIF:DateTimeOriginal')

    args = parser.parse_args()

    file_list = []
    for root, dirs, files in os.walk(args.input):
        for file in files:
            if file.lower().endswith(args.suffix.lower()+".dng"):
                file_list.append(os.path.join(root, file))
    total_files = len(file_list)
    i = 0
    for file in file_list:
        i += 1
        ogfile = get_original_filename(file, args.suffix)
        if file_exists(ogfile):
            current_date = get_date(file, args.fieldName)
            original_date = get_date(ogfile, args.fieldName)
            if current_date != original_date:
                print("Dates are different: " + current_date + "(new) != " + original_date +"(original) | (" + str(i) + "/" + str(total_files) + ")")
                fix_date(file, original_date, args.fieldName, args.dryrun)
            else:
                if i % 100 == 0:
                    print("Dates are the same: " + current_date + " | (" + str(i) + "/" + str(total_files) + ")")
        else:
            print("original file not found: " + file)
