import PySimpleGUI as sg

class PersonalFinanceManager:
    def __init__(self):
        self.table_data = []
        self.headings = ['Name', 'Category', 'Type (in or out)', 'Amount']
        sg.user_settings_filename(filename='data.json', path='.')

    def validate_category(self, expected_category):
        category = sg.user_settings_get_entry('category_list', None)
        if not category:
            print("Please enter a category first")
            return False
        if expected_category != category:
            print("Please enter the correct category.")
            return False
        return True