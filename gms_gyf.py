#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Funciones de conversión entre (grados, minutos, segundos) sexagesimales y
# grados y fracción.

from numpy import sign, trunc, abs


def gms2gdec(grados, minutos=0, segundos=0):
    """Conversion (gg,mm,ss.sssss) --> (g.gggggg)
    Por ejemplo:
        gms2gdec(-61,30)          = -61.5
        gms2gdec(-32,45,22.22222) = -32.xxxxxxxx
        gms2gdec(-33)             = -33.0"""
    s = sign(grados)
    signo = 1 if s == 0 else s
    return signo * (signo * grados + minutos / 60.0 + segundos / 3600.0)


def gdec2gms(gdec):
    """Conversion (g.gggggg) --> (gg,mm,ss.sssss)
    Por ejemplo: gdec2gms(61.5) = (61,30)"""
    # hacer las cuentas
    g = trunc(gdec)
    m = (gdec - g) * 60
    s = (m - trunc(m)) * 60
    # preparar la presentación
    g = int(g)
    m = int(m) if g == 0 else int(abs(m))
    s = abs(s) if m != 0 else s
    return (g, m, s)


def gdec2gms_list(gdec_list):
    """Conversion (g0.ggg,g1.ggg) --> ((g0,mm,ss.sss),(g1,mm,ss.sss)) masiva.
    Por ejemplo: gdec_list = [(-61.5,-31.456),(-63.456,31.3333)]"""
    gms_list = []
    for i in gdec_list:
        gms_list.append((gdec2gms(i[0]), gdec2gms(i[1])))
    return gms_list


def gms2gdec_list(gms_list):
    """Conversion ((g0,mm,ss.sss),(g1,mm,ss.sss)) --> (g0.ggg,g1.ggg) masiva.
    Por ejemplo:
    gms_list = [((-61,30),(-31,45)),((-63,45),(31,20))]"""
    gdec_list = []
    for i in gms_list:
        gdec_list.append((gms2gdec(*i[0]), gms2gdec(*i[1])))
    return gdec_list

