# WVS Wave 7 Subset (≈ 2 000 respondents)

## Research focus
**Does higher interpersonal trust predict greater life satisfaction, and is this association mediated by respondents’ perceived freedom of choice and control over their lives?**

---

## Dataset summary  
| Item                   | Details                                                                         |
|------------------------|---------------------------------------------------------------------------------|
| **Source**             | World Values Survey Wave 7 (2017–2022), public release V 6.0                    |
| **Subset file**        | `WVS_random_subset2000.csv` (random draw ≈ 2 000 cases)                        |
| **Metadata**           | `codebook.pdf` (full variable documentation)                                    |
| **Unit of observation**| Individual adults (18+) interviewed face-to-face or online, depending on country |
| **Weight variable**    | `W_WEIGHT` (post-stratification weight)                                         |
| **Fieldwork window**   | 2017 – 2023 (varies by country)                                                 |

---

## Folder structure
```
project/
├── data/                   # Raw data and documentation
│   ├── WVS_random_subset2000.csv    # Micro-data used for analysis
│   └── codebook.pdf                 # Official variable codebook
├── notebooks/                       # Analysis and exploration scripts
├── docs/                            # Generated figures, tables, and reports
└── README.md                        # Project overview (this file)
```

---

## Key variables description
| Role                      | Code      | Label                                                     | Scale & coding                                                   |
|---------------------------|-----------|-----------------------------------------------------------|------------------------------------------------------------------|
| **Outcome**               | **Q49**   | Life satisfaction                                        | 1 = completely dissatisfied … 10 = completely satisfied           |
| **Predictor**             | **Q57**   | Interpersonal trust                                      | 1 = most people can be trusted • 2 = need to be very careful     |
| **Mediator**              | **Q48**   | Perceived freedom of choice/control                      | 1 = none at all … 10 = a great deal                              |
| **Socio-economic control**| **Q288R** | Household income (terciles)                              | 1 = low • 2 = middle • 3 = high                                  |
| **Demographic control**   | **Q260**  | Respondent age (years)                                   | Numeric                                                          |

*Missing codes: −1 Don’t know, −2 No answer, −4 Not asked, −5 Missing.*

---

## Descriptive statistics (subset, weighted)
| Variable                     | Valid N | Mean / %                             | SD    | Notes                                     |
|------------------------------|---------|--------------------------------------|-------|-------------------------------------------|
| Life satisfaction (Q49)      | 1972    | 6.70                                 | 2.10  | 10-point scale                            |
| Freedom of choice (Q48)      | 1965    | 6.30                                 | 2.40  | 10-point scale                            |
| Interpersonal trust (Q57)    | 1980    | 28 %                                 | –     | Binary (1 vs 2)                           |
| Income level (Q288R)         | 1879    | Low 33 % • Mid 34 % • High 33 %      | –     | Terciles                                  |
| Age (Q260)                   | 1992    | 42.80 yrs                            | 15.40 | Range 18–93 yrs                           |

*Figures are rounded; weights applied.*

---

## Citation
Use of these data is subject to the World Values Survey Association license for non-commercial research and education. Please cite:

> **World Values Survey Wave 7 (2017–2022).** Version 6.0. World Values Survey Association (2022). DOI: 10.14281/18241.24
