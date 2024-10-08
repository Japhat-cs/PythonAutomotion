import pyautogui
import time
import pandas as pd

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write(str(link))
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=1194, y=346)
pyautogui.write("brunoloco@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhaloca")
pyautogui.press("tab")
pyautogui.press("enter")

tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=1222, y=240)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(500)
    pyautogui.click(x=1222, y=240)
