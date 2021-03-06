import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,plot_confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier


from io import BytesIO
import base64

# Loading DataSet
def load_data(dataset):
    
  if dataset=="wine":
    file="static\wine.csv"
    data=pd.read_csv(file)

    # cleaning
    col_names = data.columns
    for c in col_names:
        data[c] = data[c].replace("?", np.NaN)

    data = data.apply(lambda x:x.fillna(x.value_counts().index[0]))
    return data
    

# Explore DataSet
def data_visualisation(data):
    img_0 = BytesIO()
    img_1 = BytesIO()
    
    sns.countplot(x="Class_label",data=data)
    
    plt.savefig(img_0, format='png')
    plt.close()
    img_0.seek(0)
    plot_url_0 = base64.b64encode(img_0.getvalue()).decode('utf8')

    sns.scatterplot(x='Class_label',y='Alcohol',data=data)
    plt.savefig(img_1, format='png')
    
    plt.close()
    img_1.seek(0)
    plot_url_1 = base64.b64encode(img_1.getvalue()).decode('utf8')
    return plot_url_0,plot_url_1


def data_asArray(data):

    data = data.values
    Y = data[:, 0]
    X = data[:, 1:13]

    sc=StandardScaler()
    X_t=sc.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split( X_t, Y, test_size = 0.25, random_state = 50)

    

    return X_train, X_test, y_train, y_test,X_t,Y

