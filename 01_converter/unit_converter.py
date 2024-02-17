import PySimpleGUI as sg

layout = [
    [sg.Text('Simple Unit Converter')],
    [sg.Input(key='-INPUT-'), sg.Spin(['km to miles', 'kg to pound', 'sec to min'], key='-UNITS-'), sg.Button('Convert', key='-CONVERT-')],
    [sg.Text('Converting...', enable_events=True, key='-RESULT-')]
]

window = sg.Window('Converter', layout=layout)

while True:
    ev, vals = window.read()

    if ev == sg.WINDOW_CLOSED:
        break

    if ev == '-CONVERT-':
        input = vals['-INPUT-']
        print(input)
        if not input.isnumeric():
            output_str = 'Please enter a number.'
        else:
            match vals['-UNITS-']:
                case 'km to miles':
                    output = round(float(input) * 0.6214, 2)
                    output_str = f'{input} km = {output} miles'
                case 'kg to pound':
                    output = round(float(input) * 2.20462, 2)
                    output_str = f'{input} kg = {output} pounds'
                case 'sec to min':
                    output = float(input) / 60
                    output_str = f'{input} seconds = {output} minutes'

        window['-RESULT-'].update(output_str)

window.close()
