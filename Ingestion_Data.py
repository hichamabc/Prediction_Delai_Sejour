import pandas as pd 
from  datetime import datetime
#'C:\Users\HAMCHTKOU\Documents\Prédiction_Délai_sejour\POC4\data.csv'
#'C:\Users\HAMCHTKOU\Documents\Prédiction_Délai_sejour\POC4\délai_sejour_final.csv'

class Ingestion_Data :
    def __init__(self,path_1, path_2):
        path_1= path_1
        path_2=path_2

    def diff_date(A,B):
        date_A=datetime.strptime(A,'%d-%m-%y')
        date_B=datetime.strptime(B,'%d-%m-%y')
        date_diff=date_B-date_A
        diff_days=date_diff.days
        
        return diff_days

    def Total_Df():

        df1=pd.read_csv(path_1, sep=';', encoding='latin1')

        df2=pd.read_csv(path_2, sep=';', encoding='latin1')

        df=df1.merge(df2, left_on=('AVIS_ARRIVEE','NUM_BL'), right_on=('ID_AVISO_LLEGADA','NUM_BL'), how='inner')

        A['Delai_pointage_BAD']=list(map(diff_date,A['DATE_POINTAGE'],A['DATE_VALIDATION_BAD']))
        
        A['Delai_Creation_DUM_BAD']=list(map(diff_date,A['DATE_VALIDATION_BAD'],A['DATE_CREATION_DUM'])) 

        A=df.loc[:,['AVIS_ARRIVEE','NUM_BL','CODE_SH','LIEU_CHARGEMENT','CODE_LIEU_CHARGEMENT','PAYS_CHARGEMENT','PORT','TERMINAL','CODE_DOUANE','DATE_VALIDATION_BAD','DATE_CREATION_DUM','DATE_ML','DELAI_ML','ANNEE','MOIS','JOUR','DATE_POINTAGE','DELAI_SEJOUR']]


        return A

    
    def Aggregate_Data(colum):
        df_column=A.loc[:,[column,'Delai_Creation_DUM_BAD','Delai_pointage_BAD','DELAI_ML','DELAI_SEJOUR']]
        df_column=df_column.groupby(column).median()
        df_column.reset_index(inplace=True)
        df_column.rename(columns={'Delai_Creation_DUM_BAD':'Delai_Creation_DUM_BAD_'+column,'Delai_pointage_BAD':'Delai_pointage_BAD_'+column,'DELAI_ML':'DELAI_ML_'+column,'DELAI_SEJOUR':'DELAI_SEJOUR_'+column},inplace=True)
        return df_column

    
    def data(list_column):
        A=self.Total_Df()

        for column in list_column:
            B= A.merge(self.Aggregate_Data(column), on=column, how='inner')
            A=B


            




