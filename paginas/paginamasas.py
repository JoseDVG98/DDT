from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class ConversorMasas:

    def __init__(self, driver):
        self.driver=driver

    def ingresarValor(self,valor):
        campoValor=self.driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[1]/div/div[4]/form/input")
        campoValor.send_keys(valor)

    def ingresarMasaInicial(self,valor):
        lista=self.driver.find_element(By.XPATH, "//*[@id='from_weight']")
        lista=Select(lista)
        lista.select_by_visible_text(valor)

    def ingresarMasaFinal(self,valor):
        lista=self.driver.find_element(By.XPATH, "//*[@id='to_weight']")
        lista = Select(lista)
        lista.select_by_visible_text(valor)

    def vaciarCampo(self):
        campoValor = self.driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[1]/div/div[4]/form/input")
        campoValor.clear()

    def resultadoConversion(self):
        resultado=self.driver.find_element(By.XPATH, "//div[@id='div_weight']/b")
        return resultado.text







