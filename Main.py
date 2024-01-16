from Ingestion_Data import Ingestion_Data





if __name__ == "__main__":
    file1='C:/Users/HAMCHTKOU/Documents/Prédiction_Délai_sejour/POC4/data.csv'
    file2='C:/Users/HAMCHTKOU/Documents/Prédiction_Délai_sejour/POC4/délai_sejour_final.csv'

    D=Ingestion_Data(file1,file2)
    df=D.data(['CODE_SH','CODE_LIEU_CHARGEMENT','TERMINAL','CODE_DOUANE'])

    df.to_csv('data.csv')