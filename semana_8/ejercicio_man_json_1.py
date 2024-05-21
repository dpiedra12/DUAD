import json

def insert_a_pokemon():
   
      name_english = input("Enter the Pokemon name: ")
      type_input = input("Enter the type of Pokemon: ")
      types = [type_input.strip()]
      hp = int(input("Enter the HP value: "))
      attack = int(input("Enter the Attack value: "))
      defense = int(input("Enter the Defense value: "))
      sp_attack = int(input("Enter the Sp. Attack value: "))
      sp_defense = int(input("Enter the Sp. Defense value: "))
      speed = int(input("Enter the Speed value: "))
                 
      new_pokemon = {
          "name": {"english": name_english},
          "type": types,
          "base": {
          "HP": hp,
          "Attack": attack,
          "Defense": defense,
          "Sp. Attack": sp_attack,
          "Sp. Defense": sp_defense,
          "Speed": speed
                    }
                  }
            
      return new_pokemon
            
   
def read_jason_file(file_path ):
    new_pokemon = insert_a_pokemon()
    with open (file_path, 'r') as file:
      data = json.load(file)
    data.append (new_pokemon)
    return data
      

def write_json_file(file_path):  
    data= read_jason_file ('json_file.json')
    with open(file_path, 'w') as file:
       json.dump (data, file, indent= 4)


write_json_file('json_file.json')