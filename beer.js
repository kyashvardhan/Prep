/*Lyrics of the song 99 Bottles of Beer
99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.

98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.

97 bottles of beer on the wall, 97 bottles of beer.
Take one down and pass it around, 96 bottles of beer on the wall.

96 bottles of beer on the wall, 96 bottles of beer.
Take one down and pass it around, 95 bottles of beer on the wall. */

var beer=99;

while (beer >= 1) {
    console.log(`${beer} bottles of beer on the wall, ${beer} bottles of beer.`);
    beer--; // Decrement after printing
    if (beer > 0) {
        console.log(`Take one down and pass it around, ${beer} bottles of beer on the wall.`);
    } else {
        console.log(`Take one down and pass it around, no more bottles of beer on the wall.`);
    }
}
