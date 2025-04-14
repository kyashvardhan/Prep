#include <stdio.h>

char board[3][3];

void initializeBoard() {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            board[i][j] = ' ';
}

void printBoard() {
    printf("\n");
    for (int i = 0; i < 3; i++) {
        printf(" %c | %c | %c \n", board[i][0], board[i][1], board[i][2]);
        if (i != 2)
            printf("---|---|---\n");
    }
    printf("\n");
}

int checkWin() {
    // Check rows and columns.
    for (int i = 0; i < 3; i++) {
        if (board[i][0] != ' ' &&
            board[i][0] == board[i][1] &&
            board[i][1] == board[i][2])
            return board[i][0];
        if (board[0][i] != ' ' &&
            board[0][i] == board[1][i] &&
            board[1][i] == board[2][i])
            return board[0][i];
    }
    // Check diagonals.
    if (board[0][0] != ' ' &&
        board[0][0] == board[1][1] &&
        board[1][1] == board[2][2])
        return board[0][0];
    if (board[0][2] != ' ' &&
        board[0][2] == board[1][1] &&
        board[1][1] == board[2][0])
        return board[0][2];
    
    return ' '; // No winner yet.
}

int main() {
    initializeBoard();
    int row, col;
    char currentPlayer = 'X';
    int moves = 0;
    char winner = ' ';

    while (moves < 9 && winner == ' ') {
        printBoard();
        printf("Player %c, enter row and column (1-3): ", currentPlayer);
        scanf("%d %d", &row, &col);
        // Validate input.
        if (row < 1 || row > 3 || col < 1 || col > 3 || board[row-1][col-1] != ' ') {
            printf("Invalid move. Try again.\n");
            continue;
        }
        board[row-1][col-1] = currentPlayer;
        moves++;
        winner = checkWin();
        if (winner != ' ')
            break;
        // Switch player.
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }
    
    printBoard();
    if (winner != ' ')
        printf("Player %c wins!\n", winner);
    else
        printf("It's a draw!\n");
    
    return 0;
}
