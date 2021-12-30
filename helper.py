import statsmodels.api as sm

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
 

def ChangeFromNumericalToBinary(row):
    if row >= 0.5:
        return 1
    else:
        return 0
    
    
def calculateMatrix(y_test,y_pred):
    return accuracy_score(y_test,y_pred), \
           precision_score(y_test,y_pred), \
           recall_score(y_test,y_pred), \
           f1_score(y_test,y_pred)


def printMatrixResults(accuracy, recall, precision, f1_score):
    print('\nAccuracy: {:.4}%'.format(str(accuracy*100)))
    print('recall: {:.4}%'.format(str(recall*100)))
    print('precision: {:.4}%'.format(str(precision*100)))
    print('f1 score: {:.4}%'.format(str(f1_score*100)))
