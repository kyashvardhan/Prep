#!/usr/bin/env python3
"""
hello_world_languages.py
"""

HELLO_TRANSLATIONS = {
    "English 🇬🇧": "Hello, World!",
    "Spanish 🇪🇸": "¡Hola, Mundo!",
    "French 🇫🇷": "Bonjour, le Monde!",
    "German 🇩🇪": "Hallo, Welt!",
    "Italian 🇮🇹": "Ciao, Mondo!",
    "Portuguese 🇵🇹": "Olá, Mundo!",
    "Russian 🇷🇺": "Привет, мир!",
    "Chinese 🇨🇳": "你好，世界！",
    "Japanese 🇯🇵": "こんにちは、世界！",
    "Korean 🇰🇷": "안녕하세요, 세계!",
    "Hindi 🇮🇳": "नमस्ते, दुनिया!",
    "Bengali 🇧🇩": "হ্যালো, বিশ্ব!",
    "Arabic 🇸🇦": "مرحبا بالعالم!",
    "Greek 🇬🇷": "Γειά σου, Κόσμε!",
    "Hebrew 🇮🇱": "שלום עולם!",
    "Swahili 🌍": "Salamu, Dunia!",
    "Turkish 🇹🇷": "Merhaba, Dünya!",
    "Vietnamese 🇻🇳": "Xin chào, Thế giới!",
    "Thai 🇹🇭": "สวัสดีชาวโลก!",
    "Dutch 🇳🇱": "Hallo, Wereld!",
    "Polish 🇵🇱": "Witaj, Świecie!",
    "Persian 🇮🇷": "سلام دنیا!",
    "Indonesian 🇮🇩": "Halo, Dunia!",
    "Urdu 🇵🇰": "ہیلو، دنیا!",
    "Malayalam 🇮🇳": "ഹലോ വേൾഡ്!",
}

def print_hello_worlds():
    print("🌍 Hello, World! in Different Languages 🌍\n")
    for lang, greeting in HELLO_TRANSLATIONS.items():
        print(f"{lang}: {greeting}")

def main():
    print_hello_worlds()

if __name__ == "__main__":
    main()
