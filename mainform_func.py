from PyQt6.QtWidgets import QListWidgetItem


def fill_dates(day_list, dates):
    for i, lst_widget in enumerate(day_list):
        lst_widget.addItem(QListWidgetItem(dates[i]))