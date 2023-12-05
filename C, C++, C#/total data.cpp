/*
void insertionSort(int D[], int n)
{
   int i, k, key;
   for (i = 1; i < n; i++)
   { 
      key = D[i];
      
      for (k = i-1; k>=0 && key <= D[k]; k--)
         D[k+1] = D[k];   // shift operation
      D[k+1] = key;  // insert key
   }
}
*/

/*
void selectionSort(int D[], int n) {
   int i, index, j, min;
   for (i = 0; i < (n-1); i++) {
      min = D[n-1];
      index = n-1;
      for (j = i; j < (n-1); j++){
         if (D[j] < min){
            min = D[j];
            index = j;
         }
      }
      if (i != index){
         D[index] = D[i];
         D[i] = min;
      }
   }
}
*/

/*
void bubleSort(int D[], int n)
{
   int temp, k, move; 
         
   for (move = 0; move < (n-1); move++){
   
      for (k = 0; k < (n-1-move); k++){
         if (D[k] > D[k+1]){ //exchange the values
            temp = D[k];
            D[k] = D[k+1];
            D[k+1] = temp; 
         }
      }
   }
}
*/

/*
void mergesort(int D[], int left, int right) {
   int k;   
   if (left < right) {
      k = (left + right)/2; 	// index of midpoint
      mergesort(D, left, k);
      mergesort(D, k+1, right);

      // merge the two halves
      merge(D, left, k, right);
   }
}
const int MAX_SIZE = maximum-number-of-items-in-array;

void merge(int D[], int left, int k, int right) {
   int i, j, l = 0;
   int M[MAX_SIZE]; 	// temporary array

   for (i=left, j=k+1; (i <= k) && (j <= right); ) {
      if (D[i] < D[j]) {  
         M[l] = D[i];
         i++;
         l++;
      }
      else {  
          M[l] = D[j];
          j++;
          l++
      }
   }
   // copy the remaining elements to M
   while (i <= k){
      M[l] = D[i];
      i++;
      l++;
   }
   while (j <= right){
      M[l] = D[j];
      j++;
      l++;
   }
   // copy M to D
   for (i = left, l = 0; i <= right; i++, l++)
      D[i] = M[l];
} 
*/

/*
void quicksort(int D[], int left, int right) {
   
int k, j, q, temp;

   //partition the array into two parts
   k = left;
   j = right;

   q = D[(left+right)/2];   //pivot

   do{
      while ((D[k] < q) && (k < right))
         k++;
      while ((D[j] > q) && (j > left))
         j--;
      if (k <= j) { //exchange D[k] & D[j]
         temp = D[k];
         D[k] = D[j];
         D[j] = temp;
         k++;    j--;
      }
   }while(k <= j); 
   
// Sort each part using quicksort
   if (left < j)
      quicksort(D, left, j);
   if (k < right)
      quicksort(D, k, right);
 }
*/

/*
// Index of the left child of node i

int left(int i){
   return(2*i+1);
}

// Index of the right child of node i

int right(int i){
   return(2*i+2);
}
// Heap size is a global variable
int heap_size;   // index of the last element

void heapify(int D[], int i){
   int left_child, right_child, max, temp;
   left_child = left(i);
   right_child = right(i);
   // find the max of nodes left, right, and i
   if ((left_child <= heap_size) &&
       (D[left_child] > D[i]))
      max = left_child;
   else
      max = i;
   if ((right_child <= heap_size) &&
       (D[right_child] > D[max]))
         max = right_child;

// if max is not the i th node, exchange

   if (max != i){
      temp = D[max];
      D[max]= D[i];
      D[i] = temp;
      heapify(D, max);
   }
} 
void build_heap(int D[], int n){
int i;
heap_size = n-1;

for (i = (n-1)/2; i >= 0; i--)
   heapify(D,i);
}
void heapsort(int D[], int n){
   int i, temp;
   build_heap(D,n);
   for (i = n-1; i >= 1; i--){
   // exchange the root with the ith element
      temp = D[i];
      D[i] = D[0];
      D[0] = temp;
      heap_size--;
      heapify(D,0);
   }
}
*/

