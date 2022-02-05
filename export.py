import argparse
import os
import pandas as pd
import tempfile
import zipfile
from pathlib import Path
from lxml import etree

DATETIME_KEYS = ["startDate", "endDate"]
NUMERIC_KEYS = ["value"]
OTHER_KEYS = ["type", "sourceName", "unit"]
ALL_KEYS = OTHER_KEYS + DATETIME_KEYS + NUMERIC_KEYS


def health_xml_to_feather(zip_file, output_file, remove_zip=False):
    with tempfile.TemporaryDirectory() as tmpdirname:
        f = zipfile.ZipFile(zip_file, "r")
        f.extractall(tmpdirname)
        # Use stem to get export.xml file name in localized versions of Apple Health
        zf_path = Path(zip_file)
        xml_path = Path(tmpdirname) / Path("apple_health_export") / Path(f"{zf_path.stem}.xml")
        tree = etree.parse(str(xml_path))
        records = tree.xpath("//Record")
        df = pd.DataFrame([{key: r.get(key) for key in ALL_KEYS}
                           for r in records])

        # Clean up key types
        for k in DATETIME_KEYS:
            df[k] = pd.to_datetime(df[k])
        for k in NUMERIC_KEYS:
            # some rows have non-numeric values, so coerce and drop NaNs
            df[k] = pd.to_numeric(df[k], errors="coerce")
            df = df[df["value"].notnull()]

        # Feature requires DFs to have a default index, so reset index which
        # may have become non-contiguous after above cleanup
        df.reset_index(drop=True).to_feather(output_file)

    if remove_zip:
        os.remove(zip_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Export latest Apple Health zip to Feather data file.")
    parser.add_argument("input_file", help="path to export.zip file")
    parser.add_argument("output_file", help="path to output file")
    parser.add_argument("--remove_zip", dest="remove_zip", action="store_true",
                        help="delete zip after extraction (default: false)")
    args = parser.parse_args()
    health_xml_to_feather(args.input_file, args.output_file, args.remove_zip)
