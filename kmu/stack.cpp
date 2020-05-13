#include <iostream>
#include <string>

using namespace std;

/*********************************************************
* Class 	 : stack
* Desciption : 타입변수 T를 사용하여 경우에 따라서 유연하게 타입을 선언할 수 있는 스택
* Variables	 :
	stack_array - 스택의 아이템들을 저장하는 배열
	top - 스택의 맨 윗부분을 가르키는 변수
	
	push - 스택의 top위치에 수를 집어넣고 동시에 top의 값을 1 증가시킴
	pop - 스택의 top위치에 있는 수를 반환함과 동시에 top의 값을 1 감소시킴
	peek - 스택의 top위치에 있는 수를 반환
	isEmpty - 스택이 비었으면 1, 아니면 0
	isFull - 스택이 꽉 찼으면 1, 아니면 0
	displaystack - 스택내부의 내용들을 출력
*********************************************************/
template <typename T>
class stackarray
{
private:
	T *stack; // 스택 본체
	int top; // 스택 맨 위의 인덱스
	int Stack_Size;

public:
	stackarray(int size = 1024)
	{
		Stack_Size = size;
		stack = new T[Stack_Size];
		top = -1;
	}
	void push(T item)
	{
		if (!isFull()) {
			stack[++top] = item;
		}
	}
	T pop()
	{
		if (!isEmpty()) {
			T pop_item = stack[top--];
			return pop_item;
		}
	}
	T peek()
	{
		if (!isEmpty()) {
			T peek_item = stack[top];
			cout << peek_item << endl;
			return peek_item;
		}
	}
	int isEmpty()
	{
		return top == -1;
	}
	int isFull()
	{
		return top == Stack_Size - 1;
	}
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
				cout << stack[cusur--] << " ";
		}
		cout << "\n";
	}
};

int main()
{
	stackarray<int> my_stack;
	string input = "";
	int num;
	while (input.compare("q") != 0)
	{
		cout << "Enter command(push, pop, peek, traverse, q): ";
		cin >> input;
		if (input.compare("push") == 0)
		{
			if (!my_stack.isFull())
			{
				cout << "Enter an integer to push == > ";

				cin >> num;
				my_stack.push(num);
			}
			else
				cout << "Stack is full \n";
			continue;
		}
		if (input.compare("pop") == 0)
		{
			if (!my_stack.isEmpty())
			{
				int result;
				result = my_stack.pop();
				cout << result << " is poped.\n";
			}
			else
				cout << "Stack is empty \n";
			continue;
		}
		else if (input.compare("peek") == 0)
			my_stack.peek();
		else if (input.compare("traverse") == 0 && input.compare("q") != 0)
			my_stack.displayStack();
		else
			cout << "Try input the correct command\n";
		continue;
	}

	return 0;
}