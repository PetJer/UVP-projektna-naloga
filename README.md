# Analiza podatkov iz knjige Orgle Slovenije

Za namen projektne naloge pri predmetu [Uvod v programiranje na FMF](https://www.fmf.uni-lj.si/sl/studij-matematike/programi/1mate/2025/predmeti/152/) sem naredil analizo podatkov iz knjige [Orgle Slovenije](https://plus.cobiss.net/cobiss/si/sl/data/cobib/295329792), ki se nahajajo na spletni strani [orgle.si](https://orgle.si).
Analizo sem izvedel na seznamu [orglarji](https://orgle.si/osebe.html).

## Analiza

Jedro projekta je datoteka [`analiza.ipynb`](/analiza.ipynb), kjer so zajeti podatki analizirani glede na sledeča vprašanja:

- Kako se je spreminjalo število aktivnih orglarjev na slovenskem območju.
- Kako se je spreminjalo število aktivnih orglarjev po območjih.
- Kako se je spreminjalo število orglarjev z domnevnim obdobjem aktivnosti.
- Kateri orglarji oziroma orglarske delavnice so bile najdlje aktivne.
- Kateri orglarji so največkrat omenjeni.
- Koliko je število omemb orglarjev po straneh.
- Povezava med številom omemb in začetkom aktivnosti.
- Kateri orglarji oziroma orglarske delavnice imajo največ drugih nazivov.
- Povezava med številom omemb in številom drugih nazivov.

Za delovanje programov je potrebna python verzija vsaj `3.11` ter knjižnici [`pandas`](https://pypi.org/project/pandas/) in [`matplotlib`](https://pypi.org/project/matplotlib/) (priporočeno je delo v virtualnem okolju).

## Struktura podatkov

V datoteki [`orglarji.csv`](/podatki/orglarji.csv) se nahajajo zajeti podatki v sledeči strukturi:

| Podatek            | Pomen                                                        | Tip      |
| ------------------ | ------------------------------------------------------------ | -------- |
| Kratek naziv       | Krajši naziv orglarja.                                       | String   |
| Drugi nazivi       | Npr. celo ime, drugi zapisi imena, sodelavci, nasledniki ... | [String] |
| Začetek aktivnosti | Leto prvega opusa v knjigi.                                  | Int      |
| Konec aktivnosti   | Leto zadnjega opusa v knjigi.                                | Int      |
| Domneven začetek   | Ali je leto začetka aktivnosti le domneva.                   | Bool     |
| Domneven konec     | Ali je leto konca aktivnosti le domneva.                     | Bool     |
| Območja delovanja  | Območja, kjer je orglar pretežno deloval.                    | [String] |
| Strani z omembo    | Strani z omembo orglarja v knjigi.                           | [Int]    |

### Primer

| Kratek naziv | Drugi nazivi               | Začetek aktivnosti | Konec aktivnosti | Domneven začetek | Domneven konec | Območja delovanja | Strani z omembo          |
| ------------ | -------------------------- | ------------------ | ---------------- | ---------------- | -------------- | ----------------- | ------------------------ |
| Jenko        | [Franc Jenko, Anton Jenko] | 1927               | 1997             | False            | False          | [LJ]              | [29, 30, 31, 38, 39 ...] |

## Opombe

- Knjiga vsebuje podatke le do vključno leta 2018.
- Vsa analiza je že bila narejena od avtorjev knjige, zato analiza v tej projektni nalogi poskuša biti izvirna, zatorej morda ne vsebuje najbolj zanimivih spoznanj.
