from playwright.sync_api import sync_playwright
import time
import pyautogui
import requests

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto('https://www.google.com.br')
    time.sleep(1)
    pagina.fill('xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input', "relatorio magazine luiza")
    time.sleep(1)
    pagina.locator('xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]').click()
    time.sleep(1)
    pagina.locator('xpath=//*[@id="rso"]/div[1]/div/div/div/div[1]/div/div/div[1]/div/a/h3').click()
    time.sleep(1)
    pagina.locator('xpath=//*[@id="splash"]/div[1]/a/img').click()
    time.sleep(2)
    pagina.locator('xpath=//*[@id="accordionExample"]/div[1]/button').click()
    time.sleep(2)
    pagina.locator('xpath=//*[@id="collapse-1"]/div/ul/li[1]').click()
    time.sleep(2)
    pagina.locator('xpath=//*[@id="collapse-1"]/div/ul/li[1]').click()
    time.sleep(2)
    pagina.locator('xpath=//*[@id="d2xbRw4t5VlHNlNLv23TWQ=="]').click()
    time.sleep(40)
    pagina.locator('xpath=//*[@id="maskedImage"]').click()
    time.sleep(2)