/*
int sequentialSearch(int D[], int key, int n){
   int i;
	for (i = 0; i < n; i++){
      if (D[i]== key)
		    return i;
   }
	return -1;
}

// Secondary key sequential search
int secondaryKeySearch(STUDENT D[],
                       int N, 
                       int Result[],
                       char *key){
   int i=0, k;
   for (k=0; k<N; k++){
      if (strcmp(D[k].surname,key)==0){
         // found, insert into Result array
         Result[i]=k;
         i++;
      }
   }
   return i;
}
*/

/*
int binarySearch(int D[], int N, int key) {
   int left =0;
   int right = N –1;
   int middle; 	 

   while (left <= right) {
 	   middle = (left + right)/2;
	   if (key == D[middle])
         return middle;
     else if (key > D[middle]) 
        left = middle + 1;
	   else 
		   right  = middle – 1; 
   }
   return –1;
}
*/

/*
int hash(char *key, int tableSize)
{
	int hasVal = 0; 
	int i;
	for (i = 0; key[i]!=‘\0’; i++)
		hashVal += key[i]; 
	return hashVal % tableSize; 
}

// hashfunction 2 
int hash (char *key, int tableSize)
{
	return (key[0]+27 * key[1] + 729*key[2]) % tableSize; 	
}

// hashfunction 3
int hash (char *key, int tableSize)
{
   int hashVal = 0; 
   int i;	
   for (i = 0; key[i] != ‘\0’; i++)
	hashVal = hashVal + key[i] * pow(37,i); 
   hashVal = hashVal % tableSize; 
   if (hashVal < 0)   // in case overflows occurs 
	hashVal += tableSize; 
   return hashVal; 		
};
*/

/*
//quadratic probing
#define TableSize 997;   // a prime number
typedef struct s{
   char id[11];
   char name[20];
   float gano;
}STUDENT;

STUDENT H[TableSize];  // Global Hash Table

void initializeHashTable(){
   int i;
   for (i=0; i<TableSize; i++)
      strcpy(H[i].id,"");
} 
*/

/*
// hash function
int hashFunction(char *key, int size){
   int i,j,k,result;
   // 48 is ASCII code of 0
   i = key[10]-48;   //last digit
   j = key[9]-48;  // 2nd digit from last
   k = key[6]-48; // 5th digit from last
   
   result = (k*100 + j*10 + i) % size;

   return result;
}

//insertion function
void insert(STUDENT r){
   int c,i,p,q;
   p=hashFunction(r.id,TableSize);
   c=0;
   i=1;  q = p;
   while ((strcmp(H[p].id,"")!=0) &&
          (strcmp(H[p].id,r.id)!=0) &&
          (c <= TableSize/2)){
      c++;
      p = q + i * i; 
      i++;
      if (p > TableSize-1)
         p = p % TableSize;
   }
   //if empty position is found, insert r
   if (strcmp(H[p].id,"")==0){
      strcpy(H[p].id, r.id);
      strcpy(H[p].name, r.name);
      H[p].gano = r.gano;
   }
   else if (strcmp(H[p].id, r.id)==0)
      printf("Error, the same student cannot
             appear twice\n");
   else 
      printf("Overflow, counter has reached its
             limit\n");
}   
*/

