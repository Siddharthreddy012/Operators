# Logical operator on two persons about their height and weight 
ad=[5.9,80]
zu=[5.5,60]
stmt_1=ad[0]>zu[0]
stmt_2=ad[1]>zu[0]
print(stmt_1)
print(stmt_2)
res=stmt_1 and stmt_2
print("Our assumption is : ",res)
stmt_1=ad[0]<zu[0]
stmt_2=ad[1]<zu[1]
print(stmt_1)
print(stmt_2)
res=stmt_1 and stmt_2
print("Our assumption is : ",res)
stmt_1=ad[0]>zu[0]
stmt_2=ad[1]<zu[1]
print(stmt_1)
print(stmt_2)
res=stmt_1 and stmt_2
print("Our assumption is : ",res)
stmt_1=ad[0]<zu[0]
stmt_2=ad[1]>zu[1]
print(stmt_1)
print(stmt_2)
res=stmt_1 and stmt_2
print("Our assumption is : ",res)