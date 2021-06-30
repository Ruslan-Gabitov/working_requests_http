import requests

def get_characters_id(name_characters):
    ids = {}
    for name in name_characters:
        response = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{name}')
        response.raise_for_status()
        ids[name] = response.json()['results'][0]['id']
    return ids
    
def get_characters_intelligence(ids):
    characters_intelligence = {}  
    for name, id in ids.items():
        response = requests.get(f'https://superheroapi.com/api/2619421814940190/{id}/powerstats')
        response.raise_for_status()
        characters_intelligence[name] = int(response.json()['intelligence'])
    return characters_intelligence

def get_smartest_characters(name_characters):
    characters_intelligence = get_characters_intelligence(get_characters_id(name_characters))
    max_val = max(characters_intelligence.values())
    smartest_characters = {name:intelligence for name, intelligence in characters_intelligence.items() if max_val == intelligence}
    return smartest_characters

    
    

if __name__ == "__main__":
    smartest_characters = ''
    name_characters = ['Hulk', 'Captain America', 'Batman', 'Doctor Strange', 'Thanos']
    for name, intelligence in get_smartest_characters(name_characters).items():
        smartest_characters += f'{name}\n' 
    print(f'Самый высокий интелект {intelligence} им обладают:\n{smartest_characters}')
