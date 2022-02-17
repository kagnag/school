#include <stdio.h>
#include <stdlib.h>

#define ROWS 3
#define COLS 3
#define EMPTY 0
#define MAX_OPERATOR 4
#define Maxlength 500

const char*  action[] = {"First State", "Move cell EMPTY to UP","Move cell EMTPY to DOWN",
                        "move cell EMPTY to LEFT","move cell EMPTY to RIGHT"};
//khai bao cau truc trang thai cua 8_puzzle
typedef struct{
    int eightPuzzle[ROWS][COLS];
    int emptyRow;
    int emptyCol;
}State;
//in trang thai cua 8-puzzle
void printState(State state) {
    int row, col;
    printf("\n---------\n");
    for(row = 0; row<ROWS; row++) {
        for(col = 0; col<COLS; col++)
            printf("|%d ", state.eightPuzzle[row][col]);
        printf("|\n");
        }
    printf("\n---------\n");
}
//so sanh hai trang thai
int compareStates(State state1, State state2) {
    if(state1.emptyRow != state2.emptyRow || state1.emptyCol != state2.emptyCol)
        return 0;
    int row, col;
    for(row=0; row<ROWS; row++) 
        for(col=0; col<COLS; col++)
            if(state1.eightPuzzle[row][col] != state2.eightPuzzle[row][col])
                return 0;
    return 1;
}
//kiem tra trang thai muc tieu
int goalCheck(State state, State goal) {
    return compareStates(state, goal);
}
//ham chuyen o trong len tren
int upOperator(State state, State *result) {
    *result = state;
    int empRowCurrent = state.emptyRow, empColCurrent = state.emptyCol;
    if(empRowCurrent > 0) {
        result->emptyRow = empRowCurrent - 1;
        result->emptyCol = empColCurrent;
        result->eightPuzzle[empRowCurrent][empColCurrent] =state.eightPuzzle[empRowCurrent - 1][empColCurrent];
        result->eightPuzzle[empRowCurrent - 1][empColCurrent] = EMPTY;
        return 1;
    }
    return 0;
}
//ham chuyen o torng xuong duoi
int downOperator(State state, State *result) {
    *result = state;
    int empRowCurrent = state.emptyRow, empColCurrent = state.emptyCol;
    if(empRowCurrent < 2) {
        result->emptyRow = empRowCurrent + 1;
        result->emptyCol = empColCurrent;
        result->eightPuzzle[empRowCurrent][empColCurrent] =state.eightPuzzle[empRowCurrent + 1][empColCurrent];
        result->eightPuzzle[empRowCurrent + 1][empColCurrent] = EMPTY;
        return 1;
    }
    return 0;
}
//ham chuyen o trong sang phai
int leftOperator(State state, State *result) {
    *result = state;
    int empRowCurrent = state.emptyRow, empColCurrent = state.emptyCol;
    if(empColCurrent > 0) {
        result->emptyRow = empRowCurrent;
        result->emptyCol = empColCurrent - 1;
        result->eightPuzzle[empRowCurrent][empColCurrent] =state.eightPuzzle[empRowCurrent][empColCurrent - 1];
        result->eightPuzzle[empRowCurrent][empColCurrent - 1] = EMPTY;
        return 1;
    }
    return 0;
}
//ham chuyen o trong sang trai
int rightOperator(State state, State *result) {
    *result = state;
    int empRowCurrent = state.emptyRow, empColCurrent = state.emptyCol;
    if(empColCurrent < 2) {
        result->emptyRow = empRowCurrent;
        result->emptyCol = empColCurrent + 1;
        result->eightPuzzle[empRowCurrent][empColCurrent] =state.eightPuzzle[empRowCurrent][empColCurrent + 1];
        result->eightPuzzle[empRowCurrent][empColCurrent + 1] = EMPTY;
        return 1;
    }
    return 0;
}
//ham goi cac hanh dong chuyen o trong
int callOperators(State state, State *result, int opt) {
    switch(opt) {
        case 1: return upOperator(state, result);
        case 2: return downOperator(state, result);
        case 3: return leftOperator(state, result);
        case 4: return rightOperator(state, result);
        default: printf("Cannot call operators");
            return 0;
    }
}
//ham heuristic 1
//dem so o sai khac voi trang thai muc tieu
int heuristic1(State state, State goal) {
    int row, col, count = 0;
    for(row=0; row<ROWS; row++)
        for(col=0; col<COLS; col++)
            if(state.eightPuzzle[row][col] != goal.eightPuzzle[row][col])
                count++;
    return count;
}
//ham heuristic 2
//dem so buoc chuyen o sai ve dung cua trang thai muc tieu
int heuristic2(State state, State goal) {
    int count = 0;
    int row, col, row_g, col_g;
    for(row=0; row<ROWS; row++) 
        for(col=0; col<COLS; col++) 
            if(state.eightPuzzle[row][col] != EMPTY) {
                for(row_g = 0; row_g<ROWS; row_g++)
                    for(col_g = 0; col_g<COLS; col_g++)
                        if(state.eightPuzzle[row][col] == goal.eightPuzzle[row_g][col_g]) {
                            count += abs(row - row_g) + abs(col - col_g);
                            col_g = COLS;
                            row_g = ROWS;
                        }
            }
    return count;
}
//khai bao cau truc Node de dung cay tim kiem
typedef struct Node {
    State state;
    struct Node* parent;
    int no_function;
    int f; //f = g+h
    int g; //chi phi tu trang thai bat dau -start- den trang thai hien tai
    int h; //chi phi tu trang thai hien tai den trang thai dich -goal-
}Node;
//khai bao cau truc danh sach
typedef struct {
    Node* Elements[Maxlength];
    int size;
}List;
//khoi tao danh sach rong
void makeNull_List(List *list) {
    list->size = 0;
}
//kiem tra danh sach rong
int empty_List(List list) {
    return(list.size == 0);
}
//kiem tra danh sach day
int full_List(List list) {
    return(list.size == Maxlength);
}
//truy van gia tri cua phan tu vi tri p
Node* element_at(int p, List list) {
         return list.Elements[p-1];
}
//them phan tu vao vi tri position trong danh sach
void push_List(Node* x, int position, List *list) {
    if(!full_List(*list)) {
        int q;
        for(q=list->size; q>=position; q--)
            list->Elements[q] = list->Elements[q-1];
        list->Elements[position-1] = x;
        list->size++;
    }
    else printf("List is full\n");
}
//xoa phan tu tai vi tri position ra khoi danh sach
void delete_List(int position, List *list) {
    if(empty_List(*list))
        printf("List is empty!");
    else if(position<1 || position>list->size)
        printf("Position is not possible to delete\n");
    else {
        int i;
        for(i=position-1; i<list->size; i++)
            list->Elements[i]=list->Elements[i+1];
        list->size--;
    }
}
//tim trang thai State co thuoc Open hay Close hay ko?
//luu vi tri tim duoc vao bien *position
Node* find_State(State state, List list, int *position) {
    int i;
    for(i=1; i<=list.size; i++)
        if(compareStates(element_at(i, list)->state, state)) {
            *position = i;
            return element_at(i, list);
        }
    return NULL;
}
//sap xep danh sach theo trong so heuristic
void sort_List(List *list) {
    int i, j;
    for(i=0; i<list->size-1; i++)
        for(j=i+1; j<list->size; j++)
            if(list->Elements[i]->f > list->Elements[j]->f) {
                Node* node = list->Elements[i];
                list->Elements[i] = list->Elements[j];
                list->Elements[j] = node;
            }
}
//thuat toan tim kiem tot nhat dau tien
//ham f = g + h
Node* A_Star(State state, State goal) {
    List Open_A_Star;
    List Close_A_Star;
    makeNull_List(&Open_A_Star);
    makeNull_List(&Close_A_Star);
    Node* root = (Node*)malloc(sizeof(Node));
    root->state = state;
    root->parent = NULL;
    root->no_function = 0;
    root->g = 0;
    root->h = heuristic1(root->state, goal);
    root->f = root->g + root->h;
    push_List(root, Open_A_Star.size+1, &Open_A_Star);
    while (!empty_List(Open_A_Star)) {
        Node* node = element_at(1, Open_A_Star);
        delete_List(1, &Open_A_Star);
        push_List(node, Close_A_Star.size+1, &Close_A_Star);
        if(goalCheck(node->state, goal))
            return node;
        int opt;
        for(opt=1; opt<=MAX_OPERATOR; opt++) {
            State newstate;
            if(callOperators(node->state, &newstate, opt)) {
                Node* newNode = (Node*)malloc(sizeof(Node));
                newNode->state = newstate;
                newNode->parent = node;
                newNode->no_function = opt;
                newNode->g = node->g + 1;
                newNode->h = heuristic1(root->state, goal);
                newNode->f = newNode->g + newNode->h;
                //kiem tra trang thai moi sinh ra co thuoc Open_A_Star/ Close_A_Star
                int pos_Open, pos_Close;
                Node* nodeFoundOpen = find_State(newstate, Open_A_Star, &pos_Open);
                Node* nodeFoundClose = find_State(newstate, Close_A_Star, &pos_Close);
                if(nodeFoundOpen == NULL && nodeFoundClose == NULL) 
                    push_List(newNode, Open_A_Star.size+1, &Open_A_Star);
                else if(nodeFoundOpen != NULL && nodeFoundOpen->g > newNode->g) {
                    delete_List(pos_Open, &Open_A_Star);
                    push_List(newNode, pos_Open, &Open_A_Star);
                }
                else if(nodeFoundClose != NULL && nodeFoundClose->g > newNode->g) {
                    delete_List(pos_Close, &Close_A_Star);
                    push_List(newNode, Open_A_Star.size+1, &Open_A_Star);
                }
            }
        }
        sort_List(&Open_A_Star);
    }
    return NULL;
}
//ham in ket qua cua thuat toan BFS
void print_WayToGetGoal(Node* node) {
    List listPrint;
    makeNull_List(&listPrint);
    //duyet nguoc ve nut parent
    while (node->parent != NULL) {
        push_List(node, listPrint.size+1, &listPrint);
        node = node->parent;
    }
    push_List(node, listPrint.size+1, &listPrint);
    //in ra thu tu hanh dong di chuyen o trong
    int no_action = 0, i;
    for(i=listPrint.size; i>0; i--) {
        printf("\nAction %d: %s", no_action, action[element_at(i, listPrint)->no_function]);
        printState(element_at(i, listPrint)->state);
        no_action++;
    }
}
int main() {
    State state;//, result;
        state.emptyRow = 1;
        state.emptyCol = 1;
        state.eightPuzzle[0][0] = 1;
        state.eightPuzzle[0][1] = 2;
        state.eightPuzzle[0][2] = 3;
        state.eightPuzzle[1][0] = 8;
        state.eightPuzzle[1][1] = 0;
        state.eightPuzzle[1][2] = 4;
        state.eightPuzzle[2][0] = 7;
        state.eightPuzzle[2][1] = 6;
        state.eightPuzzle[2][2] = 5;
    State goal;
        goal.emptyRow = 1;
        goal.emptyCol = 0;
        goal.eightPuzzle[0][0] = 2;
        goal.eightPuzzle[0][1] = 8;
        goal.eightPuzzle[0][2] = 1;
        goal.eightPuzzle[1][0] = 0;
        goal.eightPuzzle[1][1] = 4;
        goal.eightPuzzle[1][2] = 3;
        goal.eightPuzzle[2][0] = 7;
        goal.eightPuzzle[2][1] = 6;
        goal.eightPuzzle[2][2] = 5;
    Node* p = A_Star(state, goal);
    print_WayToGetGoal(p);
    return 0;
}