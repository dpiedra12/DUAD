from menu import show_student_control_menu


def main():
      try:
            show_student_control_menu()
      except Exception as ex:
            print (f"An unexpected error ocurred: {ex}")


main()