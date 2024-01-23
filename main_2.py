from components.Ingestion_Data import Ingestion_Data
from components.TS_Transformation import TS_Transformation
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
    df=D.Total_Df()

    TS_object=TS_Transformation('CODE_DOUANE',2,df)

    data=TS_object.TimeSeriesData()
    data.to_csv('data_TS.csv')
