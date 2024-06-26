# csv_fixer

Fixes CSV files from Excel for uploading to gobricks.cn

When CSV files from the Lego design program [Studio](https://www.bricklink.com/v3/studio/download.page) are edited in Microsoft Excel, the resulting CSV files have changes (messed up line endings and a missing newline at the end of the file) that break the CSV parser on [gobricks.cn](https://gobricks.cn).  Running the CSV file through this program should fix the file for successful import to gobricks.

## Usage:

```
python3 csv_fixer.py filename.csv
```

where `filename.csv` is the name of the file you want to fix.  The fixed file will be saved in the same directory as the python code with the name `filename_FIXED.csv`.

To build the MacOS "droplet" application, install py2app using

```
pip3 install py2app
```

then build the app by running

```
python3 setup.py py2app
```

If all goes well, the application will be created inside a `dist` subfolder.  Drag your CSV file onto that application to process it.