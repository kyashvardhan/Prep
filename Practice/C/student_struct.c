#include <stdio.h>

typedef struct {
    int id;
    char name[50];
    float grade;
} Student;

int main() {
    Student s1;
    
    printf("Enter student ID: ");
    scanf("%d", &s1.id);
    printf("Enter student name: ");
    scanf(" %[^\n]", s1.name); // Read string with spaces
    printf("Enter student grade: ");
    scanf("%f", &s1.grade);
    
    printf("\nStudent Details:\n");
    printf("ID: %d\n", s1.id);
    printf("Name: %s\n", s1.name);
    printf("Grade: %.2f\n", s1.grade);
    
    return 0;
}
