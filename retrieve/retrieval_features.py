 """
 import required packages 
  
 """

from osgeo import ogr, osr, gdal
from netCDF4 import *
import numpy as np
import os,sys
from ecmwfapi import ECMWFDataServer
import pandas as pd
import re

def downloadFromEcmwf(bdate=None, edate=None):
    """
    downloadFromEcmwf - This procedure acquire a Param (Total Precipitation)
    from ECMWF saving it on a netcdf files
    
    """
    steps =  [360] #number of forecast hours
    steps = "/".join(["%d"%item for item in steps])
    edate = strftime("%Y-%m-%d",edate) 
    bdate = strftime("%Y-%m-%d",bdate) 

    if (edate>bdate):
        daterange = "%s/to/%s"%(bdate,edate)
        filenc = "./data/%s.nc"%(daterange.replace("/","-"))

        try:
            server = ECMWFDataServer()
            server.retrieve({
                "class": "ti",
                "dataset": "tigge",
                "date": daterange,
                "expver": "prod",
                "grid": "0.5/0.5",
                "levtype": "sfc",
                "origin": "ecmf",
                "param": "228228",#Total Precipitation
                "step": steps,
                "time": "12:00:00",
                "type": "cf",
                "area": "47.5/6.5/43.5/12.5",
                "format":"netcdf",
                "target": filenc,
            })
        except Exception as ex:
            text = "Download giornaliero del TIGGE per la variabile Ecmwf_tigge_P15 fallito causa:<%s>"%(ex)
            print(text)
            return False
    return True       


def averageOnArea(varname, filenc, fileshp):
    """
    averageOnArea - 
    This procedure interpolate data from ECMWF and average the param "varname"
    just on the basin defined in fileshp
    """
    ds    = ogr.Open(fileshp)
    layer = ds.GetLayer()
    N     = 100
    gt    = (6.25, 0.5/float(N), 0.0, 47.75, 0.0, -0.5/float(N))
    prj   = layer.GetSpatialRef().ExportToWkt()

    root = Dataset(filenc)
    m,n  = root.dimensions["latitude"].size,root.dimensions["longitude"].size
    #m,n = 9,13
    #xres,yres=130,90
    xres,yres = n*N,m*N
    #---------------------------------------------------------------------------
    #       Basin Mask by rasterize basin shape
    #---------------------------------------------------------------------------
    #Create a basin mask
    #ds_mask = gdal.GetDriverByName('GTiff').Create('tmp/mask.tif', xres, yres, 1, gdal.GDT_Float32)
    ds_mask = gdal.GetDriverByName('MEM').Create('', xres, yres, 1, gdal.GDT_Float32)
    ds_mask.SetGeoTransform(gt)
    ds_mask.SetProjection(prj)
    gdal.RasterizeLayer(ds_mask, (1,), layer, burn_values=[1.0])
    band = ds_mask.GetRasterBand(1)
    mask = band.ReadAsArray()
    countpixel = np.nansum(mask) #sum avoiding nan
    #---------------------------------------------------------------------------
    #       Read netcdf (.nc) file and make Average
    #---------------------------------------------------------------------------
    #Transform nc data ---> numpy matrix
    TIGGEvar = varname

    #Time steps
    days = root.variables["time"]
    D = len(days[:])

    for day in range(D):
        #Get just the last time-step (ts= 354) +15gg
        tigge = root.variables[TIGGEvar][day, :, :]
        #tigge_resampled = scipy.ndimage.zoom(tigge,N,order=1)

        #Adapt the size of tigge data by making no interpolation
        Ms,Ns = m*N,n*N
        tigge_resampled =np.ones((Ms,Ns))
        for i in range(Ms):
            for j in range(Ns):
                tigge_resampled[i,j] = tigge[i/N,j/N]
        #--------------------------------------------------------
        #Calculate avg
        avg    = np.nansum(tigge_resampled*mask)/countpixel
        timestamp = num2date(days[day],units=days.units,calendar=days.calendar)
        timestamp = timestamp - datetime.timedelta(hours=360)
        timestamp = strftime("%Y-%m-%d 00:00:00",timestamp)

        print(timestamp,avg)


def downloadFromFtp(fileconf):
    """
    This procedure download features from ftp 
    fileconf - file with credentials and ftp cofiguration
    """
    res = False
    ftp = FtpClient(fileconf)
    filenames = ftp.ls()
    filenames = [filename for filename in filenames if re.match(r'^featuresOf\d{8,8}\.csv$',filename,re.I)]
    filenames.sort()
    for j in range(len(filenames)):
        if not os.path.isfile("./data/%s"%filenames[j]):
            print("downloading %s"%(filenames[j]))
            filecsv = ftp.download(filenames[j],"./data")
            if os.path.isfile(filecsv):              
                df = pd.read_csv(filecsv,header=None,parse_dates =[1],engine="c")
                
    return False
