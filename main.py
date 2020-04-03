from flask import Flask,render_template,request
import pickle
from sklearn.tree import DecisionTreeClassifier
import numpy as np

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    
    if request.method =='POST':
        
        #pickle_in = open("corona.pkl","rb")
        
        
        
        age = request.form['age']
        fever = request.form['fever']
        bodyPain = request.form['bodyPain']
        contactwithCOVIDPatient = request.form['contactwithCOVIDPatient']
        soreThroat = request.form['soreThroat']
        coarsenessVoice = request.form['coarsenessVoice']
        Cold = request.form['Cold']
        Headache = request.form['Headache']
        runnyNose = request.form['runnyNose']
        travelHistory = request.form['travelHistory']
        dryCough = request.form['dryCough']
        diffBreath = request.form['diffBreath']
       

        #print('#-------------------------------data is here-------------------------------------#')
        #print(age,bodyPain,fever,Cold,diffBreath)
        
        clf = pickle.load(open("corona.pkl", "rb"))
        #columns  -- age,	fever,	bodyPain,	runnyNose,	diffBreath
        data = [[int(age),int(fever),int(bodyPain),int(contactwithCOVIDPatient),int(soreThroat),int(coarsenessVoice),int(Cold),int(Headache),int(runnyNose),int(travelHistory),int(dryCough),int(diffBreath)]]
        predict = clf.predict(data)[0]
        proba_score = clf.predict_proba(data)[0][1]
        
        if int(Cold)==1:
            cold='YES'
        elif int(Cold)==0:
            cold='NO'
        
        if int(fever)==-1:
            Fever='No Fever'
        elif int(fever)==0:
            Fever='Little Fever'
        elif int(fever)==1:
            Fever='High Fever'

        if int(bodyPain)==-1:
            bodypain='No Pain'
        elif int(bodyPain)==0:
            bodypain='Little Pain'
        elif int(bodyPain)==1:
            bodypain='Severe Pain'

        if int(contactwithCOVIDPatient)==1:
            covidpatient='YES'
        elif int(contactwithCOVIDPatient)==0:
            covidpatient='NO'

        if int(soreThroat)==1:
            sorethroat='YES'
        elif int(soreThroat)==0:
            sorethroat='NO'

        if int(coarsenessVoice)==1:
            coarvoice='YES'
        elif int(coarsenessVoice)==0:
            coarvoice='NO'

        if int(Headache)==-1:
            headache='No Headache'
        elif int(Headache)==0:
            headache='Little Headache'
        elif int(Headache)==1:
            headache='Severe Headache'

        if int(runnyNose)==1:
            runnynose='YES'
        elif int(runnyNose)==0:
            runnynose='NO'

        if int(travelHistory)==1:
            travelhistory='YES'
        elif int(travelHistory)==0:
            travelhistory='NO'

        if int(dryCough)==1:
            drycough='YES'
        elif int(dryCough)==0:
            drycough='NO'

        if int(diffBreath)==-1:
            diffbreath='No Difficulty'
        elif int(diffBreath)==0:
            diffbreath='Little Difficulty'
        elif int(diffBreath)==1:
            diffbreath='Severe Difficulty'
        
        if predict==1:
            prediction='Positive(High Risk)'
        else:
            prediction = 'Negative(Low Risk)'
        
        
        return render_template('show.html',age=age,fever=Fever,bodyPain=bodypain,contactwithCOVIDPatient=covidpatient,soreThroat=sorethroat,coarsenessVoice=coarvoice,Cold=cold,Headache=headache,runnyNose=runnynose,travelHistory=travelhistory,dryCough=drycough,diffBreath=diffbreath,prediction=prediction,proba_score=round(proba_score*100,2))
    else:
        
        return render_template('index.html',message='Something missed, Please follow the instructions..!')
              

if __name__ == '__main__':
    app.run(debug=True)
