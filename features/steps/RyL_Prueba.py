from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('Abro el navegador')
def abrirNavegador(context):
    context.driver = webdriver.Chrome("C:\dchrome\chromedriver.exe")

@when('Ingreso a la página de registro')
def IngresoPagina(context):
    context.driver.get("https://buggy.justtestit.org/")
    time.sleep(3)
    
@when('Selecciono la opcion Register')
def Clic(context):
    context.driver.find_element(By.CSS_SELECTOR, '.btn.btn-success-outline').click()
    time.sleep(3)

@when('Diligencio el campo Login identificado con el selector "{SELECTOR}" con el valor "{VALOR}"')
def Usuario(context, SELECTOR, VALOR):
    context.driver.find_element(By.CSS_SELECTOR, SELECTOR).send_keys(VALOR)

@when('Diligencio el campo First Name identificado con el selector "{SELECTOR}" con el valor "{VALOR}"')
def Usuario(context, SELECTOR, VALOR):
    context.driver.find_element(By.CSS_SELECTOR, SELECTOR).send_keys(VALOR)

@when('Diligencio el campo Last Name identificado con el selector "{SELECTOR}" con el valor "{VALOR}"')
def Usuario(context, SELECTOR, VALOR):
    context.driver.find_element(By.CSS_SELECTOR, SELECTOR).send_keys(VALOR)

@when('Diligencio el campo Password identificado con el selector "{SELECTOR}" con el valor "{VALOR}"')
def Usuario(context, SELECTOR, VALOR):
    context.driver.find_element(By.CSS_SELECTOR, SELECTOR).send_keys(VALOR)

@when('Diligencio el campo Confirm Password identificado con el selector "{SELECTOR}" con el valor "{VALOR}"')
def Usuario(context, SELECTOR, VALOR):
    context.driver.find_element(By.CSS_SELECTOR, SELECTOR).send_keys(VALOR)
    time.sleep(5)
      
@then('Hago clic en el boton Register')
def Clic(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(5)

@then('Diligencio el User identificado con el selector "{SELECTOR}" con el valor "{VALOR}"')
def Usuario(context, SELECTOR, VALOR):
    context.driver.find_element(By.CSS_SELECTOR, SELECTOR).send_keys(VALOR)

@then('Diligencio el Password identificado con el selector "{SELECTOR}" con el valor "{VALOR}"')
def Usuario(context, SELECTOR, VALOR):
    context.driver.find_element(By.CSS_SELECTOR, SELECTOR).send_keys(VALOR)
    time.sleep(2)
      
@then('Hago clic en el botón Login')
def Clic(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-success"]').click()
    time.sleep(5)


# @then('Veo la pantalla de inicio')
# def Verificacion(context):
#     elemento = context.driver.find_element(By.XPATH, "//span[@class='label label-warning']")
#     assert elemento.is_displayed()
#     context.driver.close()
    

