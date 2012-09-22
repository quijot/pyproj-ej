#!/usr/bin/env python
# -*- coding: utf-8 -*-

def toDXF(xyz, dxf_file, layer='Puntos'):
    """
    Toma una lista de coordenadas xyz = [(x1,y1,z1), (x2,y2,z2), ... ] y genera
    un archivo formato DXF con nombre dxf_file con los puntos correspondientes
    a esas coordenadas en la layer 'Puntos'.
    """
    pf = open(dxf_file, 'w')
    pf.write('  0\nSECTION\n  2\nENTITIES\n')
    for p in xyz:
        pf.write('  0\nPOINT\n  8\n' + layer + 
                 '\n 10\n' + str(p[0]) + 
                 '\n 20\n' + str(p[1]) + 
                 '\n 30\n' + str(p[2]) + '\n')
    pf.write('  0\nENDSEC\n')
    pf.write('  0\nEOF\n')
    pf.close()

def coord2dict(coord_file, sep=','):
    """
    Toma un archivo con id, x, y[, z] y devuelve un diccionario
    {id1: (x1,y1,z1), id2: (x2,y2,z2), ...}
    """
    file_in = open(coord_file, 'r')
    ixyz = {}
    for entry in file_in:
        if not entry.startswith('#') and entry.strip() != '' \
          and entry.find(sep) != -1:
            coord = entry.strip().split(sep)
            point_id = coord[0]
            x = float(coord[1])
            y = float(coord[2])
            z = 0.0 if len(coord) < 4 else coord[3]
            ixyz.update({point_id: (x, y, z)})
    file_in.close()
    return ixyz

def coord2list(coord_file, sep=','):
    """
    Toma un archivo con id, x, y[, z] y devuelve una lista
    [(id1,x1,y1,z1), (id2,x2,y2,z2), ...]
    """
    file_in = open(coord_file, 'r')
    ixyz = []
    for entry in file_in:
        if not entry.startswith('#') and entry.strip() != '' \
          and entry.find(sep) != -1:
            coord = entry.strip().split(sep)
            point_id = coord[0]
            x = float(coord[1])
            y = float(coord[2])
            z = 0.0 if len(coord) < 4 else coord[3]
            ixyz.append((point_id, x, y, z))
    file_in.close()
    return ixyz

def coord2dxf(coord_file, dxf_file=''):
    """
    Toma un archivo con id, x, y[, z] y devuelve un archivo formato DXF con
    nombre dxf_file con los puntos correspondientes a esas coordenadas en la
    layer (capa) 'Puntos'.
    """
    # rearma la lista pero sin punto_id
    # i[1:len(i)] # toma del segundo al último elemento de la lista i
    # en este caso significa que ignora id y toma x,y,z 
    l = [i[1:len(i)] for i in coord2list(coord_file)]
    dxf_file = dxf_file if dxf_file != '' else coord_file + '.dxf'
    toDXF(l, dxf_file)

