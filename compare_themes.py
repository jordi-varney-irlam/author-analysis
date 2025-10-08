#!/usr/bin/env python3
import json
import sys

def extract_author_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    # Ensure docs exist
    docs = data.get("docs", [])
    if not docs:
        return {"author": None, "themes": []}

    author = docs[0].get("name")
    themes = docs[0].get("top_subjects", [])

    return {"author": author, "themes": themes}

def compare_author_themes(file1, file2):
    author1 = extract_author_data(file1)
    author2 = extract_author_data(file2)

    themes1 = set(author1["themes"])
    themes2 = set(author2["themes"])

    common = themes1 & themes2
    unique1 = themes1 - themes2
    unique2 = themes2 - themes1

    print(f"Comparing {author1['author']} and {author2['author']}:")
    print("\nCommon Themes:")
    print(", ".join(common) if common else "None")

    print(f"\nUnique to {author1['author']}:")
    print(", ".join(unique1) if unique1 else "None")

    print(f"\nUnique to {author2['author']}:")
    print(", ".join(unique2) if unique2 else "None")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: compare_themes.py file1.json file2.json")
        sys.exit(1)
    compare_author_themes(sys.argv[1], sys.argv[2])

