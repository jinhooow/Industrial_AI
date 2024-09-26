#include <iostream>
#include <fstream>
#include <math.h>
#include <Eigen/Dense>
#include <cstdlib> // for rand() and srand()
#include <ctime>   // for time()

using namespace std;

// 함수 f의 값을 계산하는 함수
double GetValue(Eigen::Matrix<double, 2, 1> Mat)
{
    double f = 0.05 * Mat(0, 0) * Mat(0, 0) + 0.1 * Mat(1, 0) * Mat(1, 0) + sin(Mat(0, 0));
    return f;
}

// f의 기울기(Gradient)를 계산하는 함수
Eigen::Matrix<double, 2, 1> GetGradient(Eigen::Matrix<double, 2, 1> Mat)
{
    Eigen::Matrix<double, 2, 1> G;
    G(0, 0) = 0.1 * Mat(0, 0) + cos(Mat(0, 0));
    G(1, 0) = 0.2 * Mat(1, 0);
    return G;
}

// f의 헤시안(Hessian) 행렬을 계산하는 함수
Eigen::Matrix<double, 2, 2> GetHessian(Eigen::Matrix<double, 2, 1> Mat)
{
    Eigen::Matrix<double, 2, 2> H;
    H(0, 0) = 0.1 - sin(Mat(0, 0));
    H(1, 1) = 0.2;
    H(0, 1) = 0.0;
    H(1, 0) = 0.0;
    return H;
}

int main()
{
    srand(time(0));  // 시드 초기화 (random number generation)
    
    Eigen::Matrix<double, 2, 1> X; // 탐색할 벡터
    Eigen::Matrix<double, 2, 1> GRAD;
    Eigen::Matrix<double, 2, 2> HESS;
    
    const int max_iterations = 100;  // Hill-Climber 반복 횟수
    const int restarts = 10;         // Random initializations 횟수
    
    double global_value_min = numeric_limits<double>::infinity(); // 전역 최적값
    Eigen::Matrix<double, 2, 1> X_GLOBAL_MIN;  // 전역 최소 지점

    cout.precision(4);

    for (int restart = 0; restart < restarts; ++restart) // 여러 번의 초기값을 무작위로 발생
    {
        // X의 초기값을 [-5.0, 5.0] 범위에서 무작위로 설정
        X(0, 0) = -5.0 + static_cast<double>(rand()) / RAND_MAX * 10.0;
        X(1, 0) = -5.0 + static_cast<double>(rand()) / RAND_MAX * 10.0;

        cout << "\nStarting new random initialization #" << restart + 1 << endl;
        cout << "Initial X0=" << X(0, 0) << " X1=" << X(1, 0) << endl;

        // Hill-Climber 알고리즘
        double value = GetValue(X);
        double value_min = value;
        Eigen::Matrix<double, 2, 1> X_MIN = X;

        bool improve;
        int iteration = 0;

        do
        {
            improve = false;
            GRAD = GetGradient(X);
            HESS = GetHessian(X);
            X -= HESS.inverse() * GRAD;  // Newton's method로 업데이트
            value = GetValue(X);
            cout << "Iter " << iteration << " value=" << value << " X0=" << X(0, 0) << " X1=" << X(1, 0) << endl;

            if (value < value_min)
            {
                improve = true;
                value_min = value;
                X_MIN = X;
            }

            iteration++;
        } while (improve && iteration < max_iterations);  // 일정 횟수 또는 더 이상 개선되지 않을 때까지 반복

        cout << "Local min found: value_min=" << value_min << " X0*=" << X_MIN(0, 0) << " X1*=" << X_MIN(1, 0) << endl;

        // 전역 최소값을 업데이트
        if (value_min < global_value_min)
        {
            global_value_min = value_min;
            X_GLOBAL_MIN = X_MIN;
        }
    }

    // 전역 최소값 출력
    cout << "\nGlobal minimum after " << restarts << " random restarts:" << endl;
    cout << "global_value_min=" << global_value_min << " X0*=" << X_GLOBAL_MIN(0, 0) << " X1*=" << X_GLOBAL_MIN(1, 0) << endl;

    return 0;
}

