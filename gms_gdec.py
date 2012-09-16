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
    """Conversion (g.gggggg) --> (gg,mm,ss.sssss) masiva.
    Por ejemplo: gdec_list = [(-61.5,-31.456),(-63.456,31.3333)]"""
    r = []
    for i in gdec_list:
        r.append((gdec2gms(i[0]), gdec2gms(i[1])))
    return r

