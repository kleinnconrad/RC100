import feedparser
from bs4 import BeautifulSoup
import os
from datetime import datetime

# Die ID deines r/rccars Posts
POST_ID = '1s8nl1m' 
RSS_URL = f'https://www.reddit.com/r/rccars/comments/{POST_ID}/.rss'

USER_AGENT = 'GitHubAction:rc100-reddit-rss-sync:v1.0'

print(f"Lese RSS Feed: {RSS_URL}")
feed = feedparser.parse(RSS_URL, agent=USER_AGENT)

if feed.bozo:
    print("Fehler beim Abrufen des Feeds!")
    exit(1)

# Markdown Header zusammenbauen
md_content = "# Reddit Feedback: RC100 Project\n\n"
md_content += f"**Original Post:** [Link zum Thread](https://www.reddit.com/r/rccars/comments/{POST_ID}/)\n"
md_content += f"**Letzter Sync:** {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n\n"
md_content += "---\n\n"

for entry in feed.entries:
    author = entry.get('author', '[Unbekannt]').replace('/u/', '')
    link = entry.get('link', '')
    
    raw_html = entry.get('summary', '')
    soup = BeautifulSoup(raw_html, 'html.parser')
    text = soup.get_text(separator='\n').strip()
    
    text_formatted = text.replace('\n', '\n> ')
    
    md_content += f"**u/{author}** [schrieb]({link}):\n"
    md_content += f"> {text_formatted}\n\n"
    md_content += "---\n\n"

# Zielordner 'reddit' erstellen und speichern
os.makedirs('reddit', exist_ok=True)
file_path = 'reddit/reddit_feedback.md'

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(md_content)
    
print(f"Erfolgreich {len(feed.entries)} Einträge in {file_path} gespeichert!")
