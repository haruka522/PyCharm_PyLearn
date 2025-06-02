import FreeSimpleGUI as fsg

label = fsg.Text("Select files to compress:")
input_box = fsg.InputText(tooltip="Input file location")
choose_button = fsg.FilesBrowse("Choose")

label2 = fsg.Text("Select destination folder:")
input_box2 = fsg.InputText(tooltip="Output file location")
choose_button2 = fsg.FolderBrowse("Choose")

compress_button = fsg.Button("Compress")

layout = [[label, input_box, choose_button], [label2, input_box2, choose_button2], [compress_button]]

window = fsg.Window("File Compressor", layout)


window.read()
window.close()
