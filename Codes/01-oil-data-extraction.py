##Data extraction module for oil well raw data
##Set working directory to where you have this code before execution
#%reset -f
import numpy as np
import zipfile as zf ,os
import pandas as pd
import rarfile as rf,unrar
rf.UNRAR_TOOL='C:/Program Files/WinRAR/rar.EXE'


#Location of raw data
ziploc = '../Files/oil-wells-raw-data'
list_of_files = pd.Series(os.listdir(ziploc))
list_of_files = list_of_files[list_of_files.str.contains('.zip|.rar')]

##Blank datasets for well headers
well_columns = ['WELLID','WELLNAME','LEASE','API','SURFACELATITUDE',\
                'SURFACELONGITUDE','BOTTOMHOLELATITUDE','BOTTOMHOLELONGITUDE',\
                'COUNTRY','COUNTY','STATE','CURRENTOPERATOR',\
                'ORIGINALOPERATOR','WELLSTATUS','WELLTYPE','FIELD',\
                'WELLBOREPROFILE','GRID1','GRID2','GRID3','GRID4','GRID5',\
                'TOTALDEPTH','TRUEVERTICALDEPTH','LATERALLENGTH','DFELEVATION',\
                'GLELEVATION','KBELEVATION','DATEMODIFIED','FIRSTPRODDATE',\
                'LOGDATE','PERMITDATE','PLUGDATE','SPUDDATE','TESTDATE',\
                'CUMULATIVEGASPRODUCTION','CUMULATIVEOILPRODUCTION',\
                'CUMULATIVEWATERPRODUCTION','HASCORE','HASFILE','HASLOG',\
                'HASPERF','HASPRODUCTION','HASSAMPLE','HASTOP']

well_header = pd.DataFrame( np.arange(45).reshape((1,45)), \
                columns = well_columns)
well_header.astype(str)


#Processing production summary and production data
for a_file in list_of_files:
    if '.zip' in a_file:
        a_zipfile = zf.ZipFile("{}/{}".format(ziploc,a_file),'r')
        contentlist = a_zipfile.namelist()
    else:
        a_zipfile = rf.RarFile("{}/{}".format(ziploc,a_file),'r')
        contentlist = a_zipfile.namelist()[:-1]
    for content_file in contentlist:
        with a_zipfile.open(content_file) as f:
            try:
                if 'Summary' in content_file:
                    prod_summ = prod_summ.append(pd.read_csv(f),ignore_index = True)
                else:
                    if 'Head' not in content_file:
                        prod = prod.append(pd.read_csv(f),ignore_index = True)
            except:
                if 'Summary' in content_file:
                    prod_summ = pd.read_csv(f)
                else:
                    if 'Head' not in content_file:
                        prod = pd.read_csv(f)


##Processing well header data
for a_file in list_of_files:
    if '.zip' in a_file:
        a_zipfile = zf.ZipFile("{}/{}".format(ziploc,a_file),'r')
        contentlist = a_zipfile.namelist()
    else:
        a_zipfile = rf.RarFile("{}/{}".format(ziploc,a_file),'r')
        contentlist = a_zipfile.namelist()[:-1]
    for content_file in contentlist:
        if 'Head' in content_file:
            with a_zipfile.open(content_file) as f:
                with open('../Files/oil-wells-raw-data/well_temp','w') as f2:
                    for line in f:
                        line = line.replace('","',"'|'")
                        line = list(line)
                        line[0],line[-2] = "'","'"
                        line = ''.join(line)
                        f2.write(line)
            well_header = well_header.append(\
                        pd.read_csv('../Files/oil-wells-raw-data/well_temp',\
                                    sep = '|',skiprows = [0], header = None,\
                                    names = well_columns,engine = 'python'),\
                                    ignore_index= True)


#Exporting after duplicates
well_header.ix[1:]\
           .applymap(lambda x: x.strip('\''))\
           .drop_duplicates()\
           .to_csv('../Files/processed-data/well_header.csv',index = False,
                header= True)

prod.drop_duplicates().to_csv('../Files/processed-data/prod.csv',\
                                index = False,header= True)
prod_summ.drop_duplicates().to_csv('../Files/processed-data/prod_summ.csv',\
                                index = False,header= True)