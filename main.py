import pandas as pd

from orodja.zapisovanje_podatkov import zapisi_orglarje_v_csv
from orodja.filtriranje_podatkov import *

SLOVENSKA_OBMOCJA = ["CE", "NM", "GO", "KO", "LJ", "MB"]

zapisi_orglarje_v_csv()
csv = pd.read_csv('podatki/orglarji.csv')

# Primer
print(pridobi_orglarje_v_obmocjih(csv, SLOVENSKA_OBMOCJA))