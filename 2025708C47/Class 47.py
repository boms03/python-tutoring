sales_data=[('Alice', 'Product A', 100),('Bob', 'Product B', 150),('Charlie', 'Product A', 80)]

TotalA=0
TotalB=0

for i in sales_data:
    if i[1]=='Product A':
        TotalA=TotalA+i[2]
    else:
        TotalB=TotalB+i[2]
print(TotalA)
print(TotalB)



Totals={j:sum(k[2] for k in sales_data if j==k[1])for j in {i[1] for i in sales_data}}
print(Totals)
                                                                
