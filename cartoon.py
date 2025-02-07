# missing import statements should be added here

from images import get_wikipedia_page_thumbnail_url, download_image_from_url


def prompt_for_image():
    """
    Prompts the user for the name of a Wikipedia page and obtains the URL of the thumbnail image of the page.
    
    return url, page_name: str, str
    """
    search_query = input("Enter name of a personality: ")
    try:
        arr = wikipedia.search(search_query, results=3, suggestion=False)
        celeb = input("Choose name from the following list: ")
        print(f"1. {arr[0]}, 2. {arr[1]}, 3. {arr[2]}")
        return images.get_wikipedia_page_thumbnail_url(celeb)

    except Exception as e:
        print(f"Error: Unable to find image for the given name: {e}")
        return None, None
    
def convert_image_to_cartoon(image_path):
    """
    Converts an image to a cartoon given the image_path.
    """
    pass
    # TODO (and remove the pass statement above)


    
if __name__ == "__main__":
    prompt_for_image()

