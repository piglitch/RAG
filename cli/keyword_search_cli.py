#!/usr/bin/env python3

import argparse
import load_data
import string


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            removal_table = str.maketrans("", "", string.punctuation)
            # print the search query here
            print("Searching for:", args.query)
            search_results = []
            movies = load_data.load_json_file("data/movies.json")

            for i in range(len(movies)):
                # print(f"Checking movie: {movies[i]['title'].lower().translate(removal_table)}")
                if args.query.lower().translate(removal_table) in movies[i][
                    "title"
                ].lower().translate(removal_table):
                    search_results.append(movies[i])

            if search_results:
                print("Found movies:")
                for i, result in enumerate(search_results, start=1):
                    if i > 5:
                        break
                    print(f"{i}. {result['title']}")
            else:
                print("No movies found.")
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
