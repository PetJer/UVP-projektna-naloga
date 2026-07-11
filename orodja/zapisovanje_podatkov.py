import csv

def zapisi_orglarje_v_csv(orglarji):
    with open("podatki/orglarji.csv", "w", encoding='utf-8') as f:
        w = csv.DictWriter(f, orglarji[0].keys())
        w.writeheader()
        for orglar in orglarji:
            w.writerow(orglar)