/*
//implementation of linked list using arrays
typedef struct linkedList{
   char data[5];
   int next;
}SIMPLE_LIST;

//This list has at most 100 elements
SIMPLE_LIST L[100]; 
int first = -1; //Index of the first element
int last = -1; //Index of the last element

//using Pointers
typedef struct linkedList{
   char data[5];
   struct linkedList *next;
}SIMPLE_LIST;

//This list has any number of elements
//Pointers to the first and last elements
// Initially, the list is empty
SIMPLE_LIST *first = NULL; 
SIMPLE_LIST *last = NULL; 

//definition of the list
typedef struct linkedList{
   int info;   
   char message[100];
   struct linkedList *next;
}SIMPLE_LIST;

// Initially, the list is empty
SIMPLE_LIST *first = NULL; 
SIMPLE_LIST *last = NULL; 

// insertion function
int insert(SIMPLE_LIST *p){
   if (first != NULL){
      last->next = p;
      p->next = NULL;
      last = p;
   }
   else {
      first = p;
      last = p;
      p->next = NULL;
   }
   return 0;
}

// traversing a linked list
int displayList(){
   SIMPLE_LIST *p
   p = first;
   if (p == NULL){
      printf("List is empty\n");
      return -1;
   }
   while (p != NULL){
      printf(" %d %s \n", 
              p->info, p->message );
      p = p->next; 
   }
   return 0;
}

//searching in linked list(sequential)
SIMPLE_LIST *search(int key){
   SIMPLE_LIST *p;
 
   p = first;
   while (p){
      if (p->info == key)
         return p;
      p = p->next;
   }
   return NULL;
}

//deletion function
SIMPLE_LIST *delete(int key){
   SIMPLE_LIST *p, *previous;
   p = first;
   previous = NULL;

// search for the element to be deleted
   
   while (p){
      if (key == p->info)
         break;
      previous=p;
      p=p->next;
   }
   if (p != NULL){ //if found
      if (previous == NULL){  
      // if first element will be deleted
         if (first == last){
         // if list has one element
            first = NULL;
            last = NULL;
         }
         else {
             first = first->next;
         }
      else{
         //delete from middle or last
         previous->next = p->next;
         if (previous->next == NULL){
            //last element is deleted
            last = previous;
         }
      }
      free(p);
      return(p);
   }
   else     //not found
      return NULL;
}
*/

/*
//doubly linked lists
//definition of the list
typedef struct doubly_list{
   int info;
   char message[100];
   struct doubly_list *previous;
   struct doubly_list *next;
}DLIST;
DLIST *first = NULL;
DLIST *last = NULL;

//insertion function
int insert(DLIST *p){
   if (first != NULL){  // if list is not empty
      last->next = p;
      p->previous = last;
      p->next = NULL;
      last = p;
   }
   else {   // if list is empty
      first = p;
      last = p;
      first->previous = NULL;
      last->next = NULL;
   }
   return 0;
}

//display function
int display(){
   DLIST *p;
   p = first;
   if (p == NULL){
      printf("List is empty\n");
      return -1;
   }
   while (p){
      printf("%d %s\n", p->info, p->message);
      p = p->next;
   }
   return 0;
}

// search element from the list
DLIST *search(int key){
   DLIST *p;
   p = first;
   while (p){
      if (key == p->info)
         return p;
      p = p->next;
   }
   return NULL;
}

//Deletion function
DLIST *delete(int key){
   DLIST *p;
   p = search(key);
   if (p==NULL){
      printf("The element to be deleted is not 
              in the list\n");
      return NULL;
   }
   if (p == first){  //Delete the first element
      if (first == last){  // list has 1 element
         first = NULL;
         last = NULL;
      }
      else {  // list has more than one element
         first = p->next;
         first->previous = NULL;
      }
   }
   else{
      if (p == last){   //Delete from last
         last = p->previous;
         last->next = NULL;
      }
      else { //Delete from middle
         p->previous->next = p->next;
         p->next->previous = p->previous;
      }
   }
   free(p);
   return p;
}

// saving a list in a file 
int store(){
   FILE *fp;
   DLIST *p;
   // open the file
   if ((fp=fopen("list.txt","w"))==NULL){
      printf("File cannot be opened, disk is full\n");
      return -1;
   }
   p = first;
   while (p){
      fwrite(p, sizeof(DLIST)-2*sizeof(p), 1, fp);
      p = p->next;
   }
   printf("List was stored\n");
   fclose(fp);
   return 0;
}
