import PySimpleGUI as sg

layout = [
    [
        sg.Text('Hello World!'),
        
        sg.Spin([
            'item 1',
            'item 2'
        ])
    ],
    
    [
        sg.Input()
    ],
    
    [
        sg.Button('Quit'),
        sg.Button('Button 2')
    
    ]
]

root = sg.Window('B i s w a j i t', layout)

while True:
    event, values = root.read()
    if event == sg.WIN_CLOSED:
        break

root.close()


