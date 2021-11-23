#include <stdio.h>
#include <math.h>

#define NB_ROWS 4
#define NB_COLUMNS 4
#define MAX_LENGTH NB_ROWS*NB_COLUMNS
#define EMPTY 0
#define INF 999999
#define MAX_VALUE 4
// x va y co gia tri tu 0 den 7
typedef struct {
    int x, y;
}Coord;

typedef struct {
    Coord data[MAX_LENGTH];
    int size;
}ListCoord;

//tao listcord rong
void init_ListCoord(ListCoord *list) {
    list->size = 0;
}

//them coord vao listcoord
void append_ListCoord(ListCoord *list, Coord coord) {
    list->data[list->size++] = coord;
}

typedef struct {
    int data[MAX_VALUE];
    int size;
}List;

//tao danh sach rong
void init_List(List *list) {
    list->size = 0;
}

//them phan tu vao danh sach
void append_List(List *list, int n) {
    list->data[list->size++] = n;
}

//cau truc Constrain
typedef struct {
    int data[NB_ROWS*NB_COLUMNS][NB_ROWS*NB_COLUMNS];
    int n;
}Constrains;

//khoi tao rang buoc rong
void init_Constrains(Constrains* constrains) {
    int i, j;
    for(i = 0; i<NB_ROWS*NB_COLUMNS; i++)
        for(j = 0; j<NB_ROWS*NB_COLUMNS; j++)
            constrains->data[i][j] = 0;
    constrains->n = NB_ROWS*NB_COLUMNS;
}

//tim chi so dinh khi biet toa do
//mot o trong Chess chuyen thanh mot dinh trong do thi rang buoc
int indexOf(Coord coord) {
    return NB_ROWS*coord.x + coord.y;
}

//tim toa do khi biet chi so dinh
//mot dinh trong do thi rang buoc chuyen thanh mot o trong Chess
Coord positionOf_Vertex(int vertex) {
    Coord coord;
    coord.x = vertex / NB_ROWS;
    coord.y = vertex % NB_COLUMNS;
    return coord;
}

//them rang buoc
int add_Constrain(Constrains* constrains, Coord soure, Coord target) {
    int u = indexOf(soure);
    int v = indexOf(target);
    if(constrains->data[u][v] == 0) {
        constrains->data[u][v] = 1;
        constrains->data[v][u] = 1;
        return 1;
    }
    return 0;
}

//tao rang buoc mot dinh
ListCoord get_Constrains(Constrains constrains, Coord coord) {
    int i;
    int v = indexOf(coord);
    ListCoord result;
    init_ListCoord(&result);
    for(i = 0; i<constrains.n; i++) {
        if(constrains.data[v][i] == 1) {
            append_ListCoord(&result, positionOf_Vertex(i));
        }
    }
    return result;
}

//contrains
void clear_Constrains(Constrains *contrains) {
    contrains = 0;
}

typedef struct {
    int cells[NB_ROWS][NB_COLUMNS];
    Constrains constrains;
}Chess;

//khoi tao bang Chess rong
void init_Chess(Chess* chess) {
    int i, j;
    for(i = 0; i<NB_ROWS; i++) 
        for(j = 0; j<NB_COLUMNS; j++) {
            chess->cells[i][j] = EMPTY;
        }
    init_Constrains(&chess->constrains);
}

//khoi tao bang Chess co gia tri
void init_Chess_WithValues(Chess* chess, int inputs[NB_ROWS][NB_COLUMNS]) {
    int i, j;
    for(i = 0; i<NB_ROWS; i++) 
        for(j = 0; j<NB_COLUMNS; j++) {
            chess->cells[i][j] = inputs[i][j];
        }
    init_Constrains(&chess->constrains);
}

//in bang Chess
void printChess(Chess chess) {
    int i, j;
    printf("Chess:\n");
    for(i = 0; i<NB_ROWS; i++){
        for(j = 0; j<NB_COLUMNS; j++)
            printf(" %2d ", chess.cells[i][j]);
        printf("\n");
    }
    printf("------------------------\n");
}

//kiem tra trang thai ket thuc
int isFilled_Chess(Chess chess) {
    int i, j;
    int count = 0;
    for(i = 0; i<NB_ROWS; i++) 
        for(j = 0; j<NB_COLUMNS; j++) {
            if (chess.cells[i][j] != EMPTY)
                count++;
        }
    return count == NB_ROWS;
}
//tao rang buoc tu vi tri cho truoc
void spread_ConstrainsFrom(Coord position, Constrains* constrains, ListCoord* changeds) {
    int row = position.x, column = position.y;
    int i, j;
    //tao rang buoc theo cot
    for(i = 0; i<NB_ROWS; i++) {
        if(i != row) {
            Coord pos = {i, column};
            if(add_Constrain(constrains, position, pos))
                append_ListCoord(changeds, pos);
        }
    }
    //tao rang buoc theo hang
    for(i = 0; i<NB_COLUMNS; i++) {
        if(i != column) {
            Coord pos = {row, i};
            if(add_Constrain(constrains, position, pos))
                append_ListCoord(changeds, pos);
        }
     }
    //rang buoc theo duong cheo
    for(i = 0; i<NB_ROWS; i++)
        for(j = 0; j<NB_COLUMNS; j++) {
            if(i != row && j != column && abs(row-i) == abs(column-j)) {
                Coord pos = {i, j};
                if(add_Constrain(constrains, position, pos))
                    append_ListCoord(changeds, pos);
            }
        }
}

