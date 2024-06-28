
def validate_option ():
        try:
                 option = int (input ("Select a option: "))
                 if 1 <= option <= 7:
                  return option
                 else:
                    print ("\nPlease select a valid option from 1 to 7\n")

        except ValueError as ex:
                    print(f"\nIncorrect value, please enter a number.\n")


def validate_grade (number):
            try:     
                  number = int(number)
                  if number < 0 or number >100:
                        print ("\nPlease enter a valid grade\n")
                        return True
                  else:
                        return False
            except ValueError as ex:
                 print(f"\nIncorrect value, please enter  a number.\n")
                 return True
 

class Student:

      def __init__(self, student_name, student_section, spanish_grade, english_grade, social_grade, science_grade, average_grade ):
        self.student_name = student_name
        self.student_section = student_section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_grade = social_grade
        self.science_grade = science_grade
        self.average_grade = average_grade
          

      def get_info(self):
        return (f"Student name: {self.student_name}\nSection: {self.student_section}\n"
                f"Spanish grade: {self.spanish_grade}\nEnglish grade: {self.english_grade}\n"
                f"Social studies grade: {self.social_grade}\nScience grade: {self.science_grade}\n")
 

class StudentManager:
    def __init__(self):
        self.list_of_students = []
        self.average_grade = 0
      


    def convert_object_to_dic(self):
           list_of_dicts = []
           for students in self.list_of_students:
             student_dict = students.__dict__
             list_of_dicts.append(student_dict) 
           return list_of_dicts    
    

    def add_student(self, new_student):
        self.list_of_students.append(new_student) 


    def get_average_grade(self, student):
        return student.average_grade
  

    def insert_student(self):
            while True:
                  student_name = input("\nInsert the student name: ")
                  student_section = input("Insert the student section: ")

                  spanish_grade = input("Insert the Spanish grade: ")
                  while  validate_grade(spanish_grade):
                        spanish_grade = input("Insert the Spanish grade: ")
                  spanish_grade = int(spanish_grade)

                  english_grade = input("Insert the English grade: ")
                  while  validate_grade(english_grade):
                        english_grade = input("Insert the English grade: ")
                  english_grade = int(english_grade)

                  social_grade = input("Insert the Social studies grade: ")
                  while  validate_grade(social_grade):
                        social_grade = input("Insert the Social studies grade: ")
                  social_grade = int(social_grade)

                  science_grade = input("Insert the Science grade: ")
                  while  validate_grade(science_grade):
                        science_grade = input("Insert the Science grade: ")
                  science_grade = int(science_grade)

                  average_grade = (spanish_grade+english_grade+social_grade+science_grade)/4

                  new_student = Student(student_name, student_section, spanish_grade, english_grade, social_grade, science_grade, average_grade)

                  self.add_student(new_student)

                  answer = input("\nPress 'Enter' to add a new student or type 'No' to return to the main menu: ")
                  if answer == "No":
                        break


            return self.list_of_students

                                                   
    def get_students(self):
            if self.list_of_students:    
                  print ("\nInformation of all entered students\n")

                  for student in self.list_of_students:
                        print (student.get_info())
            
            else:
                  print("\nThere is no student data to show.\n")


    def show_students_top3(self):
       if self.list_of_students:  
         print ("\nTop 3 students with the highest average grades:\n")
         ordered_list = sorted(self.list_of_students, key=self.get_average_grade, reverse=True)

         for student in ordered_list[:3]:
                
             name = student.student_name
             average = student.average_grade

             print(f'Student name: {name} - Average grade: {average}')
       else:
             print ("\nThere is no student data to show.\n")            
       

    def get_overall_average(self):
      
            if self.list_of_students:
                  
                  total_sum = sum(self.get_average_grade (student)  for student in self.list_of_students)
                  total_average = total_sum / len(self.list_of_students)
                  print(f"\nThe average grade among the grades of all students is:\n{total_average}")
            else:
                  print("\nThere is no student data to calculate the average.\n")