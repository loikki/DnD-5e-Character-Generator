from PyQt4 import QtGui, QtCore
import numpy as np

import gui.tools as tools

class HealDialog(QtGui.QDialog):
    def setupUi(self):
        self.setWindowTitle("Heal")

        self.layout = QtGui.QVBoxLayout(self)
        self.l1 = QtGui.QLabel("Number of hit dice to use:", self)
        self.c1 = QtGui.QComboBox(self)
        for i in range(self.parent().character.getHitDice()[0] + 1):
            self.c1.addItem(str(i))
        self.form = QtGui.QFormLayout()
        self.layout.addLayout(self.form)
        self.form.addRow(self.l1, self.c1)

        self.l2 = QtGui.QLabel("Hit Point Healed:", self)
        self.le1 = QtGui.QLineEdit("", self)
        self.form.addRow(self.l2, self.le1)
        self.button = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self)
        roll_button = QtGui.QPushButton("Roll", self)
        self.button.addButton(
            roll_button, QtGui.QDialogButtonBox.ActionRole)

        roll_button.clicked.connect(self.roll)
        self.button.accepted.connect(self.accept)
        self.button.rejected.connect(self.reject)
        self.layout.addWidget(self.button)

        ok = self.exec_()
        if self.le1.text() == '' or not ok:
            self.le1.setText('0')
        return int(self.le1.text()), int(self.c1.currentText())

    def roll(self):
        hit_dice = self.parent().character.getHitDice()
        roll_value = tools.rollDice(
            int(self.c1.currentText()), hit_dice[2])
        self.le1.setText(str(roll_value))
        self.accept()


class DeathDialog(QtGui.QDialog):
    def setupUi(self):
        self.setWindowTitle("Death")

        self.layout = QtGui.QGridLayout(self)
        self.l1 = QtGui.QLabel("Success:", self)
        self.layout.addWidget(self.l1, 0, 0)
        self.success = [QtGui.QRadioButton("", self)]
        sgroup_0 = QtGui.QButtonGroup(self)
        sgroup_0.addButton(self.success[0])
        self.layout.addWidget(self.success[0], 0, 1)
        self.success.append(QtGui.QRadioButton("", self))
        sgroup_1 = QtGui.QButtonGroup(self)
        sgroup_1.addButton(self.success[1])
        self.layout.addWidget(self.success[1], 0, 2)
        self.success.append(QtGui.QRadioButton("", self))
        sgroup_2 = QtGui.QButtonGroup(self)
        sgroup_2.addButton(self.success[2])
        self.layout.addWidget(self.success[2], 0, 3)

        self.l2 = QtGui.QLabel("Failures:", self)
        self.layout.addWidget(self.l2, 1, 0)
        self.failure = [QtGui.QRadioButton("", self)]
        fgroup_0 = QtGui.QButtonGroup(self)
        fgroup_0.addButton(self.failure[0])
        self.layout.addWidget(self.failure[0], 1, 1)
        self.failure.append(QtGui.QRadioButton("", self))
        fgroup_1 = QtGui.QButtonGroup(self)
        fgroup_1.addButton(self.failure[1])
        self.layout.addWidget(self.failure[1], 1, 2)
        self.failure.append(QtGui.QRadioButton("", self))
        fgroup_2 = QtGui.QButtonGroup(self)
        fgroup_2.addButton(self.failure[2])
        self.layout.addWidget(self.failure[2], 1, 3)
        for i in range(3):
            self.failure[i].clicked.connect(self.manually)
            self.success[i].clicked.connect(self.manually)

        self.roll_button = QtGui.QPushButton("Roll", self)
        self.roll_button.clicked.connect(self.roll)
        self.layout.addWidget(self.roll_button, 2, 1, 1, 3)

        self.nber_success = 0
        self.nber_failure = 0
        self.healed = False
        self.exec_()
        return self.result, self.healed

    def manually(self):
        self.nber_success = np.sum([
            self.success[i].isChecked() for i in range(3)])
        self.nber_failure = np.sum([
            self.failure[i].isChecked() for i in range(3)])
        self.checkState()

    def roll(self):
        roll_value = tools.rollDice(1, 20)
        if roll_value == 1:
            self.nber_failure += 2
        elif roll_value == 20:
            self.success += 3
            self.healed = True
        elif roll_value < 10:
            self.nber_failure += 1
        else:
            self.nber_success += 1

        for i in range(3):
            if i < self.nber_success:
                self.success[i].setChecked(True)
            else:
                self.success[i].setChecked(False)
            if i < self.nber_failure:
                self.failure[i].setChecked(True)
            else:
                self.failure[i].setChecked(False)

        self.checkState()

    def checkState(self):
        if self.nber_success >= 3:
            self.result = False
            self.accept()
        elif self.nber_failure >= 3:
            self.result = True
            self.accept()


class MoneyDialog(QtGui.QDialog):
    def setupUi(self, title, default):
        self.setWindowTitle(title)

        default = tools.formatMoney(default)
        self.layout = QtGui.QVBoxLayout(self)
        self.form = QtGui.QFormLayout()
        self.layout.addLayout(self.form)
        self.label_g = QtGui.QLabel("Gold piece:", self)
        self.input_g = QtGui.QLineEdit(str(default['gp']), self)
        self.form.addRow(self.label_g, self.input_g)

        self.label_s = QtGui.QLabel("Silver piece:", self)
        self.input_s = QtGui.QLineEdit(str(default['sp']), self)
        self.form.addRow(self.label_s, self.input_s)

        self.label_c = QtGui.QLabel("Copper piece:", self)
        self.input_c = QtGui.QLineEdit(str(default['cp']), self)
        self.form.addRow(self.label_c, self.input_c)

        self.button = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self)

        self.button.accepted.connect(self.accept)
        self.button.rejected.connect(self.reject)
        self.layout.addWidget(self.button)

        ok = self.exec_()
        return_value = {'gp': int(self.input_g.text()),
                        'sp': int(self.input_s.text()),
                        'cp': int(self.input_c.text())}
        return ok, return_value
