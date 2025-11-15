from typing import Optional, List, Dict
import csv
import statistics
import sys

def csv_numeric_stats(path: str,
                      columns: Optional[List[str]] = None,
                      delimiter: str = ',',
                      header: bool = True) -> Dict[str, Dict[str, Optional[float]]]:
    """
    Read CSV at `path` and compute mean, min, max for numeric values.
    - columns: list of column names to compute. If None, compute for all numeric columns.
    - header: True if first row is header (use names). If False and columns provided, columns should be indices as strings.
    Returns a dict: { column_name_or_index: {"mean":..., "min":..., "max":..., "count":...} }
    Non-numeric or empty cells are ignored.
    """
    data = {}  # column -> list of floats
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=delimiter)
        header_row = None
        if header:
            try:
                header_row = next(reader)
            except StopIteration:
                return {}

        # Map requested column names to indices
        col_indices = None
        if columns is not None:
            if header:
                name_to_idx = {name: idx for idx, name in enumerate(header_row)}
                col_indices = []
                for c in columns:
                    if c in name_to_idx:
                        col_indices.append((c, name_to_idx[c]))
                    else:
                        raise ValueError(f"Column name not found in header: {c}")
            else:
                # when no header, user should pass indices as strings or ints
                col_indices = []
                for c in columns:
                    idx = int(c)
                    col_indices.append((str(idx), idx))
        else:
            # collect all columns (use header names if present, else indices)
            # Peek first data row to know number of columns
            try:
                first = next(reader)
            except StopIteration:
                return {}
            ncols = len(first)
            # initialize data with header names or index strings
            if header:
                for i, name in enumerate(header_row):
                    data[name] = []
            else:
                for i in range(ncols):
                    data[str(i)] = []
            # process the first row
            row = first
            for i, val in enumerate(row):
                key = header_row[i] if header else str(i)
                try:
                    v = float(val)
                    data[key].append(v)
                except Exception:
                    pass
            # continue with the rest
            for row in reader:
                for i, val in enumerate(row):
                    key = header_row[i] if header else str(i)
                    try:
                        v = float(val)
                        data[key].append(v)
                    except Exception:
                        pass
            # compute and return
            results = {}
            for key, vals in data.items():
                if vals:
                    results[key] = {
                        "mean": statistics.mean(vals),
                        "min": min(vals),
                        "max": max(vals),
                        "count": len(vals)
                    }
                else:
                    results[key] = {"mean": None, "min": None, "max": None, "count": 0}
            return results
 # If columns were specified, initialize data for them
        for name, idx in col_indices:
            data[name] = []
 # process remaining rows (or all rows if header=False and columns specified)
        # If header=True and we consumed header only, reader is at first data row already.
        for row in reader:
            for name, idx in col_indices:
                if idx < len(row):
                    val = row[idx].strip()
                    if val == '':
                        continue
                    try:
                        v = float(val)
                        data[name].append(v)
                    except Exception:
                        # ignore non-numeric
                        pass
# compute stats
    results = {}
    for key, vals in data.items():
        if vals:
            results[key] = {
                "mean": statistics.mean(vals),
                "min": min(vals),
                "max": max(vals),
                "count": len(vals)
            }
        else:
            results[key] = {"mean": None, "min": None, "max": None, "count": 0}
    return results

if __name__ == "__main__":
    # default CSV path (used if no CLI arg provided)
    path = r"c:\Users\chhar\Downloads\MTECH STUDIES\AIPP ASSIGNMENTs\Assignment-2\sample.csv"
    cols = None

    # override defaults if arguments provided
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    if len(sys.argv) >= 3:
        cols = sys.argv[2].split(',')

    stats = csv_numeric_stats(path, columns=cols, delimiter=',', header=True)
    for col, s in stats.items():
        print(f"{col}: mean={s['mean']}, min={s['min']}, max={s['max']}, count={s['count']}")
