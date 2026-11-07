#Task01: Config variables + f-string run header

import pandas as pd
from datetime import datetime

# ---------- CONFIG ----------
COUNTRIES = ["US", "GB", "IN"]
DATA_DIR = "D:/Masai/trendpulse/part1_python_foundations/data"              # relative path, never D:/...
CATEGORY_FILE = "categories.csv"
MIN_ROWS_TARGET = 40000        # project requirement

# ---------- RUN HEADER ----------
run_time = datetime.now().strftime("%Y-%m-%d %H:%M")
print(f"TrendPulse | Part 1: Python Foundations")
print(f"Run at: {run_time}")
print(f"Countries: {', '.join(COUNTRIES)}")
print(f"Data folder: {DATA_DIR}/")
print(f"Target: at least {MIN_ROWS_TARGET:,} rows in total")


#Task2: load_country() function
def load_country(country_code, data_dir=DATA_DIR):
    """Load one country's CSV and return a list of dicts (one per row)."""
    path = f"{data_dir}/{country_code}videos.csv"
    #print(path)
#have some doubts in this try, except and catch functions in python. i need to understand how it works, and how to use effectively on industrial logics. 
    try:
        df = pd.read_csv(path)
        #print(df)
    except UnicodeDecodeError:
        # Some files contain characters UTF-8 can't read
        df = pd.read_csv(path, encoding="latin-1")
        #print(df)
#in here i doubt that "to_dict" works on backend or it funcitions, expalin how it works.
    records = df.to_dict("records")
    for row in records:
        row["country"] = country_code      # remember where each row came from
        print(list("records"))
    return records

all_records = {}                      # {"US": [...], "GB": [...], "IN": [...]}
for country_code in COUNTRIES:
    all_records[country_code] = load_country(country_code)
    print(f"{country_code}: {len(all_records[country_code]):,} rows loaded")

#explain the total variable #.values() thingy
total = sum(len(rows) for rows in all_records.values())
print(f"Total: {total:,} rows (target: {MIN_ROWS_TARGET:,})")
print("Target met!" if total >= MIN_ROWS_TARGET else "Not enough rows")

print(all_records["US"][0])           # peek at one record