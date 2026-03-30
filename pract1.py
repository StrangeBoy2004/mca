"""
Kalyan Panel Chart Scraper
===========================
Fetches all panel chart data from dpboss.boston and saves it to a CSV file.

Requirements:
    pip install requests beautifulsoup4

Usage:
    python kalyan_scraper.py
    python kalyan_scraper.py --output my_data.csv
    python kalyan_scraper.py --full       # Fetch full chart (all years)
    python kalyan_scraper.py --full --output kalyan_full.csv
"""

import csv
import time
import argparse
import sys
from datetime import datetime

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing dependencies. Please run:")
    print("  pip install requests beautifulsoup4")
    sys.exit(1)


# ──────────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────────
BASE_URL = "https://dpboss.boston/panel-chart-record/kalyan.php"
FULL_URL = "https://dpboss.boston/panel-chart-record/kalyan.php?full_chart"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://dpboss.boston/",
}

CSV_COLUMNS = [
    "Date_Range",
    "Mon_Open", "Mon_Mid", "Mon_Close",
    "Tue_Open", "Tue_Mid", "Tue_Close",
    "Wed_Open", "Wed_Mid", "Wed_Close",
    "Thu_Open", "Thu_Mid", "Thu_Close",
    "Fri_Open", "Fri_Mid", "Fri_Close",
    "Sat_Open", "Sat_Mid", "Sat_Close",
]


# ──────────────────────────────────────────────
# FETCH PAGE
# ──────────────────────────────────────────────
def fetch_page(url: str, retries: int = 3, delay: float = 2.0) -> str:
    """Fetch HTML content from the given URL with retry logic."""
    for attempt in range(1, retries + 1):
        try:
            print(f"  Fetching: {url}  (attempt {attempt}/{retries})")
            response = requests.get(url, headers=HEADERS, timeout=30)
            response.raise_for_status()
            print(f"  Status: {response.status_code} | Size: {len(response.text):,} bytes")
            return response.text
        except requests.RequestException as e:
            print(f"  ERROR on attempt {attempt}: {e}")
            if attempt < retries:
                print(f"  Retrying in {delay}s...")
                time.sleep(delay)
    raise RuntimeError(f"Failed to fetch {url} after {retries} attempts.")


# ──────────────────────────────────────────────
# PARSE TABLE
# ──────────────────────────────────────────────
def clean_cell(text: str) -> str:
    """Normalize a cell value: strip spaces, collapse whitespace."""
    return " ".join(text.split()).strip()


def parse_three_digit(text: str) -> str:
    """
    Convert a cell like '5  7  9' → '579'
    or '*  *  *' → '***'
    """
    parts = text.split()
    if not parts:
        return ""
    joined = "".join(parts)
    return joined


