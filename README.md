# heart_attack_prediction_analysis

# Project Plan
<br>
<br>

## __<font color='salmon'> Description </font>__

* We want to answer whether or not a patient has a high risk of getting a heart attack.
* Supervised, Binary Classification. With 1 stated as high risk and 0 as not.

<br>
<br>

## __<font color='salmon'> The Data</font>__
|Column Names    | age | sex | cp | trtbps | chol | fbs | restecg | thalachh | exng | oldpeak | slp | caa | thall | output |	
| ---    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|Description    | Age of the person | Gender of the person | Chest Pain type chest pain type | resting blood pressure | cholestoral | (fasting blood sugar > 120 mg/dl) | electrocardiographic results | max heart rate| exercise induced angina | Previous peak | Slope | number of major vessels (0-3) | Thal rate | Target variable |
|Data    |0	|63| 1	|3	|145|	233|	1	|0	|150|	0	|2.3	|0	|0	|1|	1|

* blood sugar, exercise induced angina and Target variable are binary with 1 states as true, 0 false.
* number of major vessels, range from 0 to 3
* [source: kaggle](https://www.kaggle.com/rashikrahmanpritom/heart-attack-analysis-prediction-dataset)
<br>
<br>

## __<font color='salmon'> Sections </font>__


* Data Cleaning
* Data Exploration
* Machine Learning
* Conclusion
<br>
<br>

## __<font color='salmon'> Notes</font>__
* Install project requirements
   * `pip install -r requirements.txt` 
