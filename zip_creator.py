import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    zip_file = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(zip_file, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