def parse_table(soup: BeautifulSoup) -> list[dict]:
    """
    Find the main panel chart table and extract all rows.

    Table structure per data row:
        col 0  : Date range
        cols 1-3  : Mon open / mid / close
        cols 4-6  : Tue open / mid / close
        cols 7-9  : Wed open / mid / close
        cols 10-12: Thu open / mid / close
        cols 13-15: Fri open / mid / close
        cols 16-18: Sat open / mid / close
    """
    records = []

    # Find the table that has the panel data (look for the one with day headers)
    tables = soup.find_all("table")
    target_table = None

    for table in tables:
        headers_row = table.find("tr")
        if headers_row:
            header_text = headers_row.get_text(" ").lower()
            if "mon" in header_text and "tue" in header_text and "wed" in header_text:
                target_table = table
                break

    if target_table is None:
        print("  WARNING: Could not locate the panel chart table.")
        return records

    rows = target_table.find_all("tr")
    print(f"  Found table with {len(rows)} rows (including header).")

    for row in rows:
        cells = row.find_all(["td", "th"])
        if not cells:
            continue

        # Skip header rows
        first_cell_text = clean_cell(cells[0].get_text())
        if first_cell_text.lower() in ("date", ""):
            continue
        # Skip rows that are day-label headers (Mon, Tue, ...)
        if any(clean_cell(c.get_text()).lower() in ("mon", "tue", "wed", "thu", "fri", "sat") 
               for c in cells):
            continue

        # We expect at least 19 columns (1 date + 6 days × 3 values)
        if len(cells) < 19:
            continue

        try:
            date_range = clean_cell(cells[0].get_text())

            def day_vals(start_idx):
                open_val = parse_three_digit(clean_cell(cells[start_idx].get_text()))
                mid_val  = clean_cell(cells[start_idx + 1].get_text()).replace(" ", "")
                close_val = parse_three_digit(clean_cell(cells[start_idx + 2].get_text()))
                return open_val, mid_val, close_val

            mon_o, mon_m, mon_c = day_vals(1)
            tue_o, tue_m, tue_c = day_vals(4)
            wed_o, wed_m, wed_c = day_vals(7)
            thu_o, thu_m, thu_c = day_vals(10)
            fri_o, fri_m, fri_c = day_vals(13)
            sat_o, sat_m, sat_c = day_vals(16)

            record = {
                "Date_Range": date_range,
                "Mon_Open": mon_o, "Mon_Mid": mon_m, "Mon_Close": mon_c,
                "Tue_Open": tue_o, "Tue_Mid": tue_m, "Tue_Close": tue_c,
                "Wed_Open": wed_o, "Wed_Mid": wed_m, "Wed_Close": wed_c,
                "Thu_Open": thu_o, "Thu_Mid": thu_m, "Thu_Close": thu_c,
                "Fri_Open": fri_o, "Fri_Mid": fri_m, "Fri_Close": fri_c,
                "Sat_Open": sat_o, "Sat_Mid": sat_m, "Sat_Close": sat_c,
            }
            records.append(record)

        except (IndexError, ValueError) as e:
            print(f"  Skipping malformed row ({len(cells)} cells): {e}")
            continue

    return records


# ──────────────────────────────────────────────
# SAVE CSV
# ──────────────────────────────────────────────
def save_csv(records: list[dict], output_path: str):
    """Write records list to a CSV file."""
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(records)
    print(f"\n  Saved {len(records)} records → {output_path}")


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Scrape Kalyan Panel Chart data to CSV"
    )
    parser.add_argument(
        "--output", "-o",
        default=f"kalyan_panel_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        help="Output CSV filename (default: kalyan_panel_<timestamp>.csv)"
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="Fetch the full chart (all years) instead of recent data"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.5,
        help="Seconds to wait between requests (default: 1.5)"
    )
    args = parser.parse_args()

    url = FULL_URL if args.full else BASE_URL
    chart_type = "FULL chart" if args.full else "recent chart"

    print("=" * 60)
    print("  Kalyan Panel Chart Scraper")
    print("=" * 60)
    print(f"  Mode    : {chart_type}")
    print(f"  URL     : {url}")
    print(f"  Output  : {args.output}")
    print("=" * 60)

    # Step 1: Fetch page
    print("\n[1/3] Fetching page...")
    html = fetch_page(url)

    # Step 2: Parse table
    print("\n[2/3] Parsing panel chart table...")
    soup = BeautifulSoup(html, "html.parser")
    records = parse_table(soup)

    if not records:
        print("\n  ERROR: No records were extracted. The page structure may have changed.")
        print("  Try inspecting the page manually: " + url)
        sys.exit(1)

    print(f"  Extracted {len(records)} data rows successfully.")

    # Step 3: Save CSV
    print("\n[3/3] Saving to CSV...")
    save_csv(records, args.output)

    # Summary
    print("\n" + "=" * 60)
    print("  DONE!")
    print(f"  Total rows   : {len(records)}")
    print(f"  Output file  : {args.output}")

    # Show a small sample
    if records:
        print("\n  First 3 rows preview:")
        for r in records[:3]:
            print(f"    {r['Date_Range']} | "
                  f"Mon:{r['Mon_Open']}/{r['Mon_Mid']}/{r['Mon_Close']} | "
                  f"Tue:{r['Tue_Open']}/{r['Tue_Mid']}/{r['Tue_Close']} | "
                  f"...")
    print("=" * 60)


if __name__ == "__main__":
    main()