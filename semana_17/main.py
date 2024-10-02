import PySimpleGUI as sg
from models import PersonalFinanceManager
from user_interface import show_category_window, show_expense_window, show_income_window

def show_main_window():
    pfm = PersonalFinanceManager()
    pfm.table_data = sg.user_settings_get_entry('my_table', [])
    layout = [
        [sg.Text("")],
        [sg.Table(pfm.table_data, pfm.headings, key='table_data')],
        [sg.Text("")],
        [sg.Button("Add category"), sg.Button("Add expense"), sg.Button("Add income"), sg.Exit()],
    ]
    
    window = sg.Window("Personal Financial Management", layout)
    main_win = True
    while main_win:
        sg.user_settings_set_entry('my_table', pfm.table_data)
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == "Exit":
            main_win = False
        elif event == "Add category":
            show_category_window(pfm)
        elif event == "Add expense":
            input_category = sg.user_settings_get_entry('category_list', None)
            if not input_category:
                sg.popup("No category added. Please add a category first.")
                show_category_window(pfm)
            else:
                new_data = show_expense_window(pfm, input_category)
                if new_data:
                    pfm.table_data.append(new_data)
                    window['table_data'].update(values=pfm.table_data)
        elif event == "Add income":
            input_category = sg.user_settings_get_entry('category_list', None)
            if not input_category:
                sg.popup("No category set. Please add a category first.")
                show_category_window(pfm)
            else:
                new_data = show_income_window(pfm, input_category)
                if new_data:
                    pfm.table_data.append(new_data)
                    window['table_data'].update(values=pfm.table_data)
    
    window.close()

if __name__ == "__main__":
    show_main_window()
