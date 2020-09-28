import tempfile
import zipfile
import os
import shutil
import logging
import argparse

delFileName = "__init__.py"

parser = argparse.ArgumentParser(description="create zip file")
parser.add_argument(
    "zip_name",
    type=str,
    nargs="?",
    help="input name zip arhive"
)
args = parser.parse_args()

logging.basicConfig(format="%(asctime)s - %(name)s - %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p",
                    filename=f"{args.zip_name}.log",
                    level=logging.DEBUG)

with tempfile.TemporaryDirectory() as tmpdir:
    with zipfile.ZipFile(f"{args.zip_name}.zip", "r") as zf:
        zf.extractall(path=tmpdir)
        logging.info(f"{args.zip_name}.zip extracted in {tmpdir} ")

    try:
        for dirpath, dirnames, files in os.walk(tmpdir):
            if delFileName not in files and delFileName not in dirnames:
                shutil.rmtree(dirpath)
                logging.info(f"removed catalog {dirpath}")
    except OSError as e:
        logging.error(f"Error {dirpath} {e.strerror}")

    with zipfile.ZipFile(f"{args.zip_name}_new.zip", "w") as zf:
        for dirpath, dirnames, files in os.walk(tmpdir):
            for filename in files:
                zf.write(os.path.join(dirpath, filename),
                         dirpath.replace(tmpdir, "") + '/' + filename)
    logging.info(f"{args.zip_name}_new.zip created")
