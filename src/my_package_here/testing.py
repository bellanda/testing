import polars as pl

df = pl.DataFrame(
    {
        "a": [1, 2, 3] * 1000,
        "b": [4, 5, 6] * 1000,
        "c": [7, 8, 9] * 1000,
    }
)


def print_df(df: pl.DataFrame):
    print(df)
