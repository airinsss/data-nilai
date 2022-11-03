import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkGreen4')



df = pd.read_excel('Data1.xlsx')

layout=[
[sg.Text('Masukan Data Kamu: ')],
[sg.Text('Nama',size=(15,1)), sg.InputText(key='Nama')],
[sg.Text('Nis',size=(15,1)), sg.InputText(key='Nis')],
[sg.Text('Nilai',size=(15,1)), sg.InputText(key='Nilai')],
[sg.Submit(), sg.Button('clear'), sg.Exit()]

]

window=sg.Window('Form pendaftaran',layout)

def clear_input():
    for key in values:
        window[key]('')
        return None

while True :
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'EXIT':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        df =df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data Berhasil Di Simpan')
        clear_input()
window.close()       