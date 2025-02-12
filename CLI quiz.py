import json

def load_questions():
    return [
        {"question": "What is the capital of France?", "options": ["A. Paris", "B. Rome", "C. Berlin", "D. Madrid"], "answer": "A"},
        {"question": "Which planet is known as the Red Planet?", "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"], "answer": "C"},
        {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["A. J.K. Rowling", "B. Harper Lee", "C. Ernest Hemingway", "D. Mark Twain"], "answer": "B"}
    ]

def run_quiz():
    score = 0
    questions = load_questions()
    
    for index, q in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {q['question']}")
        for option in q['options']:
            print(option)
        
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if user_answer == q['answer']:
            print("Correct! ✅")
            score += 1
        else:
            print(f"Incorrect! ❌ The correct answer was {q['answer']}.")
    
    print(f"\nQuiz Over! Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
