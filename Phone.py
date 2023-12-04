import webbrowser
import time

# List of words to search for
search_terms = ["computer", "programming", "keyboard", "internet", "knowledge", "technology", "innovation", "education", "communication", "software", "hardware", "algorithm", "science", "engineering", "database", "cybersecurity", "robotics", "automation", "machine learning", "artificial intelligence","apple", "banana", "cherry", "date", "elephant", "frog", "grape", "honey", "iguana", "jellybean", "kiwi", "lemon", "mango", "nutmeg", "orange", "pear", "quince", "raspberry", "strawberry", "tangerine", "umbrella", "violet", "watermelon", "xylophone", "yogurt", "zebra", "apricot", "blueberry", "carrot", "dragonfruit", "fig", "grapefruit", "hazelnut", "ice cream", "jackfruit", "kale", "lime", "melon", "nectarine", "olive", "papaya", "quail", "rhubarb", "spinach", "tomato", "unicorn", "vanilla", "walnut", "x-ray", "yellow", "zeppelin", "almond", "blackberry", "cantaloupe", "date", "elderberry", "fig", "guava", "honeydew", "indigo", "jalapeno", "kiwifruit", "leek", "mushroom", "nectar", "olive", "parsley", "quinoa", "radish", "strawberry", "tangerine", "ugli fruit", "vinegar", "wheat", "xigua", "yam", "zucchini"]


# Loop through the list of search terms and open the mobile Bing browser for each search
for term in search_terms:
    search_url = f"https://www.bing.com/search?q={term}"
    webbrowser.open_new_tab(search_url)
    #time.sleep(1)

search_terms.reverse()
for term in search_terms:
    search_url = f"https://www.bing.com/search?q={term}"
    webbrowser.open_new_tab(search_url)
    time.sleep(1)
print("Search tabs opened in the default mobile browser.")