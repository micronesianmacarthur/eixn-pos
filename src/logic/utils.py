from PySide6 import QtWidgets as qtw
import json
import os

def open_dialog(dialog_class, parent=None, **kwargs):
    """
    Utility function to instantiate and execute a QDialog.
    """
    dialog = dialog_class(parent=parent, **kwargs)
    return dialog.exec()

def navigate_stacked_widget(stacked_widget: qtw.QStackedWidget, direction: int) -> int:
    """
    Navigates a QStackedWidget by a given direction (e.g., 1 for next, -1 for previous).
    Returns the new index if navigation was successful, otherwise returns the current index.
    """
    new_index = stacked_widget.currentIndex() + direction
    if 0 <= new_index < stacked_widget.count():
        stacked_widget.setCurrentIndex(new_index)
        return new_index
    return stacked_widget.currentIndex()

def dialog_connect(button, function, ui_class, parent=None, **kwargs):
    button.clicked.connect(lambda: function(ui_class, parent, **kwargs))

def window_connect(button, method, window):
    button.clicked.connect(lambda: method(window))

def load_countries():
    """
    Load country names from the countries.json file.
    Returns a sorted list of country names.
    """
    countries_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'countries.json')
    with open(countries_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return sorted([item['country'] for item in data])

def load_states_for_country(country):
    """
    Load state/province names for a given country from the countries.json file.
    Returns a sorted list of state names, or empty list if not found.
    """
    countries_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'countries.json')
    with open(countries_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        if item['country'] == country:
            if 'provinces' in item:
                return sorted([prov['name'] for prov in item['provinces']])
            elif 'districts' in item:
                return sorted([dist['name'] for dist in item['districts']])
            elif 'divisions' in item:
                return sorted([div['name'] for div in item['divisions']])
            elif 'states' in  item:
                return sorted([state['name'] for state in item['states']])
            else:
                return []
    return []
    