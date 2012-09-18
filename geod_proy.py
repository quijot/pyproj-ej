#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyproj as pp
import gms_gdec as gg


def configurar_proyeccion(lat0, lon0, fesc=1, x0=0, y0=0, datum='WGS84'):
    """Crea una proyeccion de tipo mercator transversal, con los siguientes
    parametros, por ejemplo:
      lat0 = gms(-31,44,30) Latitud de origen = 31º 44' 30" S
      lon0 = gms(-61,14)    Meridiano de tangencia = 61º 14' 00" W
      fesc = 1              Factor de escala (1 por defecto)
      x0 = 0                Falso Norte (0 por defecto, en metros)
      y0 = 0                Falso Este (0 por defecto, en metros)
      datum = 'WGS84'       Datum (ver variable pj_ellps) (WGS84 por defecto)
      proy = 'tmerc'        Tipo de proyección (ver pj_list) (tmerc por defecto)
    """
    pmerct = pp.Proj(
        proj='tmerc',
        lat_0=lat0,
        lon_0=lon0,
        k=fesc,
        x_0=x0,
        y_0=y0,
        ellps=datum)
    return pmerct


def proy2geod(coord_proy, proy):
    coord_geod = []
    for i in coord_proy:
        coord_geod.append(proy(i[0], i[1], inverse=True))
    return coord_geod


# Otra opción: Al revés
# Transformar de geodésicas a proyectadas
# Cargar las coordenadas expresadas en geodésicas.
# En pares (lon, lat):
#   Pueden ser directamente en grados y fracción o en grados sexagesimales
# Por ejemplo:
#   coord_geod = [(gg.ggggº, gg.ggggº), (gg.ggggº, gg.ggggº), ...]
#   ó
#   coord_geod = [(gms(g0,mm,ss.sss), gms(g0,mm,ss.sss)), ...]
def geod2proy(coord_geod, proy):
    coord_proy = []
    for i in coord_geod:
        coord_proy.append(proy(i[0], i[1]))
    return coord_proy

