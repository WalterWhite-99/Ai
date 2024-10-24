p = bool(int(input("Enter value for P (0 or 1) : ")))
q = bool(int(input("Enter value for Q (0 or 1) : ")))

lhs_first_law = not(p and q)
rhs_first_law = not(p) or not(q)

print(f"LHS of First Law : {lhs_first_law}")
print(f"RHS of First Law : {rhs_first_law}\n")

lhs_second_law = not(p or q)
rhs_second_law = not(p) and not(q)

print(f"LHS of Second Law : {lhs_second_law}")
print(f"RHS of Secong Law : {rhs_second_law}\n")

if lhs_first_law == rhs_first_law and lhs_second_law == rhs_second_law:
    print("Demorgan's First and Second Law is verified.")
else:
    print("Demorgan's First and Second Law is NOT verified.")

