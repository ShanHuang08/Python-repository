def stock_list(listOfArt, listOfCat):
    # Split the query by alphabet and numeric for easy processing
    new = [x.split(' ') for x in listOfArt] #[['ABART', '20'], ['CDXEF', '50'], ['BKWRK', '25'], ['BTSQZ', '89'], ['DRTYM', '60']]

    d = {x : 0 for x in listOfCat} #{'B': 0, 'R': 0, 'D': 0, 'X': 0}

    totals = []
    if len(listOfArt) > 0:
        for x, y in new:
            # print(d[x[0]]) A not in d{} 所以出錯
            if x[0] in d:
                # Convert the numeric value into int and add it to the corresponding key values in d dict
                # print(d)
                # {'B': 0, 'R': 0, 'D': 0, 'X': 0}
                # {'B': 25, 'R': 0, 'D': 0, 'X': 0}
                # {'B': 114, 'R': 0, 'D': 0, 'X': 0}
                d[x[0]] += int(y)   
                # print(d) 
                # {'B': 25, 'R': 0, 'D': 0, 'X': 0}
                # {'B': 114, 'R': 0, 'D': 0, 'X': 0}
                # {'B': 114, 'R': 0, 'D': 60, 'X': 0}

        for a, b in d.items():
            # print(a) #B, R, D, X
            # print(b) #114, 0, 60, 0
            totals.append(f'({a} : {b})')
    else:
        return ''
    
    # Join the totals list to generate proper formatting for resonse
    print(''.join(totals)) #(B : 114)(R : 0)(D : 60)(X : 0)
    print(' - '.join(totals)) #(B : 114) - (R : 0) - (D : 60) - (X : 0)
    return (' - ').join(totals)

if __name__=='__main__':
    stocklist = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
    Clist= ['B', 'R', 'D', 'X']
    stock_list(stocklist, Clist)