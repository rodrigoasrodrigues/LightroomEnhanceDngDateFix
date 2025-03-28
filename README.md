# Lightroom Enhanced Dng DateFix

This is a simple script that fixes dngs created by lightroom's enhance feature by matching the date on the original dng with the new ones.

## Why do I need this?

When using the Enhance feature, or the Denoise AI on Lightroom, a new DNG file is created, this file does not keep the original capture date of the source image, instead it assumed the date and time of the enhance feature processing, meaning that anything that depends on the date for ordering (such as Google Photos or even the sort by date on lightroom itself) will be out of order.
This script fix that by altering the metadata on the enhanced files to match the original material.

## How to use it

1. Download and install [python](https://www.python.org/downloads/) if you don't have it (instructions will depend on you system)

2. Download the script and requirements.txt

3. **BACKUP YOUR FILES BEFORE RUNNING THE SCRIPT**

4. Install the required dependencies with pip (in a terminal at the download folder):

```{bash}
pip install -r ./requirements.txt
```

5. Run the script using the desired parameters.

Examples:

```{bash}
python .\fixdates.py --input "D:\RAW\Lightroom\2024\2024-12-08 - Churrasco"
```
or

```{bash}
python .\fixdates.py --input "D:\RAW\Lightroom\2024\2024-12-19 - Ballet Alice" --suffix="-Aprimorado-NR" --dryrun
```

## Parameters

| Parameter   | Meaning                                                          | Required |
| ----------- | ---------------------------------------------------------------- | -------- |
| --input     | Input path with the dng files                                    | Yes      |
| --suffix    | Suffix for the files generated by Ai Enhance (e.g: -Enhanced-NR) | Yes      |
| --dryrun    | Display changes but do not alter the files                       | No       |
| --fieldName | Field to change, default=EXIF:DateTimeOriginal                   | No       |
