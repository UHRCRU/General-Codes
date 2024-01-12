#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};
struct node *front=0;
struct node *rear=0;

void enqueue(int x){
	struct node *newnode; 
	newnode = (struct node *)malloc(sizeof(struct node));
	newnode ->data = x;
	newnode ->next = 0;
	
	if(front==0 && rear==0){
		front=rear=newnode;
	}
	else{
		rear->next=newnode;
		rear=newnode;
	}
}

void display(){
	struct node *temp;
	if(front==0 && rear==0)
	{
		printf("Queue is empty. \n");
	}
	else{
		temp=front;
		while(temp!=0)
		{
			printf("%d \n", temp->data);
			temp=temp->next;
		}
	}
}

void peek(){
	if(front==0 && rear==0)
	printf("Queue is empty. \n");
	else{
		printf("Front element is %d \n", front->data);
	}
}

void dequeue(){
	struct node *temp;
	temp=front;
	if(front==0 && rear==0)
	printf("Queue is empty.");
	else{
		printf("Removed element is %d \n", front->data);
		front=front->next;
		free(temp);
	}
}

int main() {
	
display(); 
enqueue(8);
enqueue(2);
enqueue(-1);
display();
dequeue();
display();
peek();
enqueue(4);
display();

return 0;
}
