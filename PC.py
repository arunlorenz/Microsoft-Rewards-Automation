import webbrowser
import time    
# List of words to search for
search_terms = ["computer", "programming", "keyboard", "internet", "knowledge", "technology", "innovation", 
"education", "communication", "software", "hardware", "algorithm", "science", "engineering", "database", 
"cybersecurity", "robotics", "automation", "machine learning", "artificial intelligence"]

# Loop through the list of search terms and open the mobile Bing browser for each search
for term in search_terms:
    search_url = f"https://www.bing.com/search?q={term}"
    webbrowser.open_new_tab(search_url)
    time.sleep(2)
print("Search tabs opened in the default mobile browser.")