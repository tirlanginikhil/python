grade = lambda marks: "Pass" if marks >= 40 else "Fail"

marks = [35, 45, 67, 28, 80, 39]

for m in marks:
    print(m, ":", grade(m))