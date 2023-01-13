import pandas as pd
from app.models.model_ExtractAndLoad_data_base import extract_files,load_file
from app.extractor.settings import path_files

class ExtractorPeople():
    def __init__(self):
        self.extractor_people_path = path_files
        self.subject = 'pessoasJuridicas'
        
    def extractor_extracrt():
        self.df = extract_files(file_path =self.extractor_people_path , 
                            filename =self.subject, encoding = 'utf-8').extract_csv_file(separator=';')
    def extractor_trating():

        self.df = self.df.rename(columns={ 'Município':'municipio',
                    'Estado':'estado',
                    'Código da atividade':'cod_atividade'
                })
        self.df = self.df[['municipio','estado','cod_atividade']]

    def extractor_load():
        load_file(file_path =self.extractor_people_path , 
                            filename =self.subject).load_xlsx_file()
def run(self):
    self.extractor_extracrt()
    self.extractor_trating()
    self.extractor_load()

