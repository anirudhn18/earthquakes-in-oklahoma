##Data extraction module for oil well raw data
##Set working directory to where you have this code before execution
#%reset -f

import zipfile as zf ,os
import pandas as pd

#Location of raw data
ziploc = '..\\Files\\oil-wells-raw-data'
list_of_zipfiles = pd.Series(os.listdir(ziploc))
list_of_zipfiles = list_of_zipfiles[list_of_zipfiles.str.contains('.zip|.rar')]


for a_file in list_of_zipfiles:
    a_zipfile = zf.ZipFile("{}\\{}".format(ziploc,a_file),'r')
    for content_file in a_zipfile.namelist():
        with a_zipfile.open(content_file) as f:
            try:
                if 'Summary' in content_file:
                    prod_summ.append(pd.read_csv(f),ignore_index = False)
                else:
                    if 'Head' in content_file:
                        well_headers.append(pd.read_csv(f),ignore_index = False)
                    else:
                        prod.append(pd.read_csv(f),ignore_index = False)

            except:
                if 'Summary' in content_file:
                    prod_summ = pd.read_csv(f)
                else:
                    if 'Head' in content_file:
                        well_headers = pd.read_csv(f)
                    else:
                        prod = pd.read_csv(f)