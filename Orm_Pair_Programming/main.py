from db.connection import DBConnection
from dto.error import Base as ErrorBase
from dto.warn import Base as WarnBase
from dto.info import Base as InfoBase
from file_handling.reader import LogReader
from file_handling.processor import LogProcessor


def main():
    db = DBConnection(user='root', password='Google@11', host='localhost', database='log')
    session = db.get_session()

    # Create tables
    ErrorBase.metadata.create_all(db.engine)
    WarnBase.metadata.create_all(db.engine)
    InfoBase.metadata.create_all(db.engine)

    reader = LogReader('./log/Input')
    
    processor = LogProcessor(reader, session)
    processor.process_logs()

if __name__ == '__main__':
    main()
