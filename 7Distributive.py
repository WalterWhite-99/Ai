print("Enter values in 0 or 1.")

p = bool(int(input("Enter value for P: ")))
q = bool(int(input("Enter value for Q: ")))
r = bool(int(input("Enter value for R: ")))

lhs_OR_AND = p or (q and r)
rhs_OR_AND = (p or q) and (p or r)

print(f"\nLHS OR over AND : {lhs_OR_AND}")
print(f"RHS OR over AND : {rhs_OR_AND}")
print(f"Distributive Law of OR over AND i.e LHS_OR_AND == RHS_OR_AND : {lhs_OR_AND == rhs_OR_AND}\n")

lhs_AND_OR = p and (q or r)
rhs_AND_OR = (p and q ) or (p and r)

print(f"LHS AND over OR : {lhs_AND_OR}")
print(f"RHS AND over OR : {rhs_AND_OR}")
print(f"Distributive Law of AND over OR i.e LHS_AND_OR == RHS_AND_OR : {lhs_AND_OR == rhs_AND_OR}\n")

if lhs_OR_AND == rhs_OR_AND and lhs_AND_OR == rhs_AND_OR:
    print("Distributive Law is Verified.")