//tim mien gia tri cua o trong
List get_AvailableValues2(Coord position, Chess chess) {
    ListCoord posList = get_Constrains(chess.constrains, position);
    int availables[MAX_VALUE+1]; 
    int i;
    for(i = 1; i<=MAX_VALUE; i++)
        availables[i] = 1;
    for(i = 0; i<posList.size; i++) {
        Coord pos = posList.data[i];
        if(chess.cells[pos.x][pos.y] != EMPTY) { //dang mang gia tri
            availables[chess.cells[pos.x][pos.y]] = 0;
        }
    }
    List result;
    init_List(&result);
    for(i = 1; i<=MAX_VALUE; i++) {
        if(availables[i])
            append_List(&result, i);
    }
    return result;
}
//
Coord get_NextEmptyCell(Chess chess) {
    int i ,j;
    for(i = 0; i<NB_ROWS; i++) {
        for(j = 0; j<NB_COLUMNS; j++) {
            Coord pos = {i, j};
            if(chess.cells[i][j] == EMPTY)
                return pos;  
        }
    } 
}

int exploreCounter = 0;
int Chess_BackTracking2(Chess* chess) {
    if(isFilled_Chess(*chess))
         return 1;
    Coord position = get_NextEmptyCell(*chess);
    List availables = get_AvailableValues2(position, *chess);
    if(availables.size==0)
        return 0;
    int j;
    for(j = 0; j<availables.size; j++){
        int value = availables.data[j];
        chess->cells[position.x][position.y] = value;
        exploreCounter++;
        if(Chess_BackTracking2(chess))
            return 1; 
        chess->cells[position.x][position.y] = EMPTY;
    }  
    return 0;
}




int getAvailableValues(Coord position, Chess state){
	ListCoord posList = get_Constrains(state.constrains, position);
	int k;
	for (k = 0;k < posList.size; k++)
		if (state.cells[posList.data[k].x][posList.data[k].y] != EMPTY)
			return 0;
	int availables[MAX_VALUE+1];
	int i, j;
	for(i = 1; i<=MAX_VALUE; i++)
		availables[i] = 1;
	for(i = 0; i<NB_ROWS; i++)
		for (j = 0;j < NB_COLUMNS;j++)
			if (state.cells[i][j] != EMPTY)
				availables[state.cells[i][j]] = 0;
	
	for(i = 1;i <= MAX_VALUE;i++)
		if (availables[i])
			return i;
}

ListCoord getAvailabeCells(Chess state){
	int i, j;
	ListCoord result;
	init_ListCoord(&result);
	for(i = 0; i<NB_ROWS; i++)
		for(j = 0; j<NB_COLUMNS; j++)
			if(state.cells[i][j] == EMPTY){
				Coord pos = {i, j};
				ListCoord posList = get_Constrains(state.constrains, pos);
				int k, flag = 0;
				for (k = 0;k < posList.size;k++)
					if (state.cells[posList.data[k].x][posList.data[k].y] != EMPTY)
						flag = 1;
				if(flag)
					continue;
				append_ListCoord(&result, pos);
			}
	return result;
}

//thuat toan
//int exploreCounter = 0;

int Chess_BackTracking(Chess *state){
	if(isFilled_Chess(*state))
		return 1;
	ListCoord position = getAvailabeCells(*state);
	if (position.size == 0)
		return 0;
	int i, j;
	for (i = 0;i < position.size;i++){
		int value = getAvailableValues(position.data[i], *state);
		state->cells[position.data[i].x][position.data[i].y] = value;
		exploreCounter++;
		if (Chess_BackTracking(state))
			return 1;
		state->cells[position.data[i].x][position.data[i].y] = EMPTY;
	}
	return 0;
}

//lan truyen rang buoc tu de bai cho truoc va ket thuc bai toan
Chess solveChess(Chess chess) {
    int i, j;
    init_Constrains(&chess.constrains);
    for(i = 0; i<NB_ROWS; i++) {
        for(j = 0; j<NB_COLUMNS; j++) {
            ListCoord history;
            init_ListCoord(&history);
            Coord pos = {i, j};
            spread_ConstrainsFrom(pos, &chess.constrains, &history);
        }
    }
    exploreCounter = 0;
    if(Chess_BackTracking(&chess))
        printf("Solve\n");
    else 
        printf("Can not solve\n");
    printf("Explore %d states\n", exploreCounter);
    return chess;
}

int main() {
    Chess chess;
    init_Chess(&chess);
    printChess(chess);
    Chess result = solveChess(chess);
    printChess(result);
}