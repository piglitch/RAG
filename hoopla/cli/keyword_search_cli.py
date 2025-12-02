#!/usr/bin/env python3

import argparse
import load_data
import string
from nltk.stem import PorterStemmer

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    stemmer = PorterStemmer()

    match args.command:
        case "search":
            removal_table = str.maketrans("", "", string.punctuation)
            # print the search query here
            print("Searching for:", args.query)
            search_results = []
            movies = load_data.load_json_file("data/movies.json")

            query = args.query.lower().translate(removal_table)
            query_terms = query.split(" ")

            stopwords = load_data.load_stopwords("data/stopwords.txt")
            for stopword in stopwords:
                if stopword in query_terms:
                    query_terms.remove(stopword)

            for i in range(len(movies)):
                # print(f"Checking movie: {movies[i]['title'].lower().translate(removal_table)}")
                for term in query_terms:
                    movie_title = movies[i]["title"].lower().translate(removal_table)
                    stemmed_term = stemmer.stem(term)
                    stemmed_movie_title = stemmer.stem(movie_title)
                    if stemmed_term in stemmed_movie_title:
                        search_results.append(movies[i])
                    
                # if args.query.lower().translate(removal_table) in movies[i][
                #     "title"
                # ].lower().translate(removal_table):
                #     search_results.append(movies[i])

            if search_results:
                print("Found movies:")
                for i, result in enumerate(search_results, start=1):
                    # if i > 5:
                        # break
                    print(f"{i}. {result['title']}")
            else:
                print("No movies found.")
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
