import os, zipfile, re,traceback
from datetime import datetime

class LogReader:
    def __init__(self, log_dir):
        self.log_dir = log_dir
 
    def get_files(self):
        for file in os.listdir(self.log_dir):
            path = os.path.join(self.log_dir, file)
 
            if file.endswith('.txt') and self._valid_txt(path):
                yield file, path
 
            elif file.endswith('.zip'):
                with zipfile.ZipFile(path, 'r') as zf:
                    extract_dir = os.path.join(self.log_dir, f'unzipped_{file}')
                    zf.extractall(extract_dir)
 
                for inner in os.listdir(extract_dir):
                    p = os.path.join(extract_dir, inner)
                    if not inner.endswith('.txt'):
                        print(f"Invalid File {inner}")
                        continue
                    if self._valid_txt(p):
                        yield inner, p
 
    def _valid_txt(self, path):
        try:
            with open(path, encoding='utf-8-sig') as f:
                lines = [l.strip() for l in f if l.strip()]

            if not lines:
                print(f"Empty file: {os.path.basename(path)}")
                return False

            header_match = re.match(r'^([\w\-\.]+),(\d{8})$', lines[0])
            if not header_match:
                print(f"Invalid header in {os.path.basename(path)}")
                return False

            date_str = header_match.group(2)
            try:
                datetime.strptime(date_str, '%Y%m%d')
            except ValueError:
                print(f"Invalid date in header of {os.path.basename(path)}: {date_str}")
                return False

            try:
                expected_count = int(lines[-1])
            except ValueError:
                print(f"Invalid footer number in {os.path.basename(path)}: '{lines[-1]}'")
                return False

            actual_count = len(lines) - 2
            if expected_count != actual_count:
                print(f"Footer mismatch in {os.path.basename(path)}: expected {expected_count}, found {actual_count}")
                return False

            return True

        except Exception as e:
            print(f"Validation failed for {os.path.basename(path)}:\n{traceback.format_exc()}")
            return False
            

