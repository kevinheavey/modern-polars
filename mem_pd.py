from pathlib import Path
import pandas as pd

fec_dir = Path("data/fec")
files = sorted(fec_dir.glob("indiv*.pq"))
total_counts_pd = pd.Series(dtype="int64")

for year in files:
    occ_pd = pd.read_parquet(year, columns=["OCCUPATION"], engine="pyarrow")
    counts = occ_pd["OCCUPATION"].value_counts()
    total_counts_pd = total_counts_pd.add(counts, fill_value=0).astype("int64")