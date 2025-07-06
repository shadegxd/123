"""
generate_readme.py

Reads WVS_random_subset2000.csv,
computes weighted descriptives, and
writes a fully formatted README.md.
"""

import pandas as pd
import numpy as np

# ---- 1. Load data ----
df = pd.read_csv("data/WVS_random_subset2000.csv")

# ---- 2. Clean & rename ----
# map codes to python-friendly names
df = df.rename(columns={
    "Q49":      "life_satisfaction",
    "Q57":      "trust",
    "Q48":      "freedom",
    "Q288R":    "income",
    "Q260":     "age",
    "W_WEIGHT": "weight"
})

# replace custom missing codes with NaN
missing = [-1, -2, -4, -5]
for col in ["life_satisfaction", "trust", "freedom", "income", "age"]:
    df[col] = df[col].replace(missing, np.nan)

# ---- 3. Weighted stats helper ----
def weighted_stats(x, w):
    mask = x.notna()
    x = x[mask].astype(float)
    w = w[mask].astype(float)
    mean = np.average(x, weights=w)
    # population variance:
    var = np.average((x - mean)**2, weights=w)
    # unbiased sd:
    n = len(x)
    sd = np.sqrt(var * n/(n-1)) if n>1 else np.nan
    return mean, sd, n

# compute for continuous variables
cont_vars = ["life_satisfaction", "freedom", "age", "weight"]
cont_stats = {}
for var in cont_vars:
    m, s, n = weighted_stats(df[var], df["weight"])
    cont_stats[var] = {"mean": round(m,2), "sd": round(s,2), "n": n}

# compute % trusting (trust==1)
trust_df = df.dropna(subset=["trust"])
wtot = df["weight"].sum()
trust_pct = 100 * trust_df.loc[trust_df["trust"]==1, "weight"].sum() / wtot
trust_n   = trust_df["trust"].count()

# compute income tercile distribution
inc_df = df.dropna(subset=["income"])
pct_by_income = 100 * inc_df.groupby("income")["weight"].sum() / wtot
inc_n = inc_df["income"].count()

# ---- 4. Build markdown ----
md = f"""# WVS Wave 7 Subset (≈ 2 000 respondents)

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

---

## Key variables description
| Role                      | Code      | Label                                                     | Scale & coding                                                   |
|---------------------------|-----------|-----------------------------------------------------------|------------------------------------------------------------------|
| **Outcome**               | **Q49**   | Life satisfaction                                        | 1 = completely dissatisfied … 10 = completely satisfied           |
| **Predictor**             | **Q57**   | Interpersonal trust                                      | 1 = most people can be trusted • 2 = need to be very careful     |
| **Mediator**              | **Q48**   | Perceived freedom of choice/control                      | 1 = none at all … 10 = a great deal                              |
| **Socio-economic control**| **Q288R** | Household income (terciles)                              | 1 = low • 2 = middle • 3 = high                                  |
| **Demographic control**   | **Q260**  | Respondent age (years)                                   | Numeric                                                          |
| **Weight**                | **W_WEIGHT** | Post-stratification weight                             | Numeric                                                          |

*Missing codes: −1 Don’t know, −2 No answer, −4 Not asked, −5 Missing.*

---

## Descriptive statistics (subset, weighted)
| Variable                     | Valid N | Mean / %                             | SD    | Notes                                     |
|------------------------------|---------|--------------------------------------|-------|-------------------------------------------|
| Life satisfaction (Q49)      | {cont_stats['life_satisfaction']['n']}   | {cont_stats['life_satisfaction']['mean']}                                 | {cont_stats['life_satisfaction']['sd']}   | 10-point scale                            |
| Freedom of choice (Q48)      | {cont_stats['freedom']['n']}   | {cont_stats['freedom']['mean']}                                 | {cont_stats['freedom']['sd']}   | 10-point scale                            |
| Interpersonal trust (Q57)    | {trust_n}   | {trust_pct:.0f} %                           | –     | Binary (1 vs 2)                           |
| Income level (Q288R)         | {inc_n}   | Low {pct_by_income.loc[1]:.0f} % • Mid {pct_by_income.loc[2]:.0f} % • High {pct_by_income.loc[3]:.0f} %       | –     | Terciles                                  |
| Age (Q260)                   | {cont_stats['age']['n']}   | {cont_stats['age']['mean']} yrs                             | {cont_stats['age']['sd']}  | Range 18–93 yrs                           |
| Weight (W_WEIGHT)            | {cont_stats['weight']['n']}   | {cont_stats['weight']['mean']}                        | {cont_stats['weight']['sd']}  | Post-stratification weight                |

*Figures are rounded; weights applied.*

---

## Citation
Use of these data is subject to the World Values Survey Association license for non-commercial research and education. Please cite:

> **World Values Survey Wave 7 (2017–2022).** Version 6.0. World Values Survey Association (2022). DOI: 10.14281/18241.24
"""

# ---- 5. Write to file ----
with open("README.md", "w", encoding="utf-8") as f:
    f.write(md)

print("✅ README.md generated successfully!")
