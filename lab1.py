def listfun():
	carlist=['Ford','BMW','Volvo']
	print('I have',len(carlist),'cars to purchase.')
	print('the carlist is', carlist)
	print('\n1 also have to buy red.')
	carlist.append('red')
	print('My cars list is now',carlist)
	print('I will sort my list now')
	carlist.sort()
	print('sorted cars list is',carlist)
	print('The first car I will buy is',carlist[0])
	oldcars = carlist[0]
	print (carlist[0])
	print('I bought the', oldcars)
	del carlist[0]
	print('My cars list is now',carlist)
def tuplefun():
    forest=('elephant','lion','tiger')
    print('Number of animals in the forest is',len(forest))
    new_forest ='gorilla','giraffe',forest
    print('Number of ponds in the new forest is',len(new_forest))
    print('All animals in new forest are',new_forest)
    print('Animals came from old forest are',new_forest[1])
    print('last animal came from old forest is',new_forest[1][1])
    print('Number of animals in the new forest is',len(new_forest)-1+len(new_forest[1]))

listfun()
tuplefun()
