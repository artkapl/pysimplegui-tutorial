import PySimpleGUI as sg

layout = [
    [sg.Text('Simple Unit Converter')],
    [sg.Input(key='-INPUT-'), sg.Spin(['km to miles', 'kg to pound', 'sec to min'], key='-UNITS-'), sg.Button('Convert', key='-CONVERT-')],
    [sg.Text('Converting...', enable_events=True, key='-RESULT-')]
]

window = sg.Window('Converter', layout=layout)

def is_number(num):
    try:
        float(num)
    except ValueError:
        return False
    return True


while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    elif event == '-CONVERT-':
        input = values['-INPUT-']
        if not is_number(input):
            output_str = 'Please enter a number.'
        else:
            match values['-UNITS-']:
                case 'km to miles':
                    output = round(float(input) * 0.6214, 2)
                    output_str = f'{input} km = {output} miles'
                case 'kg to pound':
                    output = round(float(input) * 2.20462, 2)
                    output_str = f'{input} kg = {output} pounds'
                case 'sec to min':
                    output = round(float(input) / 60, 2)
                    output_str = f'{input} seconds = {output} minutes'

        window['-RESULT-'].update(output_str)

window.close()
