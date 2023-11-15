import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress")
label2 = sg.Text("Select destination folder")
input1 = sg.InputText(key="files", readonly=True)
button1 = sg.FilesBrowse("Choose")
input2 = sg.InputText(key="directory", readonly=True)
button2 = sg.FolderBrowse("Choose")
button3 = sg.Button("Compress")
label_complete = sg.Text("", key="output")

window = sg.Window("File Zipper",
                   layout=[[label1, input1, button1], [label2, input2, button2],[button3, label_complete]])

while True:
    event, values = window.read()
    # print(event, values)
    match event:
        case "Compress":
            filepaths = values["files"].split(';')
            folder = values['directory']
            make_archive(filepaths=filepaths, dest_dir=folder)
            window["output"].update(value="Zip file created")
        case sg.WIN_CLOSED:
            break

window.close()
