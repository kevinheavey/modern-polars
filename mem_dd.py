from pathlib import Path
import dask.dataframe as dd

fec_dir = Path("data/fec")

dd.read_parquet(fec_dir / "indiv*.pq", engine="pyarrow", columns=["OCCUPATION"])[
    "OCCUPATION"
].value_counts().head()