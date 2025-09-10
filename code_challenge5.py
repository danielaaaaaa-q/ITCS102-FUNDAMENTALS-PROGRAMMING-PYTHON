print("\t\t Welcome to the Manga Reader Recommender!")
print("\t\t------------------------------------------\n")
print("Answer a few questions to find new things to read.")

print("\nWhat genre do you like?")
print("1. Action")
print("2. Romance")
print("3. Horror")
genre_choice = input("Enter the choice in genre (1/2/3): ")

#-- Length --
how_long = input("How long should the manga be? (short/medium/long): ").lower()

#-- Year of Release --
year = eval(input("What year should the manga be released after? (2000s, 2010s): "))

#-- Action Recommendations --
print("\nHere are some recommendations for you!\n")
if genre_choice == "1":  # Action
    genre = "Action"
    print("You chose", genre," genre.")
    if how_long == "short" and year == 2000:
        print("For short manga recommendations from around the 2000s, consider collection such as: ", "\n -\"Blame!\" by Tsutomu Nihei", "\n -\"Gantz\" by Hiroya Oku", "\n -\"King of Thorn\" by Yuji Iwahara", "\n -\"Hotel\" by Boichi", "\n -\"Dogs: Stray Dogs Howling in the Dark\" by Shirow Miwa")
    elif how_long == "short" and year == 2010:
        print("For short manga recommendations from around the 2010s, consider collection such as: ", "\n -\"Tokyo Ghoul: Jack\" by Sui Ishida", "\n -\"Prophecy (Yokokuhan)\" by Tetsuya Tsutsui", "\n -\"Green Blood\" by Masasumi Kakizaki")
    elif how_long == "medium" and year == 2000:
        print("For medium-length manga recommendations from around the 2000s, consider collection such as: ", "\n -\"Black Cat\" by Kentaro Yabuki", "\n -\"666 Satan (O-Parts Hunter)\" by Seishi Kishimoto", "\n -\"Buso Renkin\" by Nobuhiro Watsuki", "\n -\"GetBackers\" by Yuya Aoki")
    elif how_long == "medium" and year == 2010:
        print("For medium-length manga recommendations from around the 2010s, consider collection such as: ", "\n -\"Ajin: Demi-Human\" by Gamon Sakurai", "\n -\"Akame ga Kill!\" by Takahiro and Tetsuya Tashiro", "\n -\"Btooom!\" by Junya Inoue")
    elif how_long == "long" and year == 2000:
        print("For long manga recommendations from around the 2000s, consider collection such as: ", "\n -\"Naruto\" by Masashi Kishimoto", "\n -\"Bleach\" by Tite Kubo", "\n -\"One Piece\" by Eiichiro Oda", "\n -\"Fullmetal Alchemist\" by Hiromu Arakawa", "\n -\"Death Note\" by Tsugumi Ohba and Takeshi Obata")
    elif how_long == "long" and year == 2010:
        print("For long manga recommendations from around the 2010s, consider collection such as: ", "\n -\"Attack on Titan (Shingeki no Kyojin)\" by Hajime Isayama", "\n -\"My Hero Academia (Boku no Hero Academia)\" by Kohei Horikoshi", "\n -\"Demon Slayer: Kimetsu no Yaiba\" by Koyoharu Gotouge")

#-- Romance Recommendations --
if genre_choice == "2":  # Romance
    genre = "Romance"
    print("You chose", genre," genre.")
    if how_long == "short" and year == 2000:
        print("For short manga recommendations from around the 2000s, consider collection such as: ", "\n -\"Bitter Virgin\" by Kei Kusunoki", "\n -\"Absolute Boyfriend\" by Yuu Watase")
    elif how_long == "short" and year == 2010:
        print("For short manga recommendations from around the 2010s, consider collection such as: ", "\n -\"Anohana: The Flower We Saw That Day\" by Mari Okada", "\n -\"L♥DK\" by Ayu Watanabe")
    elif how_long == "medium" and year == 2000:
        print("For medium-length manga recommendations from around the 2000s, consider collection such as: ", "\n -\"Peach Girl\" by Miwa Ueda", "\n -\"Dengeki Daisy\" by Kyousuke Motomi", "\n -\"Lovely★Complex\" by Aya Nakahara")
    elif how_long == "medium" and year == 2010:
        print("For medium-length manga recommendations from around the 2010s, consider collection such as: ", "\n -\"Strobe Edge\" by Io Sakisaka", "\n -\"Ao Haru Ride\" by Io Sakisaka", "\n -\"Kimi ni Todoke: From Me to You\" by Karuho Shiina")
    elif how_long == "long" and year == 2000:
        print("For long manga recommendations from around the 2000s, consider collection such as: ", "\n -\"Fruits Basket\" by Natsuki Takaya", "\n -\"Boys Over Flowers\" by Yoko Kamio", "\n -\"Boys Be…\" by Masahiro Itabashi and Hiroyuki Tamakoshi")
    elif how_long == "long" and year == 2010:
        print("For long manga recommendations from around the 2010s, consider collection such as: ", "\n -\"Skip Beat!\" by Yoshiki Nakamura", "\n -\"Domestic Girlfriend\" by Kei Sasuga")

#-- Horror Recommendations --
if genre_choice == "3":  # Horror   
    genre = "Horror"
    print("You chose", genre," genre.")
    if how_long == "short" and year == 2000:
        print("For short manga recommendations from around the 2000s, consider collection such as: ", "\n -\"Uzumaki\" by Junji Ito", "\n -\"The Enigma of Amigara Fault\" by Junji Ito", "\n -\"Gyo\" by Junji Ito")
    elif how_long == "short" and year == 2010:
        print("For short manga recommendations from around the 2010s, consider collection such as: ", "\n -\"Happiness\" by Shuzo Oshimi")
    elif how_long == "medium" and year == 2000:
        print("For medium-length manga recommendations from around the 2000s, consider collection such as: ", "\n -\"Parasyte (Kiseijuu)\" by Hitoshi Iwaaki", "\n -\"Tomie\" by Junji Ito")
    elif how_long == "medium" and year == 2010:
        print("For medium-length manga recommendations from around the 2010s, consider collection such as: ", "\n -\"Another\" by Yukito Ayatsuji", "\n -\"Ajin: Demi-Human\" by Gamon Sakurai")
    elif how_long == "long" and year == 2000:
        print("For long manga recommendations from around the 2000s, consider collection such as: ", "\n -\"Alive: The Final Evolution\" by Tadashi Kawashima", "\n -\"Hellsing\" by Kouta Hirano")
    elif how_long == "long" and year == 2010:
        print("For long manga recommendations from around the 2010s, consider collection such as: ", "\n -\"Terra Formars\" by Yu Sasuga", "\n -\"Chainsaw Man\" by Tatsuki Fujimoto")

else: 
    print("Invalid genre choice. Please restart the program and select a valid option.")

print("\nThank you for using the Manga Reader Recommender. Happy reading!")

