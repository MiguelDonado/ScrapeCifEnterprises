from intro_func import get_enterprises, get_file_xlsx
from logic import get_cif_from_href, get_href_anchor_tag, put_name_desired_format
import time
import pandas as pd
import tkinter as tk
from tkinter import messagebox


def main():
    renderMessage()
    cifs = []
    file = get_file_xlsx()
    enterprises = get_enterprises(file)
    for enterprise in enterprises:
        try:
            href = get_href_anchor_tag(put_name_desired_format(enterprise))
            cif = get_cif_from_href(href)
        except:
            cif = "No encontrado"
        cifs.append(cif)
        time.sleep(5)
        print(enterprise)
    df = pd.DataFrame({"Nombre": enterprises, "CIF": cifs})
    df.to_excel("output.xlsx", index=False)


def renderMessage():
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning(
        "ATENCION!",
        "TENER CUIDADO CON EL CIF DE EMPRESAS EXTRANJERAS Y PERSONAS FISICAS. DEBE SER ELIMINADO DEL EXCEL FINAL",
    )


main()
