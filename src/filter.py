import requests

def is_german(word):
	url = "https://de.wiktionary.org/w/api.php"

	params = {
		"action": "query",
		"prop": "revisions",
		"rvprop": "content",
		"rvslots": "main",
		"titles": word,
		"format": "json",
	}

	headers = {
    	"User-Agent": "DeWordle/1.0 (contact: muehlberg.lea@gmail.com)"
	}

	response = requests.get(url, params=params, headers=headers)
	data = response.json()

	pages = data["query"]["pages"]
	for page in pages.values():
		
		if "revisions" not in page:
			return False

		text = page["revisions"][0]["slots"]["main"]["*"]
		return "{{Sprache|Deutsch}}" in text
	return False


german_words = []

with open("my_words.txt", "r") as my_file:
	for line in my_file:
		word = line.strip()
		if is_german(word):
			german_words.append(word)

for word in german_words:
	print(word)