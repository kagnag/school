#include <stdio.h>
#include <stdlib.h>
#include <queue>

using namespace std;
#define sotusi 3
#define soquy 3
#define Maxlength 100

//hang chuoi de in cac hanh dong
const char* action[] = {"First State" ,"Chuyen 1 tu si va 1 con quy tu bo phai sang trai","Chuyen 1 tu si tu bo trai sang phai",
                        "Chuyen 2 con quy tu bo phai sang trai","Chuyen 1 con quy tu bo trai sang phai",
                        "Chuyen 2 tu si tu bo phai sang trai","Chuyen 1 tu si va 1 con quy tu bo trai sang phai",
                        "Chuyen 1 tu si tu bo phai sang trai","Chuyen 2 tu si tu bo trai sang phai",
                        "Chuyen 1 con quy tu bo phai sang trai","Chuyen 2 con quy bo trai sang phai"};
typedef struct {
    int tusi_L;    
    int quy_L;
    int tusi_R;
    int quy_R;
    int vitrithuyen;      
}State;
//khoi tao trang thai
void makeNullState(State *state) {
    state->tusi_L =  0;
    state->quy_L = 0;
    state->tusi_R = 0;
    state->quy_R = 0;
    state->vitrithuyen = 0; 
}
// in trang thai
void print_State(State state) {
    if(state.vitrithuyen == 1)
        printf("\n\tBo trai: Tu si %d - Quy %d ..... Thuyen dang o bo phai ..... Bo phai: Tu si %d - Quy: %d", state.tusi_L, state.quy_L, state.tusi_R, state.quy_R);
    else if(state.vitrithuyen == -1)
        printf("\n\tBo trai: Tu si %d - Quy %d ..... Thuyen dang o bo trai ..... Bo phai: Tu si %d - Quy: %d", state.tusi_L, state.quy_L, state.tusi_R, state.quy_R);
}
//ham kiem tra trang thai muc tieu
int goalcheck(State state) {
    return (state.tusi_R == 0 && state.quy_R == 0 && state.vitrithuyen == -1); 
}
//kiem tra dieu kien sau
int checkProblem(State cur_state) {
    if (cur_state.tusi_L <= sotusi && cur_state.tusi_R <= sotusi && cur_state.quy_L <= soquy && cur_state.quy_R <= soquy
	    && (cur_state.tusi_L == 0 || cur_state.tusi_L >= cur_state.quy_L)
	    && (cur_state.tusi_R == 0 || cur_state.tusi_R >= cur_state.quy_R))
        return 1;
    return 0;
}
// 1 chuyen 1 tu si tu bo L->R
int moveLR_1Tusi(State cur_state, State *result) {
    if( cur_state.vitrithuyen == -1) {
        result->tusi_L = cur_state.tusi_L - 1;
        result->quy_L = cur_state.quy_L;
        result->tusi_R = cur_state.tusi_R + 1;
        result->quy_R = cur_state.quy_R;
        result->vitrithuyen = 1; 
        if(checkProblem(*result))
            return 1;
    }
    return 0;
}
// 2 chuyen 1 quy tu bo L->R
int moveLR_1Quy(State cur_state, State *result) {
    if( cur_state.vitrithuyen == -1) {
        result->tusi_L = cur_state.tusi_L;
        result->quy_L = cur_state.quy_L - 1;
        result->tusi_R = cur_state.tusi_R;
        result->quy_R = cur_state.quy_R + 1;
        result->vitrithuyen = 1; 
        if(checkProblem(*result))
            return 1;
    }
    return 0;
}
// 3 chuyen 2 tu si tu bo L->R
int moveLR_2Tusi(State cur_state, State *result) {
    if( cur_state.vitrithuyen == -1) {
        result->tusi_L = cur_state.tusi_L - 2;
        result->quy_L = cur_state.quy_L;
        result->tusi_R = cur_state.tusi_R + 2;
        result->quy_R = cur_state.quy_R;
        result->vitrithuyen = 1; 
        if(checkProblem(*result))
            return 1;
    }
    return 0;
}
// 4 chuyen 2 quy tu bo L->R
int moveLR_2Quy(State cur_state, State *result) {
    if( cur_state.vitrithuyen == -1) {
        result->tusi_L = cur_state.tusi_L;
        result->quy_L = cur_state.quy_L - 2;
        result->tusi_R = cur_state.tusi_R;
        result->quy_R = cur_state.quy_R + 2;
        result->vitrithuyen = 1; ;
        if(checkProblem(*result))
            return 1;
    }
    return 0;
}
// 5 chuyen 1 tu si va 1 quy tu L->R
int moveLR_1Tusi_1Quy(State cur_state, State *result) {
    if( cur_state.vitrithuyen == -1) {
        result->tusi_L = cur_state.tusi_L - 1;
        result->quy_L = cur_state.quy_L - 1;
        result->tusi_R = cur_state.tusi_R + 1;
        result->quy_R = cur_state.quy_R + 1;
        result->vitrithuyen = 1; 
        if(checkProblem(*result))
            return 1;
    }
    return 0;
}
// 6 chuyen 1 tu si tu R->L
int moveRL_1Tusi(State cur_state, State *result) {
    if( cur_state.vitrithuyen == 1) {
        result->tusi_L = cur_state.tusi_L + 1;
        result->quy_L = cur_state.quy_L;
        result->tusi_R = cur_state.tusi_R - 1;
        result->quy_R = cur_state.quy_R;
        result->vitrithuyen = -1; 
        if(checkProblem(*result))
            return 1;
    }
    return 0;
}
// 7 chuyen 1 quy tu R->L
int moveRL_1Quy(State cur_state, State *result) {
    if( cur_state.vitrithuyen == 1) {
        result->tusi_L = cur_state.tusi_L;
        result->quy_L = cur_state.quy_L + 1;
        result->tusi_R = cur_state.tusi_R;
        result->quy_R = cur_state.quy_R - 1;
        result->vitrithuyen = -1;
        if(checkProblem(*result))
            return 1;
    }
    return 0;
}
// 8 chuyen 2 tu si tu R->L
int moveRL_2Tusi(State cur_state, State *result) {
    if( cur_state.vitrithuyen == 1) {
        result->tusi_L = cur_state.tusi_L + 2;
        result->quy_L = cur_state.quy_L;
        result->tusi_R = cur_state.tusi_R - 2;
        result->quy_R = cur_state.quy_R;
        result->vitrithuyen = -1;
        if(checkProblem(*result))
            return 1;
    }
    return 0;
}
// 9 chuyen 2 quy tu R->L
int moveRL_2Quy(State cur_state, State *result) {
    if( cur_state.vitrithuyen == 1) {
        result->tusi_L = cur_state.tusi_L;
        result->quy_L = cur_state.quy_L + 2;
        result->tusi_R = cur_state.tusi_R;
        result->quy_R = cur_state.quy_R - 2;
        result->vitrithuyen = -1;
        if(checkProblem(*result))
            return 1;
    }
    return 0;
}
// 10 chuyen 1 tu si va 1 quy tu
int moveRL_1Tusi_1Quy(State cur_state, State *result) {
    if( cur_state.vitrithuyen == 1) {
        result->tusi_L = cur_state.tusi_L + 1;
        result->quy_L = cur_state.quy_L + 1;
        result->tusi_R = cur_state.tusi_R - 1;
        result->quy_R = cur_state.quy_R - 1;
        result->vitrithuyen = -1;
        if(checkProblem(*result))
            return 1;
    }
    return 0;
}
//goi trang thai cac hanh dong
int call_operator(State cur_state, State *result, int option) {
    switch(option) {
        case 1: return moveRL_1Tusi_1Quy(cur_state, result);
        case 2: return moveLR_1Tusi(cur_state, result);
        case 3: return moveRL_2Quy(cur_state, result);
        case 4: return moveLR_1Quy(cur_state, result);
        case 5: return moveRL_2Tusi(cur_state, result);
        case 6: return moveLR_1Tusi_1Quy(cur_state, result); 
        case 7: return moveRL_1Tusi(cur_state, result);
        case 8: return moveLR_2Tusi(cur_state, result);
        case 9: return moveRL_1Quy(cur_state, result);
        case 10: return moveLR_2Quy(cur_state, result);   
        default: printf("\nError calls operator!"); 
            return 0;
    }
}
//khai bao Node
typedef struct Node {
    State state;
    struct Node* Parent;
    int no_function;
}Node;
//so sanh hai trang thai co bang nhau khong
int compareStates(State state1, State state2) {
    return (state1.tusi_L == state2.tusi_L && state1.tusi_R == state2.tusi_R 
        && state1.quy_L == state2.quy_L && state1.quy_R == state2.quy_R 
        && state1.vitrithuyen == state2.vitrithuyen);
}   
//tim trang thai trong Open/ Close
int find_State(State state, queue<Node*> openQueue){
    while(!openQueue.empty()){
        if(compareStates(openQueue.front()->state, state))
            return 1;
        openQueue.pop();
    }
    return 0;
}
//thuat toan duyet theo chieu sau
Node* BFS_Algorithm(State state){
    //khai bao hai ngan xep open va close
    queue<Node*> Open_BFS;
    queue<Node*> Close_BFS;
    //tao nut trang thai cha
    Node* root = (Node*)malloc(sizeof(Node));
    root->state = state;
    root->Parent = NULL;
    root->no_function = 0;
    Open_BFS.push(root);
    while(!Open_BFS.empty()){
        //lay mot dinh trong ngan xep
        Node* node = Open_BFS.front();
        Open_BFS.pop();
        Close_BFS.push(node);
        //kiem tra xem dinh lay ra co phai trang thai muc tieu
        if(goalcheck(node->state))
            return node;
        int opt;
        //goi cac phep toan tren trang thai
        for(opt = 1; opt <= 6; opt++){
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
                Open_BFS.push(newNode);
            }
        }
    }
    return NULL;
}
//dao nguoc queue
void reverseQueue(queue<Node*> &q) {
    if (q.empty())
        return;
    Node* cur = q.front();
    q.pop();
    reverseQueue(q);
    q.push(cur);
}
//in ket qua chuyen nuoc de dat den trang thai muc tieu
void print_WaysToGetGoal(Node* node) {
    queue<Node*> QueuePrint;
    //Duyet nguoc ve nut parent
    while (node->Parent != NULL) {
      QueuePrint.push(node);
        node = node->Parent;
    }
    QueuePrint.push(node);
    reverseQueue(QueuePrint);
    //In ra thu tu hanh dong chuyen nuoc
    int no_action = 0;
    while(!QueuePrint.empty()) {
        printf("\nAction %d: %s", no_action, action[QueuePrint.front()->no_function]);
        print_State(QueuePrint.front()->state);
        QueuePrint.pop();
        no_action++;
    }  
}
int main() {
    State cur_state = {0, 0, 3, 3, 1};
    Node* p = BFS_Algorithm(cur_state);
    print_WaysToGetGoal(p);
    return 0;
}
