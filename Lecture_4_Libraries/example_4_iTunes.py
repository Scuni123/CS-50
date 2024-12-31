import json
import requests

def main():
    background()
    artist = get_info()
    api_result = format(artist)
    display(api_result)
    closing()

def background():
    print("\n\n=======================================================\n"
          "           Welcome To The iTunes Song Lookup\n"
          "=======================================================\n")

def get_info():
    artist = input("Who is your favorite artist --> ")
    return artist

def format(artist):
    api= requests.get("https://itunes.apple.com/search?entity=song&limit=5&media=music&attribute=ratingIndex&attribute=genreIndex&term=" + artist)
    formatted = api.json()
    return formatted

def display(api_result):
    counter = 1
    for result in api_result["results"]:
        print(f"{counter}. {result['trackName']} \n"
              f"Album: {result['collectionName']} \n"
              f"Released: {result['releaseDate']} \n"
              f"Genre: {result['primaryGenreName']} \n"
              )
        counter += 1

def closing():
    print("\n======================================================\n"
          "                         Goobye!\n"
          "======================================================\n")

if __name__ == "__main__":
    main()
