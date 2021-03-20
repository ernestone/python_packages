## Python library for GIS and spatial stuff, plus miscellaneous functionality 
Python packages developed by the years as requirements for my different projects as GIS developer with `QGIS`, `ESRI`, 
`Oracle`, `Postgis`, and other technologies used in this kind of projects with spatial data.
### Package _extra_utils_
Packages and modules used on different commonly problems founded in typical projects dealing with strings, mails, 
logging, sql, xml and others.

To install:
```shell script
pip install "git+https://github.com/ernestone/python_packages#egg=extra_utils&subdirectory=extra_utils_pckg"
```
### Package _spatial_utils_
Modules to deal with spatial data using common used spatial libraries as `Shapely`, 
`Topojsons` (requires `Nodejs` installed), ...

To install:
```shell script
pip install "git+https://github.com/ernestone/python_packages#egg=spatial_utils&subdirectory=spatial_utils_pckg"
```
### Package _osgeo_utils_
Modules to add common functionality to `OSGEO GDAL`. Requires `GDAL` library C previously installed 
(see how here https://gdal.org/download.html#binaries).

To install:
```shell script
pip install "git+https://github.com/ernestone/python_packages#egg=spatial_utils&subdirectory=spatial_utils_pckg"
```
### Package _cx_oracle_spatial_
Modules to connect to `Oracle` database and treat his objects in a `sqlalchemy` style but dealing with spatial data as 
one more type. Added the functionality of common used libraries in this kind of projects from the `osgeo_utils` and 
`spatial_utils` packages to convert the `Oracle` data on different open source spatial data types.

To install:
```shell script
pip install "git+https://github.com/ernestone/python_packages#egg=cx_oracle_spatial&subdirectory=cx_oracle_spatial_pckg"
```

F.A.Q:
If trying install _cx_oracle_spatial_ an error with `cx_oracle` occurred try pre-install it with this in your 
requirements:
```shell
pip install cx_Oracle<7 --upgrade
```
See details here https://cx-oracle.readthedocs.io/en/6.4.1/installation.html  

