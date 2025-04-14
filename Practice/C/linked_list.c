#include <stdio.h>
#include <stdlib.h>

// Define the Node structure.
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Create a new node.
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (!newNode) {
        printf("Memory error!\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Insert node at the beginning of the list.
void insertAtHead(Node** head, int data) {
    Node* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}

// Print the linked list.
void printList(Node* head) {
    Node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    Node* head = NULL;
    insertAtHead(&head, 10);
    insertAtHead(&head, 20);
    insertAtHead(&head, 30);
    insertAtHead(&head, 40);
    
    printf("Linked List: ");
    printList(head);
    
    // Free memory (optional in small programs)
    Node* current = head;
    Node* temp = NULL;
    while(current != NULL) {
        temp = current;
        current = current->next;
        free(temp);
    }
    
    return 0;
}
