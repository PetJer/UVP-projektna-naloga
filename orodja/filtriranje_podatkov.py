def pridobi_orglarje_v_obdobju(csv, zacetek, konec, celo_obdobje, glej_domnevno = True):
    try:
        if celo_obdobje:
            aktivni_orglarji = csv[(zacetek <= csv.zacetek_aktivnosti) & (csv.konec_aktivnosti <= konec)]
        else:
            aktivni_orglarji = csv[(csv.zacetek_aktivnosti <= zacetek) & (konec <= csv.konec_aktivnosti)]
        
        if glej_domnevno:
            return aktivni_orglarji
        
        return aktivni_orglarji[(~aktivni_orglarji.domneven_zacetek) & (~aktivni_orglarji.domneven_konec)]
    except:
        print("Pridobitev orglarjev v obdobju ni bilo mogoče.")


def pridobi_cas_delovanja(csv, kratek_naziv):
    try:
        orglar = csv[csv.kratek_naziv == kratek_naziv]

        zacetek = orglar.zacetek_aktivnosti.values[0]
        konec = orglar.konec_aktivnosti.values[0]

        return konec - zacetek + 1
    except:
        print("Pridobitev časa delovanja orglarja ni bilo mogoče.")

        return 0


def pridobi_orglarje_v_obmocjih(csv, iskana_obmocja):
    try:
        return csv[csv.obmocja.apply(
                lambda obmocja: any(
                    [obmocje in eval(obmocja) for obmocje in iskana_obmocja]
                )
            )
        ]
    except:
        print("Pridobitev orglarjev v območjih ni bilo mogoče.")


def pridobi_omenjene_orglarje(csv, stran):
    try:
        return csv[csv.strani_z_omembo.apply(
                lambda strani: stran in eval(strani)
            )
        ]
    except:
        print("Pridobitev omenjenih orglarjev ni bilo mogoče.")