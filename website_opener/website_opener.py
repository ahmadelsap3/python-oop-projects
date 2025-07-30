import webbrowser
import random

def open_random_website():
    # List of websites
    websites = [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.python.org",
        "https://www.wikipedia.org",
        "https://www.stackoverflow.com"
    ]
    
    # Choose a random website
    random_site = random.choice(websites)
    
    # Open the website in the default browser
    print(f"Opening {random_site}...")
    webbrowser.open(random_site)

if __name__ == "__main__":
    open_random_website()
