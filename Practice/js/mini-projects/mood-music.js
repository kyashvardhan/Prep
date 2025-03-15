// Simple AI Mood-based Music Recommendation
const moodMusic = {
    happy: ["Happy by Pharrell Williams", "Can't Stop the Feeling"],
    sad: ["Someone Like You - Adele", "Fix You - Coldplay"],
    energetic: ["Eye of the Tiger", "Stronger - Kanye West"],
    calm: ["Weightless - Marconi Union", "Clair de Lune - Debussy"],
};

function recommendMusic(mood) {
    if (moodMusic[mood]) {
        console.log(`🎵 Based on your mood (${mood}), we recommend: ${moodMusic[mood][Math.floor(Math.random() * moodMusic[mood].length)]}`);
    } else {
        console.log("😕 Mood not recognized. Try happy, sad, energetic, or calm.");
    }
}

// Usage Example
recommendMusic("happy");
