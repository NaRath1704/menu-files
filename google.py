from googlesearch import search

# Prompt the user for the search query
query = input("Enter your search query: ")

try:
    # Perform the search and print the results
    num_results = 10
    for result in search(query, num=num_results, stop=num_results, pause=2):
        print(result)
except Exception as e:
    print(f"An error occurred: {e}")

