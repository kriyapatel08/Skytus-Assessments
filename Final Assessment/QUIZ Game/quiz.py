import json
import os
import random

HIGH_SCORE_FILE = "highscore.txt"


def load_questions():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "questions.json")

    print("Looking for:", file_path)
    print("Exists:", os.path.exists(file_path))

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("questions.json file not found!")

    except json.JSONDecodeError as e:
        print("JSON Error:", e)

    return []

def get_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            score = file.read().strip()
            return int(score) if score else 0
    return 0


def save_high_score(score):
    current = get_high_score()
    if score > current:
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(score))
        print("\n🎉 New High Score Saved!")
    else:
        print("\nHigh Score Remains:", current)


def show_result(score, total):
    wrong = total - score
    percentage = (score / total) * 100

    print("\n==============================")
    print("         QUIZ RESULT")
    print("==============================")
    print("Correct Answers :", score)
    print("Wrong Answers   :", wrong)
    print("Score           :", f"{score}/{total}")
    print("Percentage      :", f"{percentage:.2f}%")

    if percentage >= 90:
        grade = "Excellent"
    elif percentage >= 70:
        grade = "Good"
    elif percentage >= 50:
        grade = "Average"
    else:
        grade = "Needs Improvement"

    print("Grade           :", grade)

    save_high_score(score)


def start_quiz():
    questions = load_questions()

    if not questions:
        return

    random.shuffle(questions)

    score = 0

    print("\nQuiz Started...\n")

    for i, q in enumerate(questions, start=1):

        print("=" * 40)
        print(f"Question {i}")
        print(q["question"])
        print()

        options = q["options"]

        letters = ["A", "B", "C", "D"]

        for letter, option in zip(letters, options):
            print(f"{letter}. {option}")

        answer = input("\nEnter Option (A/B/C/D): ").upper()

        while answer not in letters:
            answer = input("Invalid! Enter A/B/C/D: ").upper()

        selected = options[letters.index(answer)]

        if selected == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print("❌ Wrong!")
            print("Correct Answer:", q["answer"], "\n")

    show_result(score, len(questions))


def view_high_score():
    print("\nHighest Score:", get_high_score())


def main():

    while True:

        print("\n==============================")
        print("       QUIZ GAME")
        print("==============================")
        print("1. Start Quiz")
        print("2. View High Score")
        print("3. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            start_quiz()

        elif choice == "2":
            view_high_score()

        elif choice == "3":
            print("\nThank You!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()