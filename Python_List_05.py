#List Operations
#count
#index
#pop
#remove
#sort
#insert
#append
#extend

stocks=[23,45,56,67,78,32,41]
print(stocks.count(23))
print(stocks.index(67))
print(stocks.pop())
stocks.remove(56)
print(stocks)
stocks.insert(5, 31)
print(stocks)
stocks.sort()
print(stocks)
stocks.append(100)
Mutlibagger = [5,9,2,11,7]     #Append method adds the entire list at the end of the prev list
stocks.append(Mutlibagger)
print(stocks)
Gstocks="Tata"
stocks.extend(Gstocks)   #Whereas the extend method reads each and every character in a separate index
print(stocks)
