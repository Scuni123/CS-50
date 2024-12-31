import re

url = input("URL: ").strip()

if matches := re.search(r"https?://(?www\.com)?twitter\.com/([a-z1-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
