##Data extraction module for oil well raw data
##Set working directory to where you have this code before execution

import zipfile,os
import pandas as pd


ziploc = '..\\Files\\oil-wells-raw-data'
zipfilelist = os.listdir(ziploc)

print 'zip file list'
print zipfilelist

zf = zipfile.ZipFile( '{}\\{}'.format(ziploc,zipfilelist[0])   ,'r')

print 'sample zip file contents'
print zf.namelist()

for filename in zf.namelist():
    with zf.open(filename) as f:
        if 'Summary' in filename:
            prod_summ = pd.read_csv(f)
        else:
            if 'Head' in filename:
                well_headers = pd.read_csv(f)
            else:
                prod = pd.read_csv(f)

print 'output data snaps'
print prod_summ.head()
print well_headers.head()
print prod.head()