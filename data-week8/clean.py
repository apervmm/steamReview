import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


INPUT = "steam_reviews.csv"
REVIEWS = "reviews.parquet"
GAMES = "games.parquet"
CHUNK = 500000

REMOVE = ["hidden_in_steam_china", "steam_china_location"]

KEEP = [
    "recommendationid",
    "appid",
    "author_steamid",
    "author_playtime_at_review",
    "author_last_played",
    "language",
    "timestamp_created",
    "votes_up",
    "votes_funny",
    "weighted_vote_score",
    "comment_count",
    "steam_purchase",
    "received_for_free",
    "written_during_early_access",
    "game"
]

def main():
    unique_games = set()
    writer = None

    chunks = pd.read_csv(
        INPUT,
        chunksize=CHUNK,
        low_memory=False,
        usecols=KEEP
    )

    for i, chunk in enumerate(chunks):
        # if i == 44 or i == 45:
        #     continue

        chunk_games = chunk[["appid", "game"]].drop_duplicates()
        for row in chunk_games.itertuples(index=False):
            unique_games.add((row.appid, row.game))

        to_drop = REMOVE + ["game"]
        chunk.drop(columns=to_drop, errors="ignore", inplace=True)


        if "timestamp_created" in chunk.columns:
            chunk["timestamp_created"] = pd.to_datetime(chunk["timestamp_created"], unit="s", errors="coerce")

        table = pa.Table.from_pandas(chunk, preserve_index=False)

        try:
            if writer is None:
                writer = pq.ParquetWriter(REVIEWS, table.schema, compression='snappy')
            writer.write_table(table)
        except ValueError as e:
            if "Schema mismatch" in str(e):
                print(f"Skipp {i}")
                continue
            else:
                raise

        print(i)
        del chunk

    if writer is not None:
        writer.close()

    df_games = pd.DataFrame(list(unique_games), columns=["appid", "game"])
    df_games.drop_duplicates(inplace=True)
    df_games.to_parquet(GAMES, index=False)


    print("\nbDone :DD")

if __name__ == "__main__":
    main()
