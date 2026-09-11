
## Collecting User Feedback
feedback = ["Poor Service", "Could do better", "Excellent Service", "Slow", "The absolute best", "Great"]

## Adding New Feedback
feedback.append("Worst Service Ever!")

## Feedback Count
positive_feedback = []
negative_feedback = []

for comment in feedback:
    if "excellent" in comment.lower() or "best" in comment.lower() or "great" in comment.lower():positive_feedback.append(comment)

    if "slow" in comment.lower() or "worst" in comment.lower() or "poor" in comment.lower() or "better"in comment.lower():negative_feedback.append(comment)

positive_feedback_count = len(positive_feedback)
negative_feedback_count = len(negative_feedback)

print(f"Negative Feedback Count: ", negative_feedback_count)
print(f"Positive Feedback Count: ", positive_feedback_count)

total_feedback = len(feedback)
positive_count = positive_feedback_count
negative_count = negative_feedback_count

## Calculate Percentage 
positive_percentage = (positive_feedback_count / total_feedback) * 100
negative_percentage = (negative_feedback_count / total_feedback) * 100

## Print Feedback
print("Positive Feedback:")
for comment in positive_feedback:
    print(f"- {comment}")

print("Negative Feedback:")
for comment in negative_feedback:
    print(f"- {comment}")

print("Total Feedback:", total_feedback)
print("Positive Percentage: ", positive_percentage)
print("Negative Percentage: ", negative_percentage)