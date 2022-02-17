#include <stdio.h>

#define NB_ROWS 4
#define NB_COLUMNS 4
#define MAX_LENGTH NB_ROWS*NB_COLUMNS
#define EMPTY 0
#define MAX_cells 4
#define INF 999


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
    int data[MAX_cells];
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
//mot o trong kenkenchuyen thanh mot dinh trong do thi rang buoc
int indexOf(Coord coord) {
    return NB_ROWS*coord.x + coord.y;
}

//tim toa do khi biet chi so dinh
//mot dinh trong do thi rang buoc chuyen thanh mot o trong kenken
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

//danh sach cac rang buoc cua mot dinh
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

//cau truc khung trong kenken
typedef struct {
    Coord fr[MAX_LENGTH];
    int size_f; 
    int result;
    char opt;
}Frame;

//kenken
typedef struct {
    Frame ken[MAX_LENGTH]; //kenken co n khung
    int size_k;
    int cells[NB_ROWS][NB_COLUMNS];
    Constrains constrains;
}Kenken;

//khoi tao bang kenken voi gia tri trong file .txt
void init_Kenken(Kenken* kenken) {
    freopen("kenken.txt", "r", stdin);
    scanf("%d", &kenken->size_k);
    int i, j, t;
    for(t = 0; t<kenken->size_k; t++) {
        scanf("%d%c%d", &kenken->ken[t].result, &kenken->ken[t].opt, &kenken->ken[t].size_f);
        for(i = 0; i<kenken->ken[t].size_f; i++)
            scanf("%d%d", &kenken->ken[t].fr[i].x, &kenken->ken[t].fr[i].y);
        scanf("\n");
    }
    for (i = 0; i<NB_ROWS; i++)
		for (j = 0; j<NB_COLUMNS; j++)
			kenken->cells[i][j] = EMPTY;
    init_Constrains(&kenken->constrains);
}

void printKenken(Kenken kenken){
	int i, j, l, p;
	printf("KenKen:\n");
	for (i = 0;i < NB_ROWS;i++){
		for (j = 0; j<NB_COLUMNS; j++)
			printf("------");
		printf("-\n");
		for (j = 0; j<NB_COLUMNS; j++){
			int flag = 0;
			for (l = 0; l<kenken.size_k; l++){
				for (p = 0; p<kenken.ken[l].size_f; p++)
					if (kenken.ken[l].fr[p].x == i && kenken.ken[l].fr[p].y == j){
						flag = 1;
						break;		
					}
				if (flag)
					break;
			}
			if (flag)
				printf("|%2d%c  ", kenken.ken[l].result, kenken.ken[l].opt);
			else 
				printf("|     ");
		}
		printf("|\n");
		for (j = 0; j<NB_COLUMNS; j++){
			printf("|  ");
			if (kenken.cells[i][j] != 0)
				printf("%d  ", kenken.cells[i][j]);
			else
				printf("   ");
		}
		printf("|\n");
		for (j = 0; j<NB_COLUMNS; j++){
			printf("|     ");
		}
		printf("|\n");
	}
	for (j = 0; j<NB_COLUMNS; j++)
		printf("------");
	printf("-\n");
}

//kiem tra trang thai ket thuc
int isFilled_Kenken(Kenken Kenken) {
    int i, j;
    for(i = 0; i<NB_ROWS; i++) 
        for(j = 0; j<NB_COLUMNS; j++) {
            if (Kenken.cells[i][j] == 0)
                    return 0;
        }
    return 1;
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
}

Coord getInfoFrame(Coord position, Kenken Kenken){
    int i, j;
    for(i = 0; i<Kenken.size_k; i++)
        for(j = 0; j<Kenken.ken[i].size_f; j++)
            if(position.x == Kenken.ken[i].fr[j].x && position.y == Kenken.ken[i].fr[j].y){
                Coord info = {i, j};
                return info;
            }
}

//tim mien gia tri cua o trong
List get_Availablecellss(Coord position, Kenken Kenken) {
    Coord info = getInfoFrame(position, Kenken);
    if(Kenken.ken[info.x].size_f == 1) {
        List result;
        init_List(&result);
        append_List(&result, Kenken.ken[info.x].result);
        return result;
    }

    ListCoord posList = get_Constrains(Kenken.constrains, position);
    int availables[MAX_cells+1]; // 0>0 array, just use 1>0
    int i;
    for(i = 1; i<=MAX_cells; i++)
        availables[i] = 1;
    for(i = 0; i<posList.size; i++) {
        Coord pos = posList.data[i];
        if(Kenken.cells[pos.x][pos.y] != EMPTY) { //dang mang gia tri
            availables[Kenken.cells[pos.x][pos.y]] = 0;
        }
    }
    List result;
    init_List(&result);
    if(result.size == 0)
        for(i = 1; i<=MAX_cells; i++) 
            if (availables[i])
                append_List(&result, i);
    return result;
}

//cach 2 uu tien o co mien gia tri it nhat
Coord get_NextMinDomainCell(Kenken Kenken) {
    int minLength = INF;
    int i, j;
    Coord result;
    for(i = 0; i < NB_ROWS; i++) {
        for(j = 0; j < NB_COLUMNS; j++) {
            if(Kenken.cells[i][j] == EMPTY) {
                Coord pos = {i, j};
                int availableLength = get_Availablecellss(pos, Kenken).size;
                if( availableLength < minLength) {
                    minLength = availableLength;
                    result = pos;
                }
            }
        }
    }
    return result;
}

