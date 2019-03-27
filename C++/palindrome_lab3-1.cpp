#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

using namespace std;

const int Stack_Size = 1000;

class stackarray
{
  private:
    char stack[Stack_Size];
    int top;

  public:
    stackarray() { top = -1; }
    void push(char item) { stack[++top] = item; }
    char pop() { return stack[top--]; }
    int isEmpty() { return top == -1; }
    int isFull() { return top == Stack_Size - 1; }
    void displayStack()
    {
        int cusur;
        if (isEmpty())
        {
            cout << "Stack is empty!\n";
        }
        else
        {
            cusur = top;
            while (cusur != -1)
                cout << stack[--cusur] << " ";
        }
        cout << "\n";
    }
};

int compare(char buffer, char ch)
{
    bool result = buffer == ch;
    cout << result;
    return buffer == ch;
}

int check(char exp[])
{
    stackarray checker;
    int length = strlen(exp);
    int i = 0;
    if (length % 2 == 0)
    {
        while (i < length / 2)
        {
            checker.push(exp[i++]);
        }
        while (i < length)
        {
            int j = checker.pop();
            if (!compare(exp[i], j)){
                return 0;
            }
            i++;
        }
    }
    else if (length % 2 == 1)
    {
        while (i < length / 2)
        {
            checker.push(exp[i++]);
        }
        i++;
        while (i < length)
        {
            int j = checker.pop();
            if (!compare(exp[i], j)){
                return 0;
            }
            i++;
        }
    }
}

int main()
{
    ifstream reader;
    reader.open("Lab3-1.txt", ios::in);
    if (!reader.is_open())
    {
        cout << "File is not opened";
        exit(1);
    }
    else
    {
        char buffer[80];
        while (reader.getline(buffer, 80))
        {
            cout << buffer << "\t";
            bool validity = check(buffer);
            if (validity)
                cout << " a palindrome\n";
            else
                cout << " not a palindrome\n";
        }
    }
}