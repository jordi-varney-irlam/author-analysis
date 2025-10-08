import json
import argparse

def themeExtraction(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    subjects = {
        s.strip()
        for doc in data.get("docs", [])
        for s in doc.get("top_subjects", []) or []
    }

    print(len(subjects), "unique subjects")
    print(sorted(subjects))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract all unique themes/subjects from an author JSON file.")
    parser.add_argument("filename", help="Path to the JSON file (in the same folder).")
    args = parser.parse_args()

    themeExtraction(args.filename)
