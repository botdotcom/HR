//Generate nth Fibonacci number using recursive algorithm
#include <iostream>

using namespace std;

//Recursion: Fibonacci Numbers

int fibonacci(int n) 
{
    if(n == 0)
        return 0;
    else if(n == 1)
        return 1;
    else
        return (fibonacci(n-1) + fibonacci(n-2));
}
int main() {
    int n;
    cin >> n;
    cout << fibonacci(n);
    return 0;
}
