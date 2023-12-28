from utils import PDF, DOCX
import sqlite3

DOSSIER_PATIENT = 'DOSSIER_PATIENT'
RADIOLOGIE_SOFTWARE = 'RADIOLOGIE_SOFTWARE'

class Database():
    def __init__(self, path) -> None:
        self.path = path
        self.connection = None
        self.cursor = None

    def get_conection(self):
        
        if not self.connection:
            self.connection =  sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()
        
        return self.connection, self.cursor
    
    def run(self, query="SELECT * FROM employee", fetchone=False):
        if fetchone:
            return self.cursor.fetchone() 
        return self.cursor.execute(query) 

    def insert_data_in_DWH_DOCUMEN(self, ipp, iddocument, source, text_content):
        sql_command = f"""INSERT INTO DWH_DOCUME (PATIENT_NUM, DOCUMENT_NUM, ID_DOC_SOURCE, DISPLAYED_TEXT)
        VALUES ({ipp}, {iddocument}, "{source}", "{text_content}");"""


    def update_data_in_DWH_DOCUMEN(self, ipp, iddocument, text_content, source):
        sql_command = f"""UPDATE DWH_DOCUME SET PATIENT_NUM={ipp}, ID_DOC_SOURCE="{source}", DISPLAYED_TEXT="{text_content}"
        where DOCUMENT_NUM={iddocument};"""


    def insert_or_update_docs_in_DWH_DOCUMENT(self,data):

        for ipp, iddocument, ext, text_content in data:
            source = ''
            if ext == PDF:
                source = DOSSIER_PATIENT
            if ext == DOCX:
                source = RADIOLOGIE_SOFTWARE

            row = self.run(f'SELECT * from DWH_DOCUMENT WHERE DOCUMENT_NUM={iddocument}', fetchone=True)
            
            if row:
                self.update_data_in_DWH_DOCUMEN(ipp, iddocument, text_content, source)
            else:
                assert not row['PATIENT_NUM'] and not row['PATIENT_NUM'] 
                self.insert_data_in_DWH_DOCUMEN(ipp, iddocument, text_content, source)

