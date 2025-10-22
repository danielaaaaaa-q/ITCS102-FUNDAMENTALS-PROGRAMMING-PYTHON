anime = ""
anime_list = []
while True:
    anime = input("Enter the title of an anime (or type 'exit' to finish): ")
    if anime.lower() == 'exit':
        print("You have exited the anime entry program.")
        break
    anime_list.append(anime)
    print(f"'{anime}' has been added to your anime list.")

print("Your anime list includes:")
for title in anime_list:
    print("-", title)




    

