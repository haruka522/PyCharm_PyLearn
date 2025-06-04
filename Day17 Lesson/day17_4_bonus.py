import FreeSimpleGUI as fsg
from zip_creator import make_archive

label = fsg.Text("Select files to compress:")
input_box = fsg.InputText(tooltip="Input file location")
choose_button = fsg.FilesBrowse("Choose", key="files")

label2 = fsg.Text("Select destination folder:")
input_box2 = fsg.InputText(tooltip="Output file location")
choose_button2 = fsg.FolderBrowse("Choose", key="folder")

compress_button = fsg.Button("Compress")

output_label = fsg.Text(key="message")

layout = [[label, input_box, choose_button], [label2, input_box2, choose_button2], [compress_button, output_label]]

window = fsg.Window("File Compressor", layout)

while True:
    event, values = window.read()
    if event == fsg.WIN_CLOSED or event is None:
        break
    print(event)
    print(values)

    if event == "Compress":
        # check if files are selected
        if not values['files']:
            output_label.update(value="Error: No files selected.")
            continue
        if not values['folder']:
            output_label.update(value="Error: No folder selected.")
            continue
        filepath = values['files'].split(';')
        folder = values['folder']
        make_archive(filepath, folder)

        # both lines work
        # window["message"].update(value="Compression completed.")
        output_label.update(value="Compression completed.")

window.close()
