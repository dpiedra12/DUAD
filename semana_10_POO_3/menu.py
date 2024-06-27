from actions import StudentManager, validate_option
from data import export_data_csv_file, import_data_csv_file 
            

def show_student_control_menu():
     
       
     student_manager = StudentManager()
     
     
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
            student_manager.insert_student()
                                         
        elif option ==2:
            student_manager.get_students()

        elif option ==3:
            student_manager.show_students_top3()
      
        elif option ==4:
            student_manager.get_overall_average()
        
        elif option ==5:
            students = student_manager.convert_object_to_dic()
            export_data_csv_file('students_data.csv', students, students[0].keys())
      
        elif option ==6:
            
            import_data_csv_file('students_data.csv', student_manager)
      
        elif option == 7:
              break
             



