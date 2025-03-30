import unittest
from time import sleep

from excel.excel import ArchivoExcel
from test.config import Config
from paginas.paginamasas import ConversorMasas



class TestConvertirMasas(Config):

    def testMasas (self):
        fil=2
        col=1
        pagina=ConversorMasas(self.driver)
        archivoExcel="unidades.xlsx"
        archivo=ArchivoExcel(archivoExcel)
        while(True):
            masaInicial=archivo.obtenerDatos(fil,col)
            masaFinal=archivo.obtenerDatos(fil,col+1)
            valor=archivo.obtenerDatos(fil,col+2)
            #print("{} {} {}".format(masaInicial, masaFinal, valor))
            if masaFinal and masaInicial and valor:
                pagina.ingresarValor(valor)
                pagina.ingresarMasaInicial(masaInicial)
                pagina.ingresarMasaFinal(masaFinal)
                sleep(5)
                resultado=pagina.resultadoConversion()
                archivo.modificarValor(fil,col+3, resultado)
                pagina.vaciarCampo()
                fil = fil + 1
            else:
                break











