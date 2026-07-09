import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def pridobi_orglarje(driver):
    driver.get(f"https://orgle.si/osebe")

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "vsebina"))
    )

    # Pridobivanje potrebnih spletnih elementov za zajemanje podatkov
    iframe = driver.find_element(By.NAME, "vsebina")
    driver.switch_to.frame(iframe)

    tabela_orglarjev = driver.find_element(By.ID, "OS")

    stevilo_zapisov = Select(driver.find_element(By.ID, "slcResults_OS"))
    stevilo_zapisov.select_by_value("50")

    naslednja_stran = driver.find_element(By.CLASS_NAME, "nextPage")

    orglarji = []

    # Zajemanje podatkov iz tabele orglarjev razporejene čez 4 strani
    for _ in range(4):
        orglarji_stran = tabela_orglarjev.find_elements(By.XPATH, ".//tbody/tr")

        # Odstranitev skritih orglarjev iz seznama
        orglarji_stran = [o for o in orglarji_stran if o.text != ""]

        # Urejanje podatkov v berljivo obliko
        for orglar_vrstica in orglarji_stran:

            # Zajemanje podatkov o orglarju
            orglar_ = [o.text.strip() for o in orglar_vrstica.find_elements(By.XPATH, ".//td")]

            orglar = {}

            # Kratek naziv
            orglar["kratek_naziv"] = orglar_[0]

            # Drugi nazivi (celo ime, drugi zapisi imena, sodelavci, nasledniki ...)
            orglar["drugi_nazivi"] = orglar_[1].replace(';', ',').replace('=', '').split(", ")

            # Obdobje in obmocja delovanja
            obdobje, obmocja = re.search(r"(.*?)\s+\((.*)\)", orglar_[2]).groups()

            orglar["obdobje"] = re.search(r"(.*)-(.*)", obdobje.replace('–', '-')).groups()
            orglar["obmocje"] = obmocja.split(", ")

            # Seznam strani, kjer je oseba omenjena.
            strani_ = orglar_[-1].replace('–', '-').split(", ")
            
            strani = []

            for s in strani_:
                if s == "":
                    continue

                if '-' in s:
                    s1, s2 = s.split('-')
                    strani.extend(list(range(int(s1), int(s2)+1)))
                else:
                  strani.append(int(s))
            
            orglar["strani"] = strani

            # Dodajanje orglarja v koncni seznam vseh orglarjev
            orglarji.append(orglar)

        naslednja_stran.click()

    return orglarji


def pridobi_podatke():

    # Uvodna nastavitev brskalnika za zajemanje podatkov
    nastavitve = Options()
    nastavitve.add_argument("--headless")

    driver = webdriver.Chrome(options=nastavitve)

    # Pridobitev podatkov
    orglarji = pridobi_orglarje(driver)

    driver.quit()

    return orglarji