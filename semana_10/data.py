import csv
       
def export_data_csv_file(file_path, data, headers):
           
            with open(file_path, 'w',encoding='utf-8') as file:
              
                  writer = csv.DictWriter(file, headers)
                  writer.writeheader()
                  writer.writerows(data)
                  print ("\nThe data has been exported\n")
            
       

def import_data_csv_file(file_path, students):
  try:
      if file_path.startswith("./") or not "/" in file_path:
            
            with open(file_path, 'r', encoding='utf-8') as file:
                  reader = csv.DictReader(file)
                  students.extend(reader)

            for student in students:
                  student["average_grade"] = float(student["average_grade"])
            print ("\nThe data has been imported\n")
          
            return students
  except FileNotFoundError as ex:
             print (F"There is no previously exported file. Error: {ex}")  


