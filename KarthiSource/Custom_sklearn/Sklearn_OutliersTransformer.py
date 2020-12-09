from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

#custom Outlier Transformer for making scikit learn pipeline.

class OutliersTransformer(BaseEstimator, TransformerMixin):
    
    def fit(self, data, y=None):
        return self
   
    def transform(self, data_, y=None):
        data = data_.copy() #we don't wan't to change the original data.
        
        for i, col in enumerate(columns):
            if col == 'BloodPressure':
                data[col] = np.where(data[col] <= outlier_df.loc[i, 'Lower_Bound'], outlier_df.loc[i, 'Lower_Bound'].astype(int), data[col])
                data[col] = np.where(data[col] >= outlier_df.loc[i, 'Upper_Bound'], outlier_df.loc[i, 'Upper_Bound'].astype(int), data[col])
            elif col not in ['BMI', 'DiabetesPedigreeFunction']:
                data[col] = np.where(data[col] >= outlier_df.loc[i, 'Upper_Bound'], outlier_df.loc[i, 'Upper_Bound'].astype(int), data[col])
            else:
                data[col] = np.where(data[col] >= outlier_df.loc[i, 'Upper_Bound'], outlier_df.loc[i, 'Upper_Bound'], data[col])
    
        return data.to_numpy()
