#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node* left;
    struct node* right;
    int ht;
};

struct node* root = NULL;

// function prototyping
struct node* create(int);
struct node* insert(struct node*, int);
struct node* rotate_left(struct node*);
struct node* rotate_right(struct node*);
int balance_factor(struct node*);
int height(struct node*);
void inorder(struct node*);
void preorder(struct node*);
void postorder(struct node*);
 
// creates a new tree node
struct node* create(int data)
{
    struct node* new_node = (struct node*) malloc (sizeof(struct node));
 
    // if a memory error has occurred
    if (new_node == NULL)
    {
        printf("\nMemory can't be allocated\n");
        return NULL;
    }
    new_node->data = data;
    new_node->left = NULL;
    new_node->right = NULL;
    return new_node;
}

// rotates to the left
struct node* rotate_left(struct node* root)
{
    struct node* right_child = root->right;
    root->right = right_child->left;
    right_child->left = root;
 
    // update the heights of the nodes
    root->ht = height(root);
    right_child->ht = height(right_child);
 
    // return the new node after rotation
    return right_child;
}
 
// rotates to the right
struct node* rotate_right(struct node* root)
{
    struct node* left_child = root->left;
    root->left = left_child->right;
    left_child->right = root;
 
    // update the heights of the nodes
    root->ht = height(root);
    left_child->ht = height(left_child);
 
    // return the new node after rotation
    return left_child;
}

// calculates the balance factor of a node
int balance_factor(struct node* root)
{
    int lh, rh;
    if (root == NULL)
        return 0;
    if (root->left == NULL)
        lh = 0;
    else
        lh = 1 + root->left->ht;
    if (root->right == NULL)
        rh = 0;
    else
        rh = 1 + root->right->ht;
    return lh - rh;
}
 
// calculate the height of the node
int height(struct node* root)
{
    int lh, rh;
    if (root == NULL)
    {
        return 0;
    }
    if (root->left == NULL)
        lh = 0;
    else
        lh = 1 + root->left->ht;
    if (root->right == NULL)
        rh = 0;
    else
        rh = 1 + root->right->ht;
 
    if (lh > rh)
        return (lh);
    return (rh);
}
 
// inserts a new node in the AVL tree
struct node* insert(struct node* root, int data)
{
    if (root == NULL)
    {
        struct node* new_node = create(data);
        if (new_node == NULL)
        {
            return NULL;
        }
        root = new_node;
    }
    else if (data > root->data)
    {
        // insert the new node to the right
        root->right = insert(root->right, data);
 
        // tree is unbalanced, then rotate it
        if (balance_factor(root) == -2)
        {
            if (data > root->right->data)
            {
                root = rotate_left(root);
            }
            else
            {
                root->right = rotate_right(root->right);
                root = rotate_left(root);
            }
        }
    }
    else
    {
        // insert the new node to the left
        root->left = insert(root->left, data);
 
        // tree is unbalanced, then rotate it
        if (balance_factor(root) == 2)
        {
            if (data < root->left->data)
            {
                root = rotate_right(root);
            }
            else
            {
                root->left = rotate_left(root->left);
                root = rotate_right(root);
            }
        }
    }
    // update the heights of the nodes
    root->ht= height(root);
    return root;
}
void postOrder(struct node* root)
{
    if (root != NULL) {
        postOrder(root->left);
        postOrder(root->right);
        printf(" %d ", root->data);
    }
}
 
void inOrder(struct node* root)
{
    if (root != NULL) {
        inOrder(root->left);
        printf(" %d ", root->data);
        inOrder(root->right);
    }
}
 
void preOrder(struct node* root)
{
    if (root != NULL) {
        printf(" %d ", root->data);
        preOrder(root->left);
        preOrder(root->right);
    }
}




























int main()
{

	root=insert(root,21);
	root=insert(root,26);
	root=insert(root,30);
	root=insert(root,9);
	root=insert(root,4);
	root=insert(root,14);
	root=insert(root,28);
	root=insert(root,18);
	root=insert(root,15);
	root=insert(root,10);

	printf("\nPost-order traversal\n");
	postOrder(root);
	
	printf("\nPre-order traversal\n");
	preOrder(root);
	
	printf("\nIn-order traversal\n");
	inOrder(root);
	return 0;
}
