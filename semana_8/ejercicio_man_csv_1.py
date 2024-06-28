import csv

def insert_video_game():
  list_of_games =[]

  count = int(input("Enter the number of video games: "))
  
  for index in range(1,count+1):

      video_games_list = {}
      name = input(f"Insert the name of the video game #{index}: ")
      gender = input(f"Insert  gender #{index}: ")
      developer = input(f"Insert  developer #{index}: ")
      class_ESRB = input(f"Insert ESRB classification#{index}: ")
      print ("")
      video_games_list["name"]=name
      video_games_list["gender"]=gender
      video_games_list["developer"]=developer
      video_games_list["classification"]=class_ESRB
      list_of_games.append(video_games_list) 
      
  return list_of_games


def write_csv_file(file_path, data, headers):
    
    with open(file_path, 'w', encoding='utf-8') as file:
        
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)

def main():
       list_of_games = insert_video_game()
       write_csv_file('video_games_list.csv', list_of_games, list_of_games[0].keys())


main()