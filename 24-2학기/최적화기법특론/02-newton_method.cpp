#include <iostream>
#include <fstream>
#include <math.h>

#include <Eigen/Dense>

using namespace std;
//using namespace Eigen;

double GetValue(Eigen::Matrix<double, 2, 1> Mat)
{
	double f = 0.05 * Mat(0, 0) * Mat(0, 0) + 0.1 * Mat(1, 0) * Mat(1, 0) + sin(Mat(0, 0));
	return f;
}

Eigen::Matrix<double, 2, 1> GetGradient(Eigen::Matrix<double, 2, 1> Mat)
{
	Eigen::Matrix<double, 2, 1> G;
	G(0, 0) = 0.1 * Mat(0, 0) + cos(Mat(0, 0));
	G(1, 0) = 0.2 * Mat(1, 0);
	return G;
}

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
	Eigen::Matrix<double, 2, 1> X {-2.0, -3.0}; // initial state
	
	Eigen::Matrix<double, 2, 1> GRAD;
	Eigen::Matrix<double, 2, 2> HESS;

	bool improve;
	double value = GetValue(X);
	
	cout.precision(4);
	cout << "value=" << value << " x0=" << X(0,0) << " x1=" << X(1, 0) << std::endl;
	
	double value_min = value;
	Eigen::Matrix<double, 2, 1> X_MIN = X;
	do
	{
		improve = false;
		GRAD = GetGradient(X);
		HESS = GetHessian(X);
		X -= HESS.inverse() * GRAD;
		value = GetValue(X);
		cout << "value=" << value << " x1=" << X(0, 0) << " x2=" << X(1, 0) << std::endl;
		if (value < value_min)
		{
			improve = true;
			value_min = value;
			X_MIN = X;
		}
	} while (improve);
	cout << "value_min=" << value_min << " x1*=" << X_MIN(0, 0) << " x2*=" << X_MIN(1, 0) << std::endl;
	return 0;
}