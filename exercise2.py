import FreeSimpleGUI as sg

label1 = sg.Text("Enter feet:")
input_box1 = sg.InputText(key="feet")

label2 = sg.Text("Enter inches:")
input_box2 = sg.InputText(key="inches")

convert_button = sg.Button("Convert")
result = sg.Text(key="result")

window = sg.Window("Convertor", layout=[
    [label1, input_box1],
    [label2, input_box2],
    [convert_button, result]
])

while True:
    event, values = window.read()
    meters = int(values["feet"]) * 0.3048 + int(values["inches"]) * 0.0254
    window["result"].update(value=f"{meters} m")

window.close()