int min(int a, int b){
	return a < b ? a : b;
}

int max(int a, int b){
	return a > b ? a : b;
}

int checkResFrame(Kenken kenken, Coord pos){
	Coord info = getInfoFrame(pos, kenken);
	if (kenken.ken[info.x].opt == '+'){
		int i, sum = 0, cnt = 0;
		for (i = 0; i<kenken.ken[info.x].size_f; i++)
			if (kenken.cells[kenken.ken[info.x].fr[i].x][kenken.ken[info.x].fr[i].y] > 0){
				cnt++;
				sum += kenken.cells[kenken.ken[info.x].fr[i].x][kenken.ken[info.x].fr[i].y];
			}
		if (cnt == kenken.ken[info.x].size_f)
			return sum == kenken.ken[info.x].result;
	}
	else if (kenken.ken[info.x].opt == '*'){
		int i, tich = 1, cnt = 0;
		for (i = 0; i<kenken.ken[info.x].size_f; i++)
			if (kenken.cells[kenken.ken[info.x].fr[i].x][kenken.ken[info.x].fr[i].y] > 0){
				cnt++;
				tich *= kenken.cells[kenken.ken[info.x].fr[i].x][kenken.ken[info.x].fr[i].y];
			}
		if (cnt == kenken.ken[info.x].size_f)
			return tich == kenken.ken[info.x].result;
	}
	else if (kenken.ken[info.x].opt == '-'){
		int i, cnt = 0, mi = INF, ma = 0;
		for (i = 0; i<kenken.ken[info.x].size_f; i++)
			if (kenken.cells[kenken.ken[info.x].fr[i].x][kenken.ken[info.x].fr[i].y] > 0){
				cnt++;
				mi = min(mi, kenken.cells[kenken.ken[info.x].fr[i].x][kenken.ken[info.x].fr[i].y]);
				ma = max(ma, kenken.cells[kenken.ken[info.x].fr[i].x][kenken.ken[info.x].fr[i].y]);
			}
		if (cnt == 2){
			return (ma - mi == kenken.ken[info.x].result);
		}
	}
	else if (kenken.ken[info.x].opt == '/'){
		int i, cnt = 0, mi = INF, ma = 0;
		for (i = 0; i<kenken.ken[info.x].size_f; i++)
			if (kenken.cells[kenken.ken[info.x].fr[i].x][kenken.ken[info.x].fr[i].y] > 0){
				cnt++;
				mi = min(mi, kenken.cells[kenken.ken[info.x].fr[i].x][kenken.ken[info.x].fr[i].y]);
				ma = max(ma, kenken.cells[kenken.ken[info.x].fr[i].x][kenken.ken[info.x].fr[i].y]);
			}
		if (cnt == 2)
			return (ma % mi == 0 && ma / mi == kenken.ken[info.x].result);
	}
}

//thuat toan
int exploreCounter = 0;

int Kenken_BackTracking(Kenken *kenken) {
    if(isFilled_Kenken(*kenken))
        return 1;
    Coord position = get_NextMinDomainCell(*kenken);
    List availables = get_Availablecellss(position, *kenken);
    if(availables.size == 0) {
        return 0;
    }
    int j;
    for(j = 0; j<availables.size; j++) {
        int cells = availables.data[j];
        kenken->cells[position.x][position.y] = cells;
        exploreCounter++;
        if (!checkResFrame(*kenken, position)){
			kenken->cells[position.x][position.y] = EMPTY;
			continue;
		}
        if(Kenken_BackTracking(kenken))
            return 1;
        kenken->cells[position.x][position.y] = EMPTY;
    }
    return 0;
}

//lan truyen rang buoc tu de bai cho truoc va ket thuc bai toan
Kenken solveKenken(Kenken kenken) {
    int i, j;
    init_Constrains(&kenken.constrains);
    for(i = 0; i<NB_ROWS; i++) {
        for(j = 0; j<NB_COLUMNS; j++) {
            ListCoord history;
            init_ListCoord(&history);
            Coord pos = {i, j};
            spread_ConstrainsFrom(pos, &kenken.constrains, &history);
        }
    }
    exploreCounter = 0;
    if(Kenken_BackTracking(&kenken))
        printf("Solve\n");
    else 
        printf("Can not solve\n");
    printf("Explore %d Kenkens\n", exploreCounter);
    return kenken;
}
/* 8  
2/ 2 0 0 0 1
7+ 2 0 2 1 2
4  1 0 3
1- 2 1 0 2 0
3- 2 1 1 2 1
1- 2 3 0 3 1
4* 3 2 2 3 2 3 3
2- 2 1 3 2 3
dong dau la so khung-frame
cac dong tiep theo
ket qua phep toan - phep toan - so o trong khung - toa do cua cac o
*/
int main() {
    Kenken kenken;
    init_Kenken(&kenken);
    printKenken(kenken);
    Kenken result = solveKenken(kenken);
    printKenken(result);
    return 0;
}