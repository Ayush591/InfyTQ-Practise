# Solution for Assignment 21

def generate_next_date(day,month,year):
    #Start writing your code here
    if(day==31):
        if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10):
            next_day=1
            next_month=month+1
            next_year=year
        elif(month==12):
            next_day=1
            next_month=1 
            next_year=year+1 
            year=year+1
    elif(day==30):
        if(month==4 or month==6 or month==9 or month==11):
            next_day=1 
            next_month=month+1 
            next_year=year
    elif(day==28 and month==2):
        if(year%4 ==0 and year%100!=0 and year%400 == 0):
            next_day=day+1
            next_month=month
            next_year=year
        else:
            next_day=1 
            next_month=month+1
            next_year=year
    elif(day==29 and month==2):
        next_day=1 
        next_month= month+1 
    else:
        -1
    print(next_day,"-",next_month,"-",next_year)

generate_next_date(31,12,2015)
