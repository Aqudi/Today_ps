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

int check(char exp[])
{
    stackarray checker;
    for (int i = 0; i < strlen(exp); i++)
    {
        if (exp[i] == '(' || exp[i] == '{' || exp[i] == '[')
        {
            checker.push(exp[i]);
        }
        if (exp[i] == ')' || exp[i] == '}' || exp[i] == ']')
            if (checker.isEmpty())
            {
                cout << "Unbalanced ";
                return false;
            }
            else
            {
                char temp = checker.pop();
                if (temp != '(' && exp[i] == ')')
                    cout << "Mismatched " << temp << " , " << exp[i];
                if (temp != '{' && exp[i] == '}')
                    cout << "Mismatched " << temp << " , " << exp[i];
                if (temp != '[' && exp[i] == ']')
                    cout << "Mismatched " << temp << " , " << exp[i];
            }
    }
    if (checker.isEmpty())
        return true;
    else
    {
        cout << "Unbalanced";
        return false;
    }
}

int main()
{
    ifstream reader;
    reader.open("Lab3.txt", ios::in);
    if (!reader.is_open())
    {
        cout << "파일을 열지 못했습니다.";
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
                cout << " valid\n";
            else
                cout << " Invalid\n";
        }
    }
}
