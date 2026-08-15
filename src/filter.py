import requests

words = ["gehen", "löwe", "maus", "tragen"]

def is_german(word):
	url = "https://de.wiktionary.org/w/api.php"

	params = {
    	"action": "parse",
    	"page": word,
    	"prop": "wikitext",
    	"format": "json"
	}

	headers = {
    	"User-Agent": "WordleBot/1.0"
	}

	response = requests.get(url, params=params, headers=headers)
	data = response.json()

	if "parse" in data:
		text = data["parse"]["wikitext"]["*"]

		if f"== {word} ({{{{Sprache|Deutsch}}}}) ==" in text:
			return True
		else:
			return False
	else:
		params = {
    		"action": "query",
    		"list": "search",
    		"srsearch": word,
    		"format": "json"
		}
		response = requests.get(url, params=params, headers=headers)
		data = response.json()
		
		if len(data["query"]["search"]) > 0:
			x = data["query"]["search"][0]["title"]

			params = {
    			"action": "parse",
    			"page": x,
    			"prop": "wikitext",
    			"format": "json"
			}
			response = requests.get(url, params=params, headers=headers)
			data = response.json()
			text = data["parse"]["wikitext"]["*"]
			if f"== {x} ({{{{Sprache|Deutsch}}}}) ==" in text:
				return True
			else:
				return False

		else:
			return False


print(is_german("löwe"))