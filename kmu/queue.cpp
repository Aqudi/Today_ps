#include <iostream>

using namespace std;

template <typename T>
class Queue
{
private:
	int sizeQueue;
	T *arrayOfData;
	int front; int rear; int size;
public:
	Queue(int size = 27) {
		sizeQueue = size;
		arrayOfData = new T[size];
		front = rear = -1;
	}
	void enQueue(T item) {
		if (!isFull()) {
			arrayOfData[++rear] = item;
		}
		else {
		}
	}
	T deQueue() {
		if (isEmpty()) {
			return -1;
		}
		else {
			T que_item = arrayOfData[++front];
			return que_item;
		}
	}
	bool isFull() {
		return rear == sizeQueue - 1;
	}
	bool isEmpty() {
		return front == rear;
	}
	void display_Queue() {
		int i;
		if (isEmpty()) {
		}
		else {
			i = front + 1;
			cout << "Que : ";
			while (i <= rear) {
				cout << arrayOfData[i] << " ";
				i = i + 1;
			}
			cout << endl;
		}
	}
};

template <typename T>
class Circle_Queue
{
private:
	int sizeQueue;
	T *arrayOfData;
	int front; int rear; int size;
public:
	Circle_Queue(int size = 27) {
		sizeQueue = size;
		arrayOfData = new T[size];
		front = rear = -1;
	}
	void enQueue(T item) {
		rear = (rear + 1) % sizeQueue;
		//cout << "front : " << front << " rear : " << rear << endl;

		if (front == rear) {
			cout << "CQ is Full\n";
		}
		else {
			arrayOfData[rear] = item;
		}
	}
	T deQueue() {
		front = (front + 1) % sizeQueue;
		if (front == rear) {
			cout << "CQ is Empty\n";
			return -1;
		}
		else {
			return arrayOfData[front];
		}
		//cout << "front : " << front << " rear : " << rear << endl;
	}
	bool isFull() {
		if ((rear + 1) % sizeQueue == front) {
			cout << "CQ is Full" << endl;
		}
		return (rear + 1) % sizeQueue == front;
	}
	bool isEmpty() {
		if (front == rear) {
			cout << "CQ is empty" << endl;
		}
		return front == rear;
	}
	void display_Queue() {
		int i;
		i = (front + 1) % sizeQueue;
		while (i != rear) {
			cout << "C_Que : " << arrayOfData[i] << " ";
			i = (i + 1) % sizeQueue;
			cout << endl;
		}
	}
};

int main()
{
	Queue<char> que(3);

	Circle_Queue<char> c_que(3);
	// # command 1
	que.enQueue('b');
	que.enQueue('c');
	que.enQueue('d');
	que.display_Queue();

	que.deQueue();
	que.deQueue();
	que.deQueue();
	que.deQueue();
	// # command 7
	cout << "원형큐 테스트 \n";
	c_que.enQueue('A');
	c_que.enQueue('B');
	c_que.enQueue('C');
	c_que.deQueue();
	c_que.enQueue('D');
	c_que.display_Queue();
	c_que.deQueue();
	c_que.deQueue();
	c_que.deQueue();
}