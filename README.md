## Python library for GIS and spatial stuff, plus miscellaneous functionality 
Python packages developed by the years as requirements for my different projects as GIS developer with `QGIS`, `ESRI`, `Oracle`, `Postgis`, and other technologies used in this kind of projects with spatial data.
### Package _extra_utils_
Packages and modules to deal with different problems commonly found in typical projects dealing with strings, mails, logging, sql, xml and others.

To install:
```shell script
pip install "git+https://github.com/ernestone/python_packages#egg=extra_utils&subdirectory=extra_utils_pckg"
```
### Package _spatial_utils_
Modules to deal with spatial data using common used libraries in this kind of projects like `OSGEO GDAL` (requires `GDAL` library C), `Geopandas`, `Shapely` and `Nodejs` packages to deal with `Topojsons` (requires `Nodejs` installed).

To install:
```shell script
pip install "git+https://github.com/ernestone/python_packages#egg=spatial_utils&subdirectory=spatial_utils_pckg"
```
### Package _cx_oracle_spatial_
Modules to connect to `Oracle` database and treat his objects in a `sqlalchemy` style but dealing with spatial data as one more type. Added the functionality of common used libraries in this kind of projects from the `spatial_utils` package to convert the `Oracle` data on different open source data types.

To install:
```shell script
pip install "git+https://github.com/ernestone/python_packages#egg=cx_oracle_spatial&subdirectory=cx_ora_spatial_pckg"
```