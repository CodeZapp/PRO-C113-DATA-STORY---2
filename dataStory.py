import pandas as pd
import statistics
import plotly.express as px
df = pd.read_csv('savingsDataFinal.csv')
fig = px.scatter(df, y = 'quant_saved', color = 'rem_any')
fig.show()
import csv
with open('savingsDataFinal.csv', newline = '') as f:
  reader = csv.reader(f)
  savingsData = list(reader)
savingsData.pop(0)
totalEntries = len(savingsData)
totalPeopleGivenReminder = 0
for data in savingsData:
  if int(data[3]) == 1:
    totalPeopleGivenReminder += 1
import plotly.graph_objects as go
fig = go.Figure(go.Bar(x = ['Reminded', 'Not Reminded'], y = [totalPeopleGivenReminder, (totalEntries - totalPeopleGivenReminder)]))
fig.show()
allSavings = []
for data in savingsData:
  allSavings.append(float(data[0]))
print(f'Mean of savings - {statistics.mean(allSavings)}')
print(f'Median of savings - {statistics.median(allSavings)}')
print(f'Mode of savings - {statistics.mode(allSavings)}')
remindedSavings = []
notRemindedSavings = []
for data in savingsData:
  if int(data[3]) == 1:
    remindedSavings.append(float(data[0]))
  else:
    notRemindedSavings.append(float(data[0]))
print('Results for people who were reminded to save')
print(f'Mean of savings - {statistics.mean(remindedSavings)}')
print(f'Median of savings - {statistics.median(remindedSavings)}')
print(f'Mode of savings - {statistics.mode(remindedSavings)}')
print('\n\n')
print("Results for people who were not reminded to save")
print(f'Mean of savings - {statistics.mean(notRemindedSavings)}')
print(f'Median of savings - {statistics.median(notRemindedSavings)}')
print(f'Mode of savings - {statistics.mode(notRemindedSavings)}')
print(f'Standard deviation of all the data -> {statistics.stdev(allSavings)}')
print(f'Standard deviation of people who were reminded -> {statistics.stdev(remindedSavings)}')
print(f'Standard deviation of people who were not reminded -> {statistics.stdev(notRemindedSavings)}')
import numpy as np
age = []
savings = []
for data in savingsData:
  if float(data[5]) != 0:
    age.append(float(data[5]))
    savings.append(float(data[0]))
correlation = np.corrcoef(age, savings)
print(f'Correlation between the age of the person and their savings is - {correlation[0, 1]}')
import plotly.figure_factory as ff
fig = ff.create_distplot([df['quant_saved'].tolist()], ['Savings'], show_hist = False)
fig.show()
import seaborn as sns
sns.boxplot(data = df, x = df['quant_saved'])
q1 = df['quant_saved'].quantile(0.25)
q3 = df['quant_saved'].quantile(0.75)
iqr = q3 - q1
print(f'Q1 - {q1}')
print(f'Q3 - {q3}')
print(f'IQR - {iqr}')
lowerWhisker = q1 - 1.5 * iqr
upperWhisker = q3 + 1.5 * iqr
print(f'Lower Whisker - {lowerWhisker}')
print(f'Upper Whisker - {upperWhisker}')
newDf = df[df['quant_saved'] < upperWhisker]
allSavings = newDf['quant_saved'].tolist()
print(f'Mean of savings - {statistics.mean(allSavings)}')
print(f'Median of savings - {statistics.median(allSavings)}')
print(f'Mode of savings - {statistics.mode(allSavings)}')
print(f'Standard deviation in savings - {statistics.stdev(allSavings)}')
fig = ff.create_distplot([newDf['quant_saved'].tolist()], ['Savings'], show_hist = False)
fig.show()
import random
samplingMeanList = []
for i in range(1000):
  tempList = []
  for j in range(100):
    tempList.append(random.choice(allSavings))
  samplingMeanList.append(statistics.mean(tempList))
