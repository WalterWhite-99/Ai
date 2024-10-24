print("Enter Values in 0 or 1.\n\n")

p = bool(int(input("Enter value for P: ")))
q = bool(int(input("Enter value for Q: ")))
r = bool(int(input("Enter value for R: ")))

lhs_OR = (p or q) or r
rhs_OR = p or (p or r)

print(f"\nLHS_OR : {lhs_OR}")
print(f"RHS_OR : {rhs_OR}")
print(f"Associative Law of OR i.e LHS_OR == RHS_OR : {lhs_OR == rhs_OR}\n")

lhs_AND = (p and q) and r
rhs_AND = p and ( q and r)

print(f"LHS_AND : {lhs_AND}")
print(f"RHS_AND : {rhs_AND}")
print(f"Associative Law of AND i.e LHS_AND == RHS_AND : {lhs_AND == rhs_AND}\n")

if lhs_OR == rhs_OR and lhs_AND == rhs_AND:
    print("Associative law of OR and AND is True")
    print("Associative Law is verified.")

