import pandas as pd
import Model_Grid
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error

class Experience:
    def __init__( self, name,Model_Grid_List, X_train,y_train,X_test,y_test):
        self.name=name
        self.Model_Grid_List=Model_Grid_List
        self.X_train=X_train
        self.X_test=X_test
        self.y_train=y_train
        self.y_test=y_test
    
    def best_model(self):

        L=[]

        for i in range(0,len(self.Model_Grid_List)):

            M=self.Model_Grid_List[i]

            gs = GridSearchCV(estimator=M.Model_Grid()[0],param_grid=M.Model_Grid()[1],scoring='neg_mean_squared_error',cv=3)

            gs.fit(self.X_train,self.y_train)

            l=[M.Model_Grid()[0],gs.best_params_, gs.best_score_]

            L.append(l)

            print(str(i+1)+'th grid search is finished')

        score=999999

        for i in range(len(L)):

            model=L[i]

            model[0].set_params(**model[1])

            model[0].fit(self.X_train,self.y_train)

            print(str(i+1)+'th model is trained')

            model[0].predict(self.X_test)

            y_test_predicted=model[0].predict(self.X_test)

            y_train_predicted=model[0].predict(self.X_train)

            train_error=mean_squared_error(y_train_predicted,self.y_train)

            test_error=mean_squared_error(y_test_predicted,self.y_test)

            if (score>test_error):
                score=test_error
                best_model={'model':model[0],'parameters':model[1],'train_error':train_error,'test_error':test_error}

        
        return L, best_model









        
