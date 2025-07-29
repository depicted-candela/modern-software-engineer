import os, csv, json
from .. import config
from ..validators.schema import has_required_fields, is_valid_polygon_id
from ..processors.converter import wkt_to_coords

def process_directory(full_path):
    csvfiles = [file for file in os.listdir(full_path) if file.endswith(config.SEARCHED_FILES)]
    files_processed = 0
    valid_rows = 0
    all_lines = 0
    invalid_rows = 0
    errors = []
    for csvfile in csvfiles:
        with open(os.path.join(full_path, csvfile), "r") as f:
            reader = csv.DictReader(f)
            if not has_required_fields(reader.fieldnames): 
                invalid_rows += 1
                errors.append(f"{csvfile} does not have the required fields")
            all_lines += reader.line_num
            for step, line in enumerate(reader): 
                if not is_valid_polygon_id(line.get('id')):
                    errors.append(f"{csvfile} in its line {step} defined as {line} does not have a valid polygon id")
                    invalid_rows += 1
                if wkt_to_coords(line.get('wkt'))['type'] == 'invalid':
                    errors.append(f"{csvfile} in its line {step} defined as {line} does not have geometry")
                    invalid_rows += 1
        files_processed += 1
    valid_rows += all_lines - valid_rows
    with open("report.txt", "w") as writer:
        json.dump(
            {
                'files_processed': files_processed, 
                'valid_rows': valid_rows, 
                'invalid_rows': invalid_rows,
                'errors': errors
            }, 
            writer, 
            indent=2
        )