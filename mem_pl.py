from pathlib import Path
import polars as pl
pl.toggle_string_cache(True)

fec_dir = Path("data/fec")

occupation_counts_pl = pl.scan_parquet(fec_dir / "indiv*.pq", cache=False).select(
    pl.col("OCCUPATION").value_counts(multithreaded=True, sort=True)
).collect()
