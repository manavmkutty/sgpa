# KTU SGPA Calculator
# Non-credit subjects are ignored

total_credits = 0
total_points = 0

n = int(input("Enter total number of subjects: "))

for i in range(1, n + 1):
    print(f"\nSubject {i}")

    is_credit = input("Is this a credit subject? (yes/no): ").lower()

    if is_credit == "no":
        print("Non-credit subject ignored.")
        continue   # skip this subject

    credit = float(input("Enter credit: "))
    grade_point = float(input("Enter grade point: "))

    total_credits += credit
    total_points += credit * grade_point

# Avoid division by zero
if total_credits == 0:
    print("\nNo credit subjects entered. SGPA cannot be calculated.")
else:
    sgpa = total_points / total_credits
    print("\n-------------------------")
    print(f"Total Credits : {total_credits}")
    print(f"Your SGPA     : {sgpa:.2f}")
    print("-------------------------")
