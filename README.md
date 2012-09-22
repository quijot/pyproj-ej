# pyProj-ej

__pyProj-ej__ utiliza [pyproj][pp] para realizar algunas operaciones con
 coordenadas.

[pyproj][pp] es una interfaz [Python][py] de la librería de proyecciones
 cartográficas [PROJ.4][proj].

# Instalación

[Descargar](https://github.com/quijot/pyproj-ej/zipball/master) y descomprimir.

## Requisitos previos

En teoría es multiplataforma, es decir que funciona tanto en win como en
 GNU/Linux si tenés instalados: [Python][py], [NumPy][np] y [pyproj][pp].
 Recomendado extra: [iPython][ipy].

Para instalarlos en Debian/Ubuntu/Mint/Tuquito/etc.

    $ sudo apt-get install python python-numpy python-pyproj ipython

# Uso

A través del intérprete python (recomendado [iPython][ipy]). Conviene ejecutarlo
 desde dentro del directorio de pyproj-ej:

    $ python

o si tenés ipython instaldo:

    $ ipython

## Módulo gms_gyf

Funcionalidad de conversión entre grados sexagesimales (gº m' s.sss") y grados
 y fracción (g.ggg):

    from gms_gyf import *
    gms2gyf(grados, minutos, segundos)
    gyf2gms(grados_y_fraccion)

### Ejemplos

    gms2gyf(-61,30) = -61.5
    gms2gyf(0,-45)  = -0.75
    gms2gyf(-33)    = -33.0
    gyf2gms(-61.5)  = (-61,30,0.0)
    gyf2gms(-0.75)  = (0,-45,0.0)

## Módulo geod_proy

Configuración de la proyección (tipo mercator transversal):

    import geod_proy as gp
    proy = gp.config_proy(latitud_de_origen, meridiano_central, falso_este, falso_norte, factor_de_escala, datum)

### Ejemplo

Leer y ejecutar el archivo de pruebas __test.py__. Allí se detallan los pasos
 de varios ejemplos. Para ejecutarlo desde el directorio donde se encuentra:

    $ ./test.py

### Set de archivos de ejemplo

El directorio [__coord__][coord_ej] contiene archivos con coordenadas de un caso
 real.

Se obtuvieron a partir del archivo __proy__ a través de una serie de
 transformaciones que demuestran su reciprocidad. Dentro del script __test.py__
 se explican los pasos realizados.

# Licencia (a.k.a. _pagate una birra_)

__pyProj-ej__ se encuentra bajo los términos de la Beer-ware License (Revision 42).
Para mayor información leer
[LICENSE](https://raw.github.com/quijot/pyproj-ej/master/LICENSE).

[py]: http://www.python.org/ "Python Programming Language"
[pp]: https://code.google.com/p/pyproj/ "pyproj: Pyrex generated python interface to PROJ.4 library"
[proj]: http://trac.osgeo.org/proj/ "PROJ.4 - Cartographic Projections Library"
[np]: http://numpy.scipy.org/ "NumPy is the fundamental package for scientific computing with Python"
[ipy]: http://ipython.org/
[coord_ej]: https://github.com/quijot/pyproj-ej/tree/master/coord "Set de archivos de ejemplo."
