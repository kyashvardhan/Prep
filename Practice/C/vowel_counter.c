#include <stdio.h>
#include <ctype.h>

int countVowels(const char *str) {
    int count = 0;
    while (*str) {
        char ch = tolower(*str);
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
            count++;
        str++;
    }
    return count;
}

int main() {
    char str[200];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    
    int vowels = countVowels(str);
    printf("Number of vowels: %d\n", vowels);
    return 0;
}
