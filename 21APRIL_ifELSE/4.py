'''4. 4. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test'''


sb=input("Subscription = ").lower()
p=int(input("Progess = "))
ts=int(input("Test Score = "))

if sb=="premium":
    if p>=80:
        if ts>=70:
            acc="certificate unlock"
        else:
            acc="Retry test"
    else:
        acc="please complete course"
elif sb=="basic":
    if p>=50:
        acc="Limited access"
    else:
        acc="content locked"
else:
    acc="access denied"
print("Access Status =",acc)
