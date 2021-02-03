import json
import requests

class Pokemon:
    def __init__(self, name, type_Of, abilities, weight):
        self.name = name
        self.type_Of = type_Of
        self.abilities = abilities
        self.weight = weight

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type_Of

    def get_abilities(self):
        return self.abilities

    def get_weight(self):
        return self.weight

    def __repr__(self):
        return f'<Pokemon: {self.type_Of} {self.name}>'

    def __str__(self):
        return f'{self.type_Of} {self.name}'

    # @classmethod
    def all(self):
        print("+:"*25)
        print(f'Pokemon name: {(self.name).title()}')
        print(f'Pokemon Type: {(self.type_Of).title()}')
        print(f'Pokemon ability: {(self.abilities).title()}')
        print(f'Pokemon weight: {self.weight}')
        print(":+"*25)


class PokeDex:
    def __init__(self, name):
        self.web_link = f'https://pokeapi.co/api/v2/pokemon/{name}'

    def run(self):
        url = requests.get(self.web_link)
        if url.status_code == 400:
            print('You must pass in a valid Poke Name to execute this program.')
        elif url.status_code == 200:
            data = url.json()
            abilities = data['abilities'][0]['ability']['name']
            name = data['forms'][0]['name']
            types = data['types'][0]['type']['name']
            weight = data['weight']
            p = Pokemon(name, types, abilities, weight)
            p.all()

# data = res.json()['MRData']['StandingsTable']['StandingsList'][0]['DriverStandings']:
#    for driver in data:
#        d = Driver(driver['Driver']['givenName'], driver['Driver']['familyName'], type=driver['Driver']['dateofBirth'], driver['points'], driver['position'], driver['Driver']['nationality'], driver['constructors'][0])


p_list = ['ratata', 'pikachu', 'charmander', 'magikarp', 'ditto', 'snorlax', 'eevee', 'dragonite', 'koffing', 'weezing',
          'moltres', 'kadabra', 'articuno', 'ghastly', 'ekans', 'meowth', 'lucario', 'bulbasaur', 'articuno', 'zapdos', 'mew']

for i in p_list:
    program = PokeDex(i)
    program.run()
