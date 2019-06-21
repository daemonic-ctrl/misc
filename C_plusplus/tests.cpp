#include <iostream>

using namespace std;
constexpr int g_ceAddOne(int num) {return ++num;};

int main()
{
	int ivar = 0;
	cout << "Enter Value for var: ";
	cin >> ivar;

	cout << g_ceAddOne(ivar) << endl;

	int aArrayOne [g_ceAddOne(ivar)] = {ivar};
	int aArrayTwo [ivar] = {g_ceAddOne(ivar)};

	cout << aArrayOne[0] << endl;
	cout << aArrayTwo[0] << endl;

	return 0;
}
