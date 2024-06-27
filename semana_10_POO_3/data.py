import csv
from actions import Student
       
def export_data_csv_file(file_path, data, headers):
           
            with open(file_path, 'w',encoding='utf-8') as file:
              
                  writer = csv.DictWriter(file, headers)
                  writer.writeheader()
                  writer.writerows(data)
                  print ("\nThe data has been exported\n")
            
def import_data_csv_file(file_path, student_manager):
    try:
        students = []
        if file_path.startswith("./") or not "/" in file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        row['student_name'],
                        row['student_section'],
                        int(row['spanish_grade']),
                        int(row['english_grade']),
                        int(row['social_grade']),
                        int(row['science_grade']),
                        float(row['average_grade'])
                    )
                    students.append(student)
            student_manager.list_of_students = students
            print("\nThe data has been imported\n")
            return students
    except FileNotFoundError as ex:
        print(f"\nThere is no previously exported file. Error: {ex}")
         



