from dto.error import ErrorLog
from dto.info import InfoLog
from dto.warn import WarnLog
import logging

class LogDAO:
    def __init__(self, session):
        self.session = session

    def insert_log(self, log_type, file_name, count):
        try:
            model_map = {
                'error': ErrorLog(file_name=file_name, error_frequency=count),
                'info': InfoLog(file_name=file_name, info_frequency=count),
                'warn': WarnLog(file_name=file_name, warn_frequency=count),
            }
            entry = model_map.get(log_type)
            if entry:
                self.session.add(entry)
                self.session.commit()
                
            else:
                logging.warning(f"Unknown log type: {log_type}")
        except Exception as e:
            self.session.rollback()
            logging.error(f"Error inserting log: {e}")
