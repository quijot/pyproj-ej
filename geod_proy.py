#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyproj
from gms_gyf import *

def config_proy(latitud_de_origen, meridiano_central, falso_este=0,
    falso_norte=0, factor_de_escala=1, datum='WGS84'):
    """Crea una proyeccion de tipo mercator transversal, con los siguientes
    parametros:
      latitud_de_origen     Latitud de origen
      meridiano_central     Meridiano central
      falso_este            Falso Este (0 por defecto, en metros)
      falso_norte           Falso Norte (0 por defecto, en metros)
      factor_de_escala      Factor de escala (1 por defecto)
      datum                 Datum, 'WGS84' por defecto (ver variable pj_ellps
      para otros datums posibles, ej: 'GRS80')
    """
    pmerct = pyproj.Proj(
        proj='tmerc',
        lat_0=latitud_de_origen,
        lon_0=meridiano_central,
        k=factor_de_escala,
        x_0=falso_norte,
        y_0=falso_este,
        ellps=datum)
    return pmerct


def proy2geod(archivo_de_coordenadas, proyeccion, separador=','):
    ext = '.geod'
    geod_proy(archivo_de_coordenadas, proyeccion, ext, True, separador)


def geod2proy(archivo_de_coordenadas, proyeccion, separador=','):
    ext = '.proy'
    geod_proy(archivo_de_coordenadas, proyeccion, ext, False, separador)


def geod_proy(coord_file, proj, file_ext, inv, sep=','):
    file_in = open(coord_file, 'r')
    file_out = open(coord_file + file_ext, 'a')
    for entry in file_in:
      if not entry.startswith('#') and len(entry.strip()) != 0 \
        and entry.find(sep) != -1:
        coord_id, coord_in1, coord_in2 = entry.split(sep)
        if not inv:
          g1, m1, s1 = coord_in1.strip().split(' ')
          g2, m2, s2 = coord_in2.strip().split(' ')
          coord_in1 = gms2gyf(int(g1), int(m1), float(s1))
          coord_in2 = gms2gyf(int(g2), int(m2), float(s2))
        coord_out1, coord_out2 = proj(coord_in1, coord_in2, inverse=inv)
        if inv:
          g1, m1, s1 = gyf2gms(coord_out1)
          g2, m2, s2 = gyf2gms(coord_out2)
          coord_out1 = str(g1) + ' ' + str(m1) + ' ' + str(s1)
          coord_out2 = str(g2) + ' ' + str(m2) + ' ' + str(s2)
        file_out.write(str(coord_id) + sep + str(coord_out1) \
          + sep + str(coord_out2) + '\n')
    file_in.close()
    file_out.close()

