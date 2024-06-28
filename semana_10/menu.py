from actions import insert_student, validate_option, get_students, show_students_top3, get_overall_average
from data import export_data_csv_file, import_data_csv_file 
            

def show_student_control_menu():
     
     #file_path= 'students_data.csv'   
     students =[] 
     while True:
        
        print ("\nMenu\n")
        print("1. Enter the student data")
        print("2. Show the data of all students")
        print("3. Show the top 3 students with the best average grades")
        print("4. Show the average of each student's average grades")
        print("5. Export all current data to a CSV file")
        print("6. Import data from a previously exported CSV file")
        print("7. Exit\n")
        option  = validate_option ()
        
        if option ==1:
            insert_student(students)
                                         
        elif option ==2:
            get_students(students)

        elif option ==3:
            show_students_top3(students)
      
        elif option ==4:
            get_overall_average(students)
        
        elif option ==5:
            export_data_csv_file('students_data.csv', students, students[0].keys())
      
        elif option ==6:
            import_data_csv_file( 'students_data.csv', students)
      
        elif option == 7:
              break
             