meanSampling = statistics.mean(samplingMeanList)
fig = ff.create_distplot([samplingMeanList], ['Savings (Sampling)'], show_hist = False)
fig.add_trace(go.Scatter(x = [meanSampling, meanSampling], y = [0, 0.1], mode = 'lines', name = 'MEAN'))
fig.show()
print(f'Standard deviation of the sampling data - {statistics.stdev(samplingMeanList)}')
print(f'Mean of Population - {statistics.mean(allSavings)}')
print(f'Mean of Sampling Distribution - {meanSampling}')
tempDf = newDf[newDf.age != 0]
age = tempDf['age'].tolist()
savings = tempDf['quant_saved'].tolist()
correlation = np.corrcoef(age, savings)
print(f'Correlation between the age of the person and their savings is - {correlation[0, 1]}')
remindedDf = newDf.loc[newDf['rem_any'] == 1]
notRemindedDf = newDf.loc[newDf['rem_any'] == 0]
print(remindedDf.head())
print(notRemindedDf.head())
fig = ff.create_distplot([notRemindedDf['quant_saved'].tolist()], ['Savings (Not Reminded)'], show_hist = False)
fig.show()
notRemindedSavings = notRemindedDf['quant_saved'].tolist()
samplingMeanListNotReminded = []
for i in range(1000):
  temp_list = []
  for j in range(100):
    temp_list.append(random.choice(notRemindedSavings))
  samplingMeanListNotReminded.append(statistics.mean(tempList))
meanSamplingNotReminded = statistics.mean(samplingMeanListNotReminded)
stdevSamplingNotReminded = statistics.stdev(samplingMeanListNotReminded)
print(f'Mean of Sampling (Not Reminded) -> {samplingMeanListNotReminded}')
print(f'Standard Deviation of Sampling (Not Reminded) -> {stdevSamplingNotReminded}')
fig = ff.create_distplot([samplingMeanListNotReminded], ['Savings (Sampling)'], show_hist = False)
fig.add_trace(go.Scatter(x = [samplingMeanListNotReminded], y = [0, 0.1], mode = 'lines', name = 'MEAN'))
fig.show()
firstStdDeviationStart = meanSamplingNotReminded - stdevSamplingNotReminded
firstStdDeviationEnd = meanSamplingNotReminded + stdevSamplingNotReminded
print(f'First (start) - {firstStdDeviationStart} and First (end) - {firstStdDeviationEnd}')
secondStdDeviationStart = meanSamplingNotReminded - (2 * stdevSamplingNotReminded)
secondStdDeviationEnd = meanSamplingNotReminded + (2 * stdevSamplingNotReminded)
print(f'Second (start) - {secondStdDeviationStart} and Second (end) - {secondStdDeviationEnd}')
thirdStdDeviationStart = meanSamplingNotReminded - (3 * stdevSamplingNotReminded)
thirdStdDeviationEnd = meanSamplingNotReminded + (3 * stdevSamplingNotReminded)
print(f'Third (start) - {thirdStdDeviationStart} and Third (end) - {thirdStdDeviationEnd}')
remindedSavings = remindedDf['quant_saved'].tolist()
samplingMeanListReminded = []
for i in range(1000):
  tempList = []
  for j in range(100):
    tempList.append(random.choice(remindedSavings))
  samplingMeanListReminded.append(statistics.mean(tempList))
meanSamplingReminded = statistics.mean(samplingMeanListReminded)
stdevSamplingReminded = statistics.stdev(samplingMeanListReminded)
print(f'Mean of Sampling (Reminded) -> {meanSamplingReminded}')
print(f'Standard Deviation of Sampling (Reminded) -> {stdevSamplingReminded}')
fig = ff.create_distplot([samplingMeanListReminded], ['Savings (Sampling)'], show_hist = False)
fig.add_trace(go.Scatter(x=[meanSampling, meanSampling], y=[0, 0.1], mode = 'lines', name = 'MEAN'))
fig.show()
zScore = (meanSamplingReminded - meanSamplingNotRreminded) / stdevSamplingNotReminded
print(f'Z-Score is - {zScore}')