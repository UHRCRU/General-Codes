// C program for Quick Sort
#include <stdio.h>
#include <stdlib.h>
 

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
// function to find the partition position
int Partition(int arr[], int lb, int ub)
{
	// select the leftmost element as pivot
	int Pivot=arr[lb];
	int start=lb;
	int end=ub;
	// traverse each element of the array
    // compare them with the pivot
	while(start<end)
	{
		while(arr[start]<=Pivot)
		{
			start++;
		}
		while(arr[end]>Pivot)
		{
			end--;
		}
		if(start<end)
		{
			swap(&arr[start],&arr[end]);
		}
	}
	swap(&arr[lb],&arr[end]);
	 // return the partition point
	return end;
}
void quickSort(int arr[], int lb, int ub)
{
	if(lb<ub)
	{
	// find the pivot element such that
    // elements smaller than pivot are on left of pivot
    // elements greater than pivot are on right of pivot
		int loc= Partition(arr, lb, ub);
		// recursive call on the left of pivot
		quickSort(arr,lb,loc-1);
		// recursive call on the right of pivot
		quickSort(arr,loc+1,ub);
	}
}
 
// Function to print an array
void printArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}
 
// Driver code
int main()
{
    int arr[] = { 7, 6, 10, 5, 9, 2, 1, 15, 4 };
    int arr_size = sizeof(arr) / sizeof(arr[0]);
 
    printf("Given array is \n");
    printArray(arr, arr_size);
 
    quickSort(arr, 0, arr_size - 1);
 
    printf("\nSorted array is \n");
    printArray(arr, arr_size);
    return 0;
}