def model(algorithm,X_train, X_test, y_train, y_test,epochs=100):
    global model1
    if algorithm== "DecisionTreeClassifier":
        model1 = DecisionTreeClassifier(criterion = "gini", random_state = 50,max_depth=5, min_samples_leaf=5)
        model_details=model1.fit(X_train,y_train)
        pred=model1.predict(X_test)

        accuracy=accuracy_score(y_test,pred)*100
        class_report=classification_report(y_test,pred)
        con_matrix=confusion_matrix(y_test,pred)

        pickle.dump(model1, open("static/model_wine.pkl","wb"))

        #----------------plotting----------------------------

        plot_confusion_matrix(model1,X_test,y_test)
        plt.title('Confusion Matrix')
        img_4 = BytesIO()
        plt.savefig(img_4, format='png')
        plt.close()
        img_4.seek(0)
        plot_url_4 = base64.b64encode(img_4.getvalue()).decode('utf8')

        X_mean=np.mean(X_test,axis=1)
        plt.plot(X_mean,y_test,'.',X_mean,pred,'*')
        plt.xlabel('X_Mean')
        plt.ylabel('Class')
        plt.legend(['Actual','Predicted'])
        plt.title('Actual vs Predicted')
        
        img_2 = BytesIO()
        plt.savefig(img_2, format='png')
        plt.close()
        img_2.seek(0)
        plot_url_2 = base64.b64encode(img_2.getvalue()).decode('utf8')
        #----------------------------------------------------

        return model_details,accuracy,class_report,con_matrix,plot_url_2,plot_url_4
    elif algorithm == "SVM":
        model1=svm.SVC(C= 10000, kernel = 'rbf', degree = 3)
        model_details=model1.fit(X_train,y_train)
        pred=model1.predict(X_test)
        print(pred)
        accuracy=accuracy_score(y_test,pred)*100
        class_report=classification_report(y_test,pred)
        con_matrix=confusion_matrix(y_test,pred)

        
        pickle.dump(model1, open("static/model_wine.pkl","wb"))
        #----------------plotting----------------------------


        plot_confusion_matrix(model1,X_test,y_test)
        plt.title('Confusion Matrix')
        img_4 = BytesIO()
        plt.savefig(img_4, format='png')
        plt.close()
        img_4.seek(0)
        plot_url_4 = base64.b64encode(img_4.getvalue()).decode('utf8')


        X_mean=np.mean(X_test,axis=1)
        plt.plot(X_mean,y_test,'.',X_mean,pred,'*')
        plt.xlabel('X_Mean')
        plt.ylabel('Class')
        plt.legend(['Actual','Predicted'])
        plt.title('Actual vs Predicted')
        
        img_2 = BytesIO()
        plt.savefig(img_2, format='png')
        plt.close()
        img_2.seek(0)
        plot_url_2 = base64.b64encode(img_2.getvalue()).decode('utf8')
        #----------------------------------------------------

        return model_details,accuracy,class_report,con_matrix,plot_url_2,plot_url_4

    elif algorithm == "MLPClassifier":
        model1=MLPClassifier(hidden_layer_sizes=[20,15,10,8,5],max_iter=2000)
        model_details=model1.fit(X_train,y_train)
        pred=model1.predict(X_test)
        print(pred)
        accuracy=accuracy_score(y_test,pred)*100
        class_report=classification_report(y_test,pred)
        con_matrix=confusion_matrix(y_test,pred)

        pickle.dump(model1, open("static/model_wine.pkl","wb"))
        #----------------plotting----------------------------
        plot_confusion_matrix(model1,X_test,y_test)
        plt.title('Confusion Matrix')
        img_4 = BytesIO()
        plt.savefig(img_4, format='png')
        plt.close()
        img_4.seek(0)
        plot_url_4 = base64.b64encode(img_4.getvalue()).decode('utf8')

        X_mean=np.mean(X_test,axis=1)
        plt.plot(X_mean,y_test,'.',X_mean,pred,'*')
        plt.xlabel('X_Mean')
        plt.ylabel('Class')
        plt.legend(['Actual','Predicted'])
        plt.title('Actual vs Predicted')
        
        img_2 = BytesIO()
        plt.savefig(img_2, format='png')
        plt.close()
        img_2.seek(0)
        plot_url_2 = base64.b64encode(img_2.getvalue()).decode('utf8')
        #----------------------------------------------------

        return model_details,accuracy,class_report,con_matrix,plot_url_2,plot_url_4

    elif algorithm == "RandomForestClassifier":
        model1=RandomForestClassifier(n_estimators=200)
        model_details=model1.fit(X_train,y_train)
        pred=model1.predict(X_test)
        print(pred)
        accuracy=accuracy_score(y_test,pred)*100
        class_report=classification_report(y_test,pred)
        con_matrix=confusion_matrix(y_test,pred)

        pickle.dump(model1, open("static/model_wine.pkl","wb"))
        #----------------plotting----------------------------

        plot_confusion_matrix(model1,X_test,y_test)
        plt.title('Confusion Matrix')
        img_4 = BytesIO()
        plt.savefig(img_4, format='png')
        plt.close()
        img_4.seek(0)
        plot_url_4 = base64.b64encode(img_4.getvalue()).decode('utf8')

        X_mean=np.mean(X_test,axis=1)
        plt.plot(X_mean,y_test,'.',X_mean,pred,'*')
        plt.xlabel('X_Mean')
        plt.ylabel('Class')
        plt.legend(['Actual','Predicted'])
        plt.title('Actual vs Predicted')
        
        img_2 = BytesIO()
        plt.savefig(img_2, format='png')
        plt.close()
        img_2.seek(0)
        plot_url_2 = base64.b64encode(img_2.getvalue()).decode('utf8')
        #----------------------------------------------------

        return model_details,accuracy,class_report,con_matrix,plot_url_2,plot_url_4
    

'''
def predict_output(test_row,X_t,Y):
    output=model1.predict(X_t[test_row:test_row+1,:])
    return Y[test_row],int(output[0])

def predict(row):
    return predict_output(row,X_t,Y)

'''

def run(algorithm,dataset):
    global X_t,Y
    
    data=load_data(dataset)
    plot_url_0,plot_url_1=data_visualisation(data)
    X_train, X_test, y_train, y_test,X_t,Y=data_asArray(data)
    m=len(Y)
    model_details=''
    accuracy=''
    class_report=''
    con_matrix=''
    model_details,accuracy,class_report,con_matrix,plot_url_2,plot_url_4=model(algorithm,X_train, X_test, y_train, y_test,150)
    #plot_tree(model1)
    
    print(class_report)
    return model_details,accuracy,class_report,con_matrix,m,plot_url_0,plot_url_1,plot_url_2,plot_url_4,X_t,Y

