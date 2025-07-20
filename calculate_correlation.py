import sqlite3
import pandas as pd
import json

def main():
    # Connect to in-memory SQLite database
    conn = sqlite3.connect(":memory:")
    # Load SQL script and create table
    with open("q-sql-correlation-github-pages.sql", "r") as f:
        sql_script = f.read()
    conn.executescript(sql_script)
    # Load data into pandas DataFrame
    df = pd.read_sql_query("SELECT * FROM retail_data", conn)

    # Define pairs to compute correlation
    pairs = [
        ("Footfall", "Promo_Spend"),
        ("Footfall", "Net_Sales"),
        ("Promo_Spend", "Net_Sales")
    ]

    results = {}
    for a, b in pairs:
        corr = df[a].corr(df[b])
        results[f"{a}-{b}"] = corr

    # Find strongest correlation by absolute value
    strongest_pair, strongest_value = max(results.items(), key=lambda x: abs(x[1]))

    # Prepare output
    output = {
        "pair": strongest_pair,
        "correlation": round(strongest_value, 2),
        "url": "https://10vee.github.io/Vercel-App/correlation.json"
    }

    # Write JSON file to docs folder
    with open("docs/correlation.json", "w") as f:
        json.dump(output, f, indent=2)
        f.write("\n")

    # Done: output written to docs/correlation.json

if __name__ == "__main__":
    main()
