import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def normaliziraj_obdobje(zacetek, konec):
    match konec:
        case "":
            konec = zacetek
        case '>':
            # Maksimum leta delovanja je letnica izida knjige
            konec = '2018'

    return {
        "zacetek_aktivnosti": int(zacetek.replace('*', '')),
        "konec_aktivnosti": int(konec.replace('*', '')),
        "domneven_zacetek": '*' in zacetek,
        "domneven_konec": '*' in konec
    }


def normaliziraj_strani(strani_):
    strani = []

    for s in strani_:
        if s == "":
            continue

        if '-' in s:
            s1, s2 = s.split('-')
            strani.extend(list(range(int(s1), int(s2)+1)))
        else:
            strani.append(int(s))
    
    return strani


def pridobi_orglarje():
    nastavitve = Options()
    nastavitve.add_argument("--headless")

    driver = webdriver.Chrome(options=nastavitve)
    driver.get(f"https://orgle.si/osebe")

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "vsebina"))
    )

    # Pridobivanje potrebnih spletnih elementov za zajemanje podatkov
    iframe = driver.find_element(By.NAME, "vsebina")
    driver.switch_to.frame(iframe)

    tabela = driver.find_element(By.ID, "OS")

    stevilo_zapisov = Select(driver.find_element(By.ID, "slcResults_OS"))
    stevilo_zapisov.select_by_value("50")

    naslednja_stran = driver.find_element(By.CLASS_NAME, "nextPage")

    orglarji = []

    # Zajemanje podatkov iz tabele orglarjev razporejene čez 4 strani
    for _ in range(4):
        orglarji_tabela = tabela.find_elements(By.XPATH, ".//tbody/tr")

        # Odstranitev skritih orglarjev iz seznama
        orglarji_tabela = [o for o in orglarji_tabela if o.text != ""]

        # Urejanje podatkov v berljivo obliko
        for orglar_vrstica in orglarji_tabela:

            # Zajemanje podatkov o orglarju
            orglar_ = [o.text.strip() for o in orglar_vrstica.find_elements(By.XPATH, ".//td")]

            orglar = {}

            # Kratek naziv
            orglar["kratek_naziv"] = orglar_[0]

            # Drugi nazivi (celo ime, drugi zapisi imena, sodelavci, nasledniki ...)
            orglar["drugi_nazivi"] = orglar_[1].replace(';', ',').replace('=', '').split(", ")

            # Obdobje in območja delovanja
            obdobje_, obmocja_ = re.search(r"(.*?)\s+\((.*)\)", orglar_[2]).groups()

            obdobje_ = obdobje_.replace('–', '-')
            obdobje_ = re.search(r"(.*)-(.*)", obdobje_).groups()
            orglar.update(normaliziraj_obdobje(obdobje_[0], obdobje_[1]))

            orglar["obmocja_delovanja"] = obmocja_.split(", ")
            
            # Strani z omembo orglarja v knjigi
            strani_ = orglar_[-1].replace('–', '-').split(", ")
            orglar["strani_z_omembo"] = normaliziraj_strani(strani_)

            orglarji.append(orglar)

        naslednja_stran.click()

    driver.quit()

    return orglarji