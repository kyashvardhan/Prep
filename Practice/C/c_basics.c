#include <stdio.h>
#include <string.h>

// Function declaration
int add(int a, int b);

// Structure declaration
struct Student {
    char name[50];
    int age;
    float marks;
};

int main() {
    // 1. Variables and Data Types
    int x = 10, y = 20;
    float pi = 3.14;
    char grade = 'A';

    printf("🔢 Basic Variables:\n");
    printf("x = %d, y = %d, pi = %.2f, grade = %c\n\n", x, y, pi, grade);

    // 2. Input/Output
    int input;
    printf("📥 Enter a number: ");
    scanf("%d", &input);
    printf("You entered: %d\n\n", input);

    // 3. Conditional Statements
    printf("🔁 If-Else Check:\n");
    if (input > 0)
        printf("Positive number\n");
    else if (input < 0)
        printf("Negative number\n");
    else
        printf("Zero\n");
    printf("\n");

    // 4. Loops
    printf("🔄 For loop from 1 to 5:\n");
    for (int i = 1; i <= 5; i++) {
        printf("%d ", i);
    }
    printf("\n\n");

    // 5. Arrays
    printf("📚 Array Example:\n");
    int nums[] = {1, 2, 3, 4, 5};
    int len = sizeof(nums) / sizeof(nums[0]);
    for (int i = 0; i < len; i++) {
        printf("nums[%d] = %d\n", i, nums[i]);
    }
    printf("\n");

    // 6. Functions
    printf("📞 Function Call: add(10, 15)\n");
    int result = add(10, 15);
    printf("Result = %d\n\n", result);

    // 7. Structures
    printf("👤 Structure Example:\n");
    struct Student s1;
    strcpy(s1.name, "John Doe");
    s1.age = 20;
    s1.marks = 88.5;

    printf("Name: %s\n", s1.name);
    printf("Age: %d\n", s1.age);
    printf("Marks: %.2f\n", s1.marks);

    return 0;
}

// Function definition
int add(int a, int b) {
    return a + b;
}
