import requests
from PyQt5.QtWidgets import*

app = QApplication([])
window = QWidget()

valuta1_input = QLineEdit()
valuta1_input.setPlaceholderText("Введіть валюту")

result_btn = QPushButton("Перевести")

datayear_input = QLineEdit()
datayear_input.setPlaceholderText("Введіть дату")

cilckist_input = QLineEdit()
cilckist_input.setPlaceholderText("Введіть кількість")

resultat_input = QLineEdit()
resultat_input.setPlaceholderText("Результат")




main_line = QVBoxLayout()
main_line.addWidget(valuta1_input)
main_line.addWidget(datayear_input)
main_line.addWidget(cilckist_input)
main_line.addWidget(resultat_input)
main_line.addWidget(result_btn)



def get_result():
    valcode = valuta1_input.text()
    response = requests.get(
        f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&json")
    data = response.json()
    print(data)
    print(data[0]["rate"])


result_btn.clicked.connect(get_result)
window.setLayout(main_line)



window.show()
app.exec()