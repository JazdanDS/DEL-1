import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


class HealthAnalyzer: 
    
    
    """ Klass för statistiska analyser samt visualiseringar på datasetet
        
        -Statestik för en kolum
        -Scatterplots för två variabler
        -Linjär regression
        -Regressionsdiagnostik (linje och residualplot)
        
        -pd.DataFrame är datan som skall analyseras
        -reg_model är våran regressionsmodell
        """

    def __init__(self,df:pd.DataFrame):
        self.df = df.copy()
    """ Vi initerar analysen med våran df"""
    def describing_colums(self,column):
        return self.df[column].describe()
    
    """ Beräknar statistik för kolumer"""

    def scatter_plot(self,x_col,y_col):
        """Scatterplot mellan två variabler"""
        data = self.df[[x_col, y_col]].dropna()
        x = data[x_col]
        y = data [y_col]
        plt.scatter(x,y)
        plt.xlabel (x_col)
        plt.ylabel (y_col)
        plt.title (f"{y_col} vs {x_col}")
        plt.show()
        
    def regression(self, x_col,y_col): 
        """Här tränar vi regressionsmodellen"""
        data = self.df[[x_col, y_col]].dropna()
        x = data[[x_col]].values
        y = data [[y_col]]
        model = LinearRegression() 
        model.fit (x,y)
        self.reg_model = model
        self.reg_x_col = x_col
        self.reg_y_col = y_col
        return model #Tränade modellen
    
    """Plott för regressionslinjen OBS! Kräver att man kör regression innan så att variablerna är satta"""

    def plot_regression (self):  
        data = self.df[[self.reg_x_col, self.reg_y_col]].dropna()
        x = data[[self.reg_x_col]].values
        y = data[[self.reg_y_col]].values
        y_pred = self.reg_model.predict(x)
        plt.figure(figsize= (6,4))
        plt.scatter (x,y,alpha=0.7)
        plt.plot(x,y_pred,color ="red", linewidth = 2)
        plt.xlabel(self.reg_x_col)
        plt.ylabel(self.reg_y_col)
        plt.title("Regression över Blodtryck och Cholesterol")
        plt.show

        """ Här gör vi regressions diagnostik mellan de två variablerna
        Vi tränar modellen
        Vi beräknar residualer
        Vi gör en regressionsplot med en linje
        Vi gör en residualplot
        Beräknar och sedan returnerar vi r2 värdet som visar hur stor del av variationen som förklaras av modellen"""

    def reg_diagnostic (self, x_col:str,y_col:str): 
        data = self.df[[x_col,y_col]].dropna()
        x = data[[x_col]].to_numpy()
        y = data [[y_col]].to_numpy()
        model = LinearRegression()
        model.fit (x,y)
        intercept_hat = float(model.intercept_)
        slope_hat = float(model.coef_[0])
        y_hat = model.predict(x)
        residuals = y-y_hat
        ss_tot = np.sum((y-y.mean()) ** 2)  
        ss_res = np.sum(residuals ** 2)
        r2 = 1 - ss_res / ss_tot
        self.reg_model = model
        self.reg_x_col = x_col
        self.reg_y_col = y_col
        
    


        plt.figure(figsize=(6, 4))
        plt.scatter(x[:, 0], y, alpha=0.7)
        x_line = np.linspace(x.min(), x.max(), 100)
        y_line = intercept_hat + slope_hat * x_line
        plt.plot(x_line, y_line, color="red")
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title("Regression över blodtryck och ålder")
       

        plt.figure(figsize=(6, 4))
        plt.scatter(y_hat, residuals, alpha=0.7)
        plt.axhline(0, color="red", linewidth=2)
        plt.xlabel("Förklarat värde (ŷ)")
        plt.ylabel("Residual (y - ŷ)")
        plt.title("Residualer, 0 = Bra")
        plt.show()
        return (f"Värdet av r2: {r2}")





