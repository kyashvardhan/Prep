#include <stdio.h>

double celsiusToFahrenheit(double celsius) {
    return (celsius * 9 / 5) + 32;
}

double fahrenheitToCelsius(double fahrenheit) {
    return (fahrenheit - 32) * 5 / 9;
}

int main() {
    int choice;
    double temp, converted;
    
    printf("Temperature Converter\n");
    printf("1. Celsius to Fahrenheit\n");
    printf("2. Fahrenheit to Celsius\n");
    printf("Choose an option: ");
    scanf("%d", &choice);
    
    if(choice == 1) {
        printf("Enter temperature in Celsius: ");
        scanf("%lf", &temp);
        converted = celsiusToFahrenheit(temp);
        printf("%.2lf Celsius = %.2lf Fahrenheit\n", temp, converted);
    } else if (choice == 2) {
        printf("Enter temperature in Fahrenheit: ");
        scanf("%lf", &temp);
        converted = fahrenheitToCelsius(temp);
        printf("%.2lf Fahrenheit = %.2lf Celsius\n", temp, converted);
    } else {
        printf("Invalid option.\n");
    }
    
    return 0;
}
