import json
import argparse
import os

def themeExtraction(filename):
    # Build the full path to the JSON file inside "Data (Json Files)"
    filepath = os.path.join("Data (Json Files)", filename)

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    subjects = {
        s.strip()
        for doc in data.get("docs", [])
        for s in doc.get("top_subjects", []) or []
    }

    print(len(subjects), "unique subjects")
    print(sorted(subjects))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract all unique themes/subjects from an author JSON file inside 'Data (Json Files)' folder."
    )
    parser.add_argument("filename", help="Name of the JSON file (inside 'Data (Json Files)')")
    args = parser.parse_args()

    themeExtraction(args.filename)
