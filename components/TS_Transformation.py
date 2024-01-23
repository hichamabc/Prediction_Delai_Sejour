import pandas as pd 
from  datetime import datetime

class TS_Transformation:
    def __init__(self, column,p,df):
        self.column=column
        self.p=p
        self.df=df

    
    def List_CODE_DOUANE(self):
        df=self.df
        df=df.loc[:,['CODE_DOUANE','NUM_BL','DATE_POINTAGE','DELAI_SEJOUR']]
        df_grouped=df.groupby(self.column).count()
        df_grouped[df_grouped['DELAI_SEJOUR']>=self.p]
        df_grouped.reset_index(inplace=True)
        L=list(df_grouped[self.column].unique())

        return L

    def TS_CODE_DOUANE(self,C):
        df=self.df

        Delai_sejour_column=['DELAI_SEJOUR_'+str(i+1) for i in range(self.p)]

        data_df=pd.DataFrame([],columns=[self.column,'AVIS_ARRIVEE','NUM_BL','DATE_POINTAGE']+Delai_sejour_column+['DELAI_SEJOUR'])

        df_CODE_DOUANE=df[df[self.column]==C]

        df_CODE_DOUANE.reset_index(inplace=True)
        
        df_CODE_DOUANE.drop('index',axis=1,inplace=True)

        L_date=list(df_CODE_DOUANE['DATE_POINTAGE'])

        L_NUM_BL=list(df_CODE_DOUANE['NUM_BL'])

        L_AVIS_ARRIVE=list(df_CODE_DOUANE['AVIS_ARRIVEE'])

        for i in range(len(df_CODE_DOUANE)-self.p): 

            L_delai=list(df_CODE_DOUANE.loc[i:i+self.p,'DELAI_SEJOUR'])

            feature=[[C,L_AVIS_ARRIVE[i],L_NUM_BL[i],L_date[i]]+L_delai[::-1]]

            df_i=pd.DataFrame(feature,columns=[self.column,'AVIS_ARRIVEE','NUM_BL','DATE_POINTAGE']+ Delai_sejour_column +['DELAI_SEJOUR'])

            data_df = pd.concat([data_df, df_i], ignore_index=True)
        return data_df

    def TimeSeriesData(self):

        L_df=list(map(self.TS_CODE_DOUANE,self.List_CODE_DOUANE()))
        result_df = pd.concat((df for df in L_df), ignore_index=True)

        return result_df