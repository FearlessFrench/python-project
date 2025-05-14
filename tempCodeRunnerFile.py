import requests # pip install requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response) # >>> <Response [200]>
    
    if response.status_code == 200: # OK response
        #print("Data retrieved!")
        pokemon_data = response.json()
        print(pokemon_data)
    else:
        print(f"Failed to retrieve data {response.status_code}")
    
pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info: # If it exists, this will be True
    print(f"{pokemon_info["name"]}")
    print(f"The {pokemon_info["id"]} pokemon in the franchise")
    print(f"Height: {pokemon_info["height"]} ft")
    print(f"Weight: {pokemon_info["height"]} lbs")