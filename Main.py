from Ingestion_Data import Ingestion_Data
from Experience import Experience
from Model_Grid import Model_Grid
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)

from xgboost import XGBRegressor





if __name__ == "__main__":
    file1='C:/Users/HAMCHTKOU/Documents/Prédiction_Délai_sejour/POC4/data.csv'
    file2='C:/Users/HAMCHTKOU/Documents/Prédiction_Délai_sejour/POC4/délai_sejour_final.csv'

    D=Ingestion_Data(file1,file2)

    df=D.data(['CODE_SH','CODE_LIEU_CHARGEMENT','TERMINAL','CODE_DOUANE'])

    train=df[(df['ANNEE']<2023) | ((df['ANNEE']==2023) & (df['MOIS']<10))]

    test=df[(df['ANNEE']>=2023) & (df['MOIS']>=10)]

    X_train=train.loc[:, ['ANNEE', 'MOIS','JOUR','TYPE_MR',  'Delai_Creation_DUM_BAD_CODE_SH', 'Delai_pointage_BAD_CODE_SH',
       'DELAI_ML_CODE_SH', 'DELAI_SEJOUR_CODE_SH',
       'Delai_Creation_DUM_BAD_CODE_LIEU_CHARGEMENT',
       'Delai_pointage_BAD_CODE_LIEU_CHARGEMENT',
       'DELAI_ML_CODE_LIEU_CHARGEMENT', 'DELAI_SEJOUR_CODE_LIEU_CHARGEMENT',
       'Delai_Creation_DUM_BAD_TERMINAL', 'Delai_pointage_BAD_TERMINAL',
       'DELAI_ML_TERMINAL', 'DELAI_SEJOUR_TERMINAL',
       'Delai_Creation_DUM_BAD_CODE_DOUANE', 'Delai_pointage_BAD_CODE_DOUANE',
       'DELAI_ML_CODE_DOUANE', 'DELAI_SEJOUR_CODE_DOUANE']]
    y_train=train.loc[:,'DELAI_SEJOUR']
    
    X_test=test.loc[:, ['ANNEE', 'MOIS','JOUR','TYPE_MR',  'Delai_Creation_DUM_BAD_CODE_SH', 'Delai_pointage_BAD_CODE_SH',
       'DELAI_ML_CODE_SH', 'DELAI_SEJOUR_CODE_SH',
       'Delai_Creation_DUM_BAD_CODE_LIEU_CHARGEMENT',
       'Delai_pointage_BAD_CODE_LIEU_CHARGEMENT',
       'DELAI_ML_CODE_LIEU_CHARGEMENT', 'DELAI_SEJOUR_CODE_LIEU_CHARGEMENT',
       'Delai_Creation_DUM_BAD_TERMINAL', 'Delai_pointage_BAD_TERMINAL',
       'DELAI_ML_TERMINAL', 'DELAI_SEJOUR_TERMINAL',
       'Delai_Creation_DUM_BAD_CODE_DOUANE', 'Delai_pointage_BAD_CODE_DOUANE',
       'DELAI_ML_CODE_DOUANE', 'DELAI_SEJOUR_CODE_DOUANE']]
       
    y_test=test.loc[:,'DELAI_SEJOUR']


    Model_Grid_List=[Model_Grid(RandomForestRegressor(),{'n_estimators':[40,50,60,70,80,90,100],'max_depth':[4,5,6,7,8]}),
    Model_Grid(GradientBoostingRegressor(),{'n_estimators':[40,50,60,70,80,90,100],'max_depth':[4,5,6,7,8],'learning_rate':[.1,.01,.05,.001]}),
    Model_Grid(XGBRegressor(),{'n_estimators':[40,50,60,70,80,90,100],'max_depth':[4,5,6,7,8],'learning_rate':[.1,.01,.05,.001]}),
    Model_Grid(AdaBoostRegressor(),{'n_estimators':[40,50,60,70,80,90,100],'learning_rate':[.1,.01,.05,.001]}),
    Model_Grid(CatBoostRegressor(verbose=False),{'n_estimators':[40,50,60,70,80,90,100],'learning_rate':[.1,.01,.05,.001],'depth':[4,5,6,7,8]})]

    E=Experience('First Experience',Model_Grid_List, X_train,y_train,X_test,y_test)
    L=E.best_model()
    print(L[0])

    print(L[1])

    


