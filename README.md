# Analiza podatkov iz knjige Orgle Slovenije

Za namen projektne naloge pri predmetu [Uvod v programiranje na FMF](https://www.fmf.uni-lj.si/sl/studij-matematike/programi/1mate/2025/predmeti/152/) sem naredil analizo podatkov iz knjige [Orgle Slovenije](https://plus.cobiss.net/cobiss/si/sl/data/cobib/295329792), ki se nahajajo na spletni strani [orgle.si](https://orgle.si).
Analizo sem izvedel na seznamu [orglarji](https://orgle.si/osebe.html).

## Analiza

Za ogled rezultatov analize je potrebno zagnati le datoteko [`analiza.ipynb`](/analiza.ipynb), kjer so zajeti podatki analizirani.

Za delovanje programov je potrebna python verzija vsaj `3.11` ter knjižnici [`pandas`](https://pypi.org/project/pandas/) in [`matplotlib`](https://pypi.org/project/matplotlib/) (priporočeno je delo v virtualnem okolju).

## Struktura podatkov

V datoteki [`orglarji.csv`](/podatki/orglarji.csv) se nahajajo zajeti podatki v sledeči strukturi:

| Podatek            | Pomen                                                   | Tip      |
| ------------------ | ------------------------------------------------------- | -------- |
| Kratek naziv       | Krajši naziv orglarja.                                  | String   |
| Drugi nazivi       | Celo ime, drugi zapisi imena, sodelavci, nasledniki ... | [String] |
| Začetek aktivnosti | Leto prvega opusa v knjigi.                             | Int      |
| Konec aktivnosti   | Leto zadnjega opusa v knjigi.                           | Int      |
| Domneven začetek   | Ali je leto začetka aktivnosti le domneva.              | Bool     |
| Domneven konec     | Ali je leto konca aktivnosti le domneva.                | Bool     |
| Območja delovanja  | Območja, kjer je orglar pretežno deloval.               | [String] |
| Strani z omembo    | Strani z omembo orglarja v knjigi.                      | [Int]    |

### Primer

| Podatek            | Vsebina                          |
| ------------------ | -------------------------------- |
| Kratek naziv       | Jenko                            |
| Drugi nazivi       | [Franc Jenko, Anton Jenko]       |
| Začetek aktivnosti | 1927                             |
| Konec aktivnosti   | 1997                             |
| Domneven začetek   | False                            |
| Domneven konec     | False                            |
| Območja delovanja  | [LJ]                             |
| Strani z omembo    | [29, 30, 31, 38, 39, 55, 60 ...] |

## Opombe

- Knjiga vsebuje podatke le do vključno leta 2018.
- Ne ločujemo med samostojnimi orglarji in orglarskimi delavnicami.
