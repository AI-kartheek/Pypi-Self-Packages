from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

#custom Outlier Transformer for making scikit learn pipeline.

class OutliersTransformer(BaseEstimator, TransformerMixin):
    
    def __init__(self, outlier_df):
        self.outlier_df = outlier_df
        
    def fit(self, data, y=None):
        return self
   
    def transform(self, data_, y=None):
        data = data_.copy() #we don't wan't to change the original data.
        
        for i, col in enumerate(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']):
            if col == 'BloodPressure':
                data[col] = np.where(data[col] <= self.outlier_df.loc[i, 'Lower_Bound'], self.outlier_df.loc[i, 'Lower_Bound'].astype(int), data[col])
                data[col] = np.where(data[col] >= self.outlier_df.loc[i, 'Upper_Bound'], self.outlier_df.loc[i, 'Upper_Bound'].astype(int), data[col])
            elif col not in ['BMI', 'DiabetesPedigreeFunction']:
                data[col] = np.where(data[col] >= self.outlier_df.loc[i, 'Upper_Bound'], self.outlier_df.loc[i, 'Upper_Bound'].astype(int), data[col])
            else:
                data[col] = np.where(data[col] >= self.outlier_df.loc[i, 'Upper_Bound'], self.outlier_df.loc[i, 'Upper_Bound'], data[col])
    
        return data.to_numpy()
