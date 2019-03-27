#include <iostream>
#include <sstream>
#include <stdio.h>
#include <string.h>

using namespace std;
const int Stack_Size = 1000;

class stackarray
{
  private:
    int stack[Stack_Size];
    int top;

  public:
    stackarray() { top = -1; }
    void push(int item) { stack[++top] = item; }
    void pop() { cout << stack[top--] << "\n"; }
    void size() { cout << top + 1 << "\n"; }
    void peek() { cout << stack[top] << "\n"; }
    int isEmpty() { return (top == -1) ? 1 : 0; }
    int isFull() { return top == Stack_Size - 1; }
};

int main()
{
    stackarray my_stack;
    char str[6] ;
    int n, num;

    scanf("%d", &n);
    fgetc(stdin);

    for (int i = 0; i < n; i++)
    {
        scanf("%s", str);
        fgetc(stdin);

        if (!strcmp(str, "push"))
        {
            scanf("%d", &num);
            fgetc(stdin);
            if (!my_stack.isFull()) my_stack.push(num);
            // else
            //     cout << "Stack is full \n";
            continue;
        }
        if (!strcmp(str, "pop"))
        {
            if (!my_stack.isEmpty()) my_stack.pop();
            else cout << "-1\n";
                
            // else
            //     cout << "Stack is empty \n";
            continue;
        }
                if (!strcmp(str, "empty"))
        {
            cout << my_stack.isEmpty() << "\n";
            continue;
        }

        if (!strcmp(str, "top"))
        {
            if (!my_stack.isEmpty())
                my_stack.peek();
            else cout << "-1\n";
            continue;
        }
        if (!strcmp(str, "size"))
            my_stack.size();
            continue;
    }

    return 0;
}