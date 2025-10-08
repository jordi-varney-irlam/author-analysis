import sys
import requests
import json


def fetch_author_data(author_name: str) -> dict:
    """Query Open Library's author search API for a given author name."""
    base_url = "https://openlibrary.org/search/authors.json"
    params = {"q": author_name}
    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        raise RuntimeError(f"Request failed with status {response.status_code}")

    return response.json()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 collect.py '<author name>'", file=sys.stderr)
        sys.exit(1)

    author_name = sys.argv[1]
    data = fetch_author_data(author_name)

    # Pretty-print the JSON result to stdout so you can redirect to a file
    json.dump(data, sys.stdout, indent=2)


if __name__ == "__main__":
    main()
