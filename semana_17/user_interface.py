import PySimpleGUI as sg

def show_category_window(pfm):
    layout = [
        [sg.Text(pfm.headings[1])],
        [sg.Input(key=pfm.headings[1])],
        [sg.Button("Add")],
    ]
    window = sg.Window("PFM - Category", layout)
    my_categories = sg.user_settings_get_entry('category_list', [])

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Add":
            new_category = values[pfm.headings[1]]
            if new_category not in my_categories:
                my_categories.append(new_category)
                sg.user_settings_set_entry('category_list', my_categories)
                sg.popup('Category has been saved')
            else:
                sg.popup('Category already exists')
            window.close()
            return my_categories
    window.close()


def show_expense_window(pfm, input_category):
    if not pfm.validate_category(input_category):
        return None

    layout = [
        [sg.Text(pfm.headings[0])],
        [sg.Input(key=pfm.headings[0])],
        [sg.Text(pfm.headings[1])],
        [sg.Input(key=pfm.headings[1])],
        [sg.Text(pfm.headings[3])],
        [sg.Input(key=pfm.headings[3])],
        [sg.Button("Add")],
    ]

    window = sg.Window("PFM - Expense", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Add":
            existing_category = sg.user_settings_get_entry('category_list', None)
            new_category = values[pfm.headings[1]]
            if new_category not in existing_category:
                sg.popup("The entered category does not exist. Please register the category first.")
                window.close()
                return None
            else:
                sg.popup("The data has been entered correctly")
            new_entry = [values[pfm.headings[0]], values[pfm.headings[1]], "Out", values[pfm.headings[3]]]
            
            window.close()
            return new_entry


def show_income_window(pfm, input_category):
    if not pfm.validate_category(input_category):
        return None

    layout = [
        [sg.Text(pfm.headings[0])],
        [sg.Input(key=pfm.headings[0])],
        [sg.Text(pfm.headings[1])],
        [sg.Input(key=pfm.headings[1])],
        [sg.Text(pfm.headings[3])],
        [sg.Input(key=pfm.headings[3])],
        [sg.Button("Add")],
    ]

    window = sg.Window("PFM - Income", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Add":
            existing_category = sg.user_settings_get_entry('category_list', None)
            new_category = values[pfm.headings[1]]
            if new_category not in existing_category:
                sg.popup("The entered category does not exist. Please register the category first.")
                window.close()
                return None
            else:
                sg.popup("The data has been entered correctly")
            new_entry = [values[pfm.headings[0]], values[pfm.headings[1]], "In", values[pfm.headings[3]]]
            
            window.close()
            return new_entry
