def pridobi_orglarje_v_obdobju(org, zacetek, konec, glej_domnevno=True):
    try:
        aktivni_orglarji = org[
            org.zacetek_aktivnosti.between(zacetek, konec)
            | org.konec_aktivnosti.between(zacetek, konec)
            | ((org.zacetek_aktivnosti <= zacetek) & (konec <= org.konec_aktivnosti))
        ]

        if glej_domnevno:
            return aktivni_orglarji

        return aktivni_orglarji[(~aktivni_orglarji.domneven_zacetek) & (~aktivni_orglarji.domneven_konec)]
    except:
        print("Pridobitev orglarjev v obdobju ni bilo mogoče.")


def pridobi_orglarje_po_desetletjih(org, zacetek, konec, glej_domnevno=True):
    try:
        return [
            pridobi_orglarje_v_obdobju(org, d, d + 10, glej_domnevno)
            for d in range(zacetek, konec, 10)
        ]
    except:
        print("Pridobitev orglarjev po desetletjih ni bilo mogoče.")


def pridobi_orglarje_v_obmocjih(org, iskana_obmocja):
    try:
        return org[org.obmocja_delovanja.apply(
            lambda obmocja: any(
                [obmocje in eval(obmocja) for obmocje in iskana_obmocja]
            )
        )]
    except:
        print("Pridobitev orglarjev v območjih ni bilo mogoče.")


def pridobi_omenjene_orglarje(org, stran):
    try:
        return org[org.strani_z_omembo.apply(
            lambda strani: stran in eval(strani)
        )]
    except:
        print("Pridobitev omenjenih orglarjev ni bilo mogoče.")
