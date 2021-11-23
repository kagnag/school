#include <stdio.h>
#include <stdlib.h>
#include <stack>

using namespace std;

#define tankcapacity_X 10
#define tankcapacity_Y 5
#define tankcapacity_Z 6
#define empty_S 0
#define goal 8
#define Maxlength 100
//hang chuoi de in ra cac hanh dong
const char* action[] = {"First State", "pour Water X to Y","pour Water Y to Z",  "pour Water Z to X",
                        "pour Water X to Z",  "pour Water Z to Y", "pour Water Y to X"};

typedef struct{
     int x, y, z;
}State;
//khoi tao trang thai
void makeNullState(State *state){
    state->x = state->y = state->z = 0;
}
//in trang thai
void print_State(State state){
    printf("\n  X:%d --- Y:%d -- Z:%d", state.x, state.y, state.z);
}
//ham kiem tra trang thai muc tieus
int goalcheck(State state){
    return (state.x==goal);
}
//max
int max(int a, int b){
    return a > b ? a : b;
}
//min
int min(int a, int b){
    return a < b ? a : b;
}
//chuyen nuoc tu x qua y
int pourWaterXY(State cur_state, State *result){
    if(cur_state.x > 0 && cur_state.y < tankcapacity_Y){
        result->x = max(cur_state.x - (tankcapacity_Y - cur_state.y), empty_S);
        result->y = min(cur_state.x + cur_state.y, tankcapacity_Y);
        result->z = cur_state.z;
        return 1;
    }
    return 0;
}
//chuyen nuoc tu x qua z
int pourWaterXZ(State cur_state, State *result){
    if(cur_state.x > 0 && cur_state.z < tankcapacity_Z){
        result->x = max(cur_state.x - (tankcapacity_Z - cur_state.z), empty_S);
        result->z = min(cur_state.x + cur_state.z, tankcapacity_Z);
        result->y = cur_state.y;
        return 1;
    }
    return 0;
}
//chuyen nuoc tu y qua x
int pourWaterYX(State cur_state, State *result){
    if(cur_state.y >0 && cur_state.x < tankcapacity_X){
        result->y = max(cur_state.y - (tankcapacity_X - cur_state.x),empty_S);
        result->x = min(cur_state.x + cur_state.y, tankcapacity_X);
        result->z = cur_state.z;
        return 1;
    }
    return 0;
}
//chuyen nuoc tu y qua z
int pourWaterYZ(State cur_state, State *result){
    if(cur_state.y > 0 && cur_state.z < tankcapacity_Z){
        result->y = max(cur_state.y - (tankcapacity_Z - cur_state.z),empty_S);
        result->z = min(cur_state.z + cur_state.y, tankcapacity_Z);
        result->x = cur_state.x;
        return 1;
    }
    return 0;
}
//chuyen nuoc tu z qua x
int pourWaterZX(State cur_state, State *result){
    if(cur_state.z > 0 && cur_state.x < tankcapacity_X){
        result->z = max(cur_state.z - (tankcapacity_X - cur_state.x),empty_S);
        result->x = min(cur_state.x + cur_state.z, tankcapacity_X);
        result->y = cur_state.y;
        return 1;
    }
    return 0;
}
//chuyen nuoc tu z qua y
int pourWaterZY(State cur_state, State *result){
    if(cur_state.z > 0 && cur_state.y < tankcapacity_Y){
        result->z = max(cur_state.z - (tankcapacity_Y - cur_state.y), empty_S);
        result->y = min(cur_state.y + cur_state.z, tankcapacity_Y);
        result->x = cur_state.x;
        return 1;
    }
    return 0;
}
//so sanh hai trang thai co bang nhau khong
int compareStates(State state1, State state2){
    return (state1.x == state2.x && state1.y == state2.y || 
            state1.x == state2.x && state1.z == state2.z ||
            state1.y == state2.y && state1.z == state2.z);
}   
//goi cac trang thai hanh dong
int call_operator(State cur_state, State *result, int option) {
    switch(option) {
        case 1: return pourWaterXY(cur_state, result);
        case 2: return pourWaterYZ(cur_state, result);     
        case 3: return pourWaterZX(cur_state, result);     
        case 4: return pourWaterXZ(cur_state, result);    
        case 5: return pourWaterZY(cur_state, result);
        case 6: return pourWaterYX(cur_state, result);
        default: printf("Error calls operator!");
            return 0;
    }
}
//khai bao cau truc Node
typedef struct Node {
    State state;
    struct Node* Parent;
    int no_function;
}Node;
//tim trang thai trong Open/ Close
int find_State(State state, stack<Node*> openStack){
    while(!openStack.empty()){
        if(compareStates(openStack.top()->state, state))
            return 1;
        openStack.pop();
    }
    return 0;
}
//thuat toan duyet theo chieu sau
Node* DFS_Algorithm(State state){
    // khai bao hai ngan xep open va close
    stack<Node*> Open_DFS;
    stack<Node*> Close_DFS;
    //tao nut trang thai cha
    Node* root = (Node*)malloc(sizeof(Node));
    root->state = state;
    root->Parent = NULL;
    root->no_function = 0;
    Open_DFS.push(root);
    while(!Open_DFS.empty()){
        //lay mot dinh trong ngan xep
        Node* node = Open_DFS.top();
        Open_DFS.pop();
        Close_DFS.push(node);
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
                if(find_State(newstate, Close_DFS) || find_State(newstate, Open_DFS))
                    continue;
                //neu trang thai moi chua ton tai thi them vao ngan xep
                Node* newNode = (Node*)malloc(sizeof(Node));
                newNode->state = newstate;
                newNode->Parent = node;
                newNode->no_function = opt;
                Open_DFS.push(newNode);
            }
        }
    }
    return NULL;
}
//in ket qua chuyen nuoc de dat den trang thai muc tieu
void print_WaysToGetGoal(Node* node) {
    stack<Node*> stackPrint;
    //Duyet nguoc ve nut parent
    while (node->Parent != NULL) {
      stackPrint.push(node);
        node = node->Parent;
    }
    stackPrint.push(node);
    //In ra thu tu hanh dong chuyen nuoc
    int no_action = 0;
    while(!stackPrint.empty()) {
        printf("\nAction %d: %s", no_action, action[stackPrint.top()->no_function]);
        print_State(stackPrint.top()->state);
        stackPrint.pop();
        no_action++;
    }  
}
int main() {
    State cur_state = {10, 0, 0};
    Node* p = DFS_Algorithm(cur_state);
    print_WaysToGetGoal(p);
    return 0;
}