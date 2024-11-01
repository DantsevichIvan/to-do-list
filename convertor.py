import FreeSimpleGUI as sg

sg.theme('Black')

label1 = sg.Text("Enter feet:")
input_box1 = sg.InputText(key="feet")

label2 = sg.Text("Enter inches:")
input_box2 = sg.InputText(key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
result = sg.Text(key="result")

window = sg.Window("Convertor", layout=[
    [label1, input_box1],
    [label2, input_box2],
    [convert_button, exit_button, result]
], font=("Helvetica", 16))

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case "Convert":
            try:
                meters = int(values["feet"]) * 0.3048 + int(values["inches"]) * 0.0254
                window["result"].update(value=f"{meters:.4f} m")
            except ValueError:
                sg.popup("Please enter a number", font=("Helvetica", 14))
        case sg.WIN_CLOSED:
            break

window.close()
