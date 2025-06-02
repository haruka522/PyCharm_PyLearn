
diary_date = input("Enter today's date: ").strip()
user_mood = input("How do you rate your mood today from 1 to 10? ")

user_thoughts = input("Let your thoughts flow: \n")

with open(f"diary/{diary_date}.txt", "w") as file:
    file.write(user_mood + 2 * "\n")
    file.write(user_thoughts)
