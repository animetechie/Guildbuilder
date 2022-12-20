import random
from PyQt5.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QWidget)

class SplitGroupsDialog(QWidget):
    def __init__(self):
        super().__init__()

        # Create a list of people
        self.people = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank', 'Gloria']

        # Create a form layout to hold the input fields
        self.form_layout = QFormLayout()

        # Create a line edit for the group size
        self.group_size_edit = QLineEdit()
        self.form_layout.addRow('Group size:', self.group_size_edit)

        # Create a combo box for selecting the split type
        self.split_type_combo = QComboBox()
        self.split_type_combo.addItems(['Random', 'Alternating'])
        self.form_layout.addRow('Split type:', self.split_type_combo)

        # Create a push button for splitting the groups
        self.split_button = QPushButton('Split Groups')
        self.split_button.clicked.connect(self.split_groups)
        self.form_layout.addRow(self.split_button)

        # Create labels to display the group lists
        self.group1_label = QLabel()
        self.form_layout.addRow('Group 1:', self.group1_label)
        self.group2_label = QLabel()
        self.form_layout.addRow('Group 2:', self.group2_label)

        # Create a vertical layout to hold the form layout
        vbox = QVBoxLayout()
        vbox.addLayout(self.form_layout)

        # Set the main layout of the widget
        self.setLayout(vbox)

    def split_groups(self):
        # Get the group size from the line edit
        group_size = int(self.group_size_edit.text())

        # Get the split type from the combo box
        split_type = self.split_type_combo.currentText()

        # Clear the group labels
        self.group1_label.setText('')
        self.group2_label.setText('')

        # Split the groups based on the selected split type
        if split_type == 'Random':
            group1 = random.sample(self.people, group_size)
            group2 = [p for p in self.people if p not in group1]
        elif split_type == 'Alternating
