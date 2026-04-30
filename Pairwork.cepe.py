#Developing a Smart Classroom Quiz & Performance Analyzer using Python 
#continuously allows students to participate in a quiz system. 
# This program takes student IDs, generates a unique value, conducts a quiz, and evaluates student performance.


# Step 1: Taking two student IDs as input
id1 = int(input("Enter ID of student 1: "))
id2 = int(input("Enter ID of Student 2: "))

# Extracting last two digits from both IDs
last2_id1 = id1 % 100
last2_id2 = id2 % 100

# Creating a small unique number based on both IDs
unique_value = (last2_id1 + last2_id2) % 10
print("\nUnique Value Generated:", unique_value)

# Step 2:Collecting student names dynamically
students = {}

print("\nEnter student names (type 'exit' to stop):")

# Loop continues until user decides to stop
while True:
    name = input("Student name: ").strip()

# Exit condition for stopping input
    if name.lower() == "exit":
        break

# Avoid storing blank entries
    if name == "":
        print("Warning: Empty name skipped!")
        continue

 # Adding student with initial score set to zero
    students[name] = 0  # initialize score

# Step 3: Showing all registered students
print("Student List")
for name in students:
    print(name)

# Step 4: Quiz section for each student

def run_quiz(name):
    score = 0

    print(f"Quiz for {name}")

 # Question based on generated value (Q1)
    q1 = unique_value + 2
    ans1 = int(input("Q1: unique_value + 2 = "))
    if ans1 == q1:
        score += 1

 # Second calculation-based question
    q2 = unique_value * 3
    ans2 = int(input("Q2: unique_value × 3 = "))
    if ans2 == q2:
        score += 1

# Final question for testing logic
    q3 = unique_value + 5
    ans3 = int(input("Q3: unique_value + 5 = "))
    if ans3 == q3:
        score += 1

 # Returning total marks earned
    return score

# Step 5: Evaluating each student's performance
for name in students:
    score = run_quiz(name)
    students[name] = score

# Deciding performance category
    if score == 3:
        level = "Excellent"
    elif score == 2:
        level = "Good"
    elif score == 1:
        level = "Need Improvement"
    else:
        level = "Poor Performance"

    print("Score:", score)
    print("Performance Level:", level)

# Checking if student qualifies for certificate
    if score >= 2:
        print("Certificate: Eligible for certificate")
    else:
        print("Certificate: Not Eligible for certificate")

    # Star pattern for outcomes
    print("Star Pattern:")
    if score > 0:
        
        print("*" * score)
    else:
        print("")

print("Final Results")
for name, score in students.items():
    print(f"{name}: {score} marks")

print ("End of the quiz")