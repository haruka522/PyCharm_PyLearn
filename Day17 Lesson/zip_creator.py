import pathlib
import zipfile

def make_archive(filepaths, output_dir):
    output_path = pathlib.Path(output_dir, "compressed.zip")
    with zipfile.ZipFile(output_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    print('Hello World')