
def validate_option ():
        try:
                 option = int (input ("Select a option: "))
                 if 1 <= option <= 7:
                  return option
                 else:
                    print ("\nPlease select a valid option from 1 to 7\n")

        except ValueError as ex:
                    print(f"\nIncorrect value, please enter a number. Error: {ex}\n")


def validate_grade (number):
            try:     
                  number = int(number)
                  if number < 0 or number >100:
                        print ("\nPlease enter a valid grade\n")
                        return True
                  else:
                        return False
            except ValueError as ex:
                 print(f"\nIncorrect value, please enter  a number. Error: {ex}\n")
                 return True


def insert_student(list_students):
            spanish_grade = 0
            while True:
                 
                  
                  info_of_students = {}
                  student_name = input("\nInsert the student name: ")
                  student_section = input("Insert the student section: ")
                  
                  spanish_grade =  input("Insert the Spanish grade: ")
                  while  (validate_grade(spanish_grade)):
                         spanish_grade =  input("Insert the Spanish grade: ")
                  spanish_grade = int(spanish_grade)

                  english_grade =  input("Insert the English grade: ")
                  while (validate_grade(english_grade)):
                        english_grade =  input("Insert the English grade: ")
                  english_grade = int(english_grade)
                  
                  social_grade = input("Insert the Social studies grade: ")
                  while (validate_grade(social_grade)):
                        social_grade = input("Insert the Social studies grade: ")
                  social_grade = int(social_grade)

                  science_grade = input("Insert the Science grade: ")
                  while (validate_grade(science_grade)):
                         science_grade = input("Insert the Social studies grade: ")
                  science_grade = int(science_grade)

                  average_grade = (spanish_grade+english_grade+social_grade+science_grade)/4
                                    
                  info_of_students["student_name"]=student_name
                  info_of_students["student_section"]=student_section
                  info_of_students["spanish_grade"]=spanish_grade
                  info_of_students["english_grade"]=english_grade
                  info_of_students["social_grade"]=social_grade
                  info_of_students["science_grade"]=science_grade
                  info_of_students["average_grade"]=average_grade

                  list_students.append(info_of_students) 
                  
                  answer = input ("\n Press 'Enter' to add a new student  or  type 'No' to return to the main menu: ")

                  if answer == "No":                           
                        break
                  
            return list_students

                                                   
def get_students(list_students):
       if list_students:    
           print ("\nInformation of all entered students\n")
           
           for students in list_students:
                  
                  for key, value in students.items():  
                              
                        if key == "student_name":
                              print (f'Student name: {value}')
                        elif key == "student_section":
                              print (f'Student section: {value}')    
                        elif key == "spanish_grade":
                              print (f'Spanish grade: {value}')    
                        elif key == "english_grade":
                              print (f'English grade: {value}')    
                        elif key == "social_grade":
                              print (f'Social studies grade: {value}')         
                        elif key == "science_grade":
                              print (f'Science grade: {value}\n') 
       else:
             print("\nThere is no student data to show.\n")
       
               
def get_average_grade(list_students):
       return list_students["average_grade"]

def show_students_top3(list_students):
       if list_students:  
         print ("\nTop 3 students with the highest average grades:\n")
         ordered_list = sorted(list_students, key=get_average_grade, reverse=True)

         for student in ordered_list[:3]:
                
            name = student["student_name"]
            average = student["average_grade"]

            print (f'Student name: {name} - Average grade: {average}')
       else:
             print ("\nThere is no student data to show.\n")


def get_overall_average(list_students):
    
    if list_students:
         
         total_sum = sum(student["average_grade"] for student in list_students)
        # total_average = int(total_average)
         total_average = total_sum / len(list_students)
         print(f"\nThe average grade among the grades of all students is:\n{total_average}")
    else:
        print("\nThere is no student data to calculate the average.\n")