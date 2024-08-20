import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# CSV 파일에서 데이터를 불러옵니다.
data = pd.read_csv('C:/Users/M/Desktop/대학원/산업인공지능학개론/과제/machine learning/sensor_data.csv')

# 'Driving state'를 수치적으로 변환합니다.
data['Driving state'] = data['Driving state'].map({'Forward': 1, 'Backward': -1, 'Stopped': 0})

# 센서 데이터를 입력 특성과 출력 레이블로 변환합니다.
X = data[['Speed', 'Acceleration', 'Steering angle']].values
y = data['Driving state'].values

# 데이터를 학습용과 테스트용으로 분할합니다.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 회귀 모델을 초기화하고 학습시킵니다.
model = LinearRegression()
model.fit(X_train, y_train)

# 테스트 데이터에 대해 예측을 수행합니다.
y_pred = model.predict(X_test)

# 평가 지표를 계산합니다.
mse = mean_squared_error(y_test, y_pred)
print("평균 제곱 오차 (MSE):", mse)


import matplotlib.pyplot as plt

# 조향각에 따른 우회전과 좌회전을 구분하는 그래프
plt.figure(figsize=(10, 6))
plt.scatter(data[data['Turning direction'] == 'Right turn']['Steering angle'], data[data['Turning direction'] == 'Right turn']['Driving state'], label='Right turn', color='blue')
plt.scatter(data[data['Turning direction'] == 'Left turn']['Steering angle'], data[data['Turning direction'] == 'Left turn']['Driving state'], label='Left turn', color='red')
plt.xlabel("Steering Angle")
plt.ylabel("Driving State")
plt.title("Steering Angle vs Driving State (Turn Direction)")
plt.legend()
plt.show()

# 가속도를 이용한 급정지과 급출발을 구분하는 그래프
plt.figure(figsize=(10, 6))
plt.scatter(data[data['Driving condition'] == 'Rapid deceleration']['Acceleration'], data[data['Driving condition'] == 'Rapid deceleration']['Driving state'], label='Rapid deceleration', color='blue')
plt.scatter(data[data['Driving condition'] == 'Rapid acceleration']['Acceleration'], data[data['Driving condition'] == 'Rapid acceleration']['Driving state'], label='Rapid acceleration', color='red')
plt.xlabel("Acceleration")
plt.ylabel("Driving State")
plt.title("Acceleration vs Driving State (Driving Condition)")
plt.legend()
plt.show()

# 속도를 이용한 후진과 전진을 구분하는 그래프
plt.figure(figsize=(10, 6))
plt.scatter(data[data['Driving state'] == 'Forward']['Speed'], data[data['Driving state'] == 'Forward']['Driving state'], label='Forward', color='blue')
plt.scatter(data[data['Driving state'] == 'Backward']['Speed'], data[data['Driving state'] == 'Backward']['Driving state'], label='Backward', color='red')
plt.xlabel("Speed")
plt.ylabel("Driving State")
plt.title("Speed vs Driving State (Driving Direction)")
plt.legend()
plt.show()
