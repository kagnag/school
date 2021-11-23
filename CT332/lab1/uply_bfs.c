#include <stdio.h>
#include <stdlib.h>

#define Maxlength 100
//hang chuoi sinh ra hanh dong
const char* action[] = {"First State", "Lat 234", "Lat 456", "Lat 345", "Lat 123"};

 typedef struct {
     int glass1, glass2, glass3, glass4, glass5, glass6;
 }State;
 //khoi tao trang thai
 void makeNullState(State *state) {
     state->glass1 = -1;
     state->glass2 = -1;
     state->glass3 = -1;
     state->glass4 = -1;
     state->glass5 = -1;
     state->glass6 = -1;
 }
//in trang thai
void print_State(State state) {
    printf("\n\t%d %d %d %d %d %d ", state.glass1, state.glass2, state.glass3, state.glass4, state.glass5, state.glass6);
}
//kiem tra trang thai muc tieu
int goalcheck(State state) {
    return (state.glass1 + state.glass2 + state.glass3 + state.glass4 + state.glass5 + state.glass6 == 6);
}
//lat ly 1
int flip_1(State *cur_state) {
    if(cur_state->glass1 == 1)
    return cur_state->glass1 = 0;
    return cur_state->glass1 = 1;
}
//lat ly 2
int flip_2(State *cur_state) {
    if(cur_state->glass2 == 1)
    return cur_state->glass2 = 0;
    return cur_state->glass2 = 1;
}
//lat ly 3
int flip_3(State *cur_state) {
    if(cur_state->glass3 == 1)
    return cur_state->glass3 = 0;
    return cur_state->glass3 = 1;
}
//lat ly 4
int flip_4(State *cur_state) {
    if(cur_state->glass4 == 1)
    return cur_state->glass4 = 0;
    return cur_state->glass4 = 1;
}
//lat ly 5
int flip_5(State *cur_state) {
    if(cur_state->glass5 == 1)
    return cur_state->glass5 = 0;
    return cur_state->glass5 = 1;
}
//lat ly 6
int flip_6(State *cur_state) {
    if(cur_state->glass6 == 1)
    return cur_state->glass6 = 0;
    return cur_state->glass6 = 1;
}
//lat ly 123
int flip_123(State cur_state, State *result) {
    if(cur_state.glass1 + cur_state.glass2 + cur_state.glass3 == 3)
        return 0;
    result->glass1 = flip_1(&cur_state);
    result->glass2 = flip_2(&cur_state);
    result->glass3 = flip_3(&cur_state);
    result->glass4 = cur_state.glass4;
    result->glass5 = cur_state.glass5;
    result->glass6 = cur_state.glass6;
    return 1;
}
//lat ly 234
int flip_234(State cur_state, State *result) {
    if(cur_state.glass2 + cur_state.glass3 + cur_state.glass4 == 3)
        return 0;
    result->glass1 = cur_state.glass1;
    result->glass2 = flip_2(&cur_state);
    result->glass3 = flip_3(&cur_state);
    result->glass4 = flip_4(&cur_state);
    result->glass5 = cur_state.glass5;
    result->glass6 = cur_state.glass6;
    return 1;
}
//lat ly 345
int flip_345(State cur_state, State *result) {
    if(cur_state.glass3 + cur_state.glass4 + cur_state.glass5 == 3)
        return 0;
    result->glass1 = cur_state.glass1;
    result->glass2 = cur_state.glass2;
    result->glass3 = flip_3(&cur_state);
    result->glass4 = flip_4(&cur_state);
    result->glass5 = flip_5(&cur_state);
    result->glass6 = cur_state.glass6;
    return 1;
}
//lat ly 456
int flip_456(State cur_state, State *result) {
    if(cur_state.glass4 + cur_state.glass5 + cur_state.glass6 == 3)
        return 0;
    result->glass1 = cur_state.glass1;
    result->glass2 = cur_state.glass2;
    result->glass3 = cur_state.glass3;
    result->glass4 = flip_4(&cur_state);
    result->glass5 = flip_5(&cur_state);
    result->glass6 = flip_6(&cur_state);
    return 1;
}
//so sanh hai trang thai co bang nhau khong
int compareStates(State state1, State state2){
    return (state1.glass1 == state2.glass1 && state1.glass2 == state2.glass2 &&
    state1.glass3== state2.glass3 && state1.glass4 == state2.glass4 && 
    state1.glass5 == state2.glass5 && state1.glass6 == state2.glass6);
}   
//goi trang thai cac hanh dong
int call_operator(State cur_state, State *result, int option){
    switch(option){
        case 1: return flip_234(cur_state, result); 
        case 2: return flip_456(cur_state, result);
        case 3: return flip_345(cur_state, result);
        case 4: return flip_123(cur_state, result);
        default: printf("Error calls operator!");
            return 0;
    }
}
//khai bao Node
typedef struct Node{
    State state;
    struct Node* Parent;
    int no_function;
}Node;
//khai bao cau truc Queue
 typedef struct {
     Node* Elements[Maxlength];
     int front, rear;
 }Queue;
//khoi tao hang doi rong
 void makeNull_Queue(Queue *queue) {
     queue->front = -1;
     queue->rear = -1;
 }
 //kiem tra hang doi co rong hay khong
 int empty_Queue(Queue queue) {
     return queue.front == -1;
 }
 //kiem tra hang doi co day hay khong
 int full_Queue(Queue queue) {
     return ((queue.rear - queue.front + 1)%Maxlength) == 0;
 }
 //tra ve phan tu dau hang doi
 Node* get_Front(Queue queue) {
     if(empty_Queue(queue)) 
         printf("Queue is empty!");
    else   
        return queue.Elements[queue.front];
 }
 //xoa bo mot phan tu khoi hang doi
 void del_Queue(Queue *queue) {
     if(!empty_Queue(*queue)) {
         if(queue->front == queue->rear)
            makeNull_Queue(queue);
        else 
            queue->front = (queue->front+1)%Maxlength;
     }
     else
        printf("Error, Delete");
 }
 //Them phan tu vao hang doi
 void push_Queue(Node* x, Queue *queue) {
     if(!full_Queue(*queue)) {
         if(empty_Queue(*queue))
            queue->front = 0;
        queue->rear = (queue->rear+1)%Maxlength;
        queue->Elements[queue->rear] = x;
     }
     else  
        printf("Error, Push");
 }
 //tim trang thai trong Open/ Close
int find_State(State state, Queue openQueue){
    while(!empty_Queue(openQueue)){
        if(compareStates(get_Front(openQueue)->state,state))
            return 1;
        del_Queue(&openQueue);
    }
    return 0;
}
//thuat toan duyet theo chieu rong
Node* BFS_Algorithm(State state){
    //khai bao hai ngan xep open va close
    Queue Open_BFS;
    Queue Close_BFS;
    makeNull_Queue(&Open_BFS);
    makeNull_Queue(&Close_BFS);
    //tao nut trang thai cha
    Node* root = (Node*)malloc(sizeof(Node));
    root->state = state;
    root->Parent = NULL;
    root->no_function = 0;
    push_Queue(root, &Open_BFS);
    while(!empty_Queue(Open_BFS)){
        //lay mot dinh trong ngan xep
        Node* node = get_Front(Open_BFS);
        del_Queue(&Open_BFS);
        push_Queue(node, &Close_BFS);
        //kiem tra xem dinh lay ra co phai trang thai muc tieu
        if(goalcheck(node->state))
            return node;
        int opt;
        //goi cac phep toan tren trang thai
        for(opt = 1; opt <= 4; opt++){
            State newstate;
            makeNullState(&newstate);
            if(call_operator(node->state, &newstate, opt)){
                //neu trang thai moi sinh ra ton tai thi bo qua
                if(find_State(newstate, Close_BFS) || find_State(newstate, Open_BFS))
                    continue;
                //neu trang thai moi chua ton tai thi them vao ngan xep
                Node* newNode = (Node*)malloc(sizeof(Node));
                newNode->state = newstate;
                newNode->Parent = node;
                newNode->no_function = opt;
                push_Queue(newNode, &Open_BFS);
            }
        }
    }
    return NULL;
}
//dao nguoc hang doi
void reverseQueue(Queue *q) {
    if (empty_Queue(*q))
        return;
    Node* curr = get_Front(*q); 
    del_Queue(q); 
    reverseQueue(q);
    push_Queue(curr, q);
}

//in ket qua chuyen nuoc de dat den trang thai muc tieu
void print_WaysToGetGoal(Node* node) {
    Queue QueuePrint;
    makeNull_Queue(&QueuePrint);
    //Duyet nguoc ve nut parent
    while (node->Parent != NULL) {
        push_Queue(node, &QueuePrint);
        node = node->Parent;
    }
    push_Queue(node, &QueuePrint);
    reverseQueue(&QueuePrint);
    //In ra thu tu hanh dong chuyen nuoc
    int no_action = 0;
    while(!empty_Queue(QueuePrint)) {
        printf("\nAction %d: %s", no_action, action[get_Front(QueuePrint)->no_function]);
        print_State(get_Front(QueuePrint)->state);
        del_Queue(&QueuePrint);
        no_action++;
    }  
}
int main() {
    State cur_state = {1, 0, 1, 0, 1 ,0};
    Node* p = BFS_Algorithm(cur_state);
    print_WaysToGetGoal(p);
    return 0;
}
