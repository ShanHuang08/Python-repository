from datetime import datetime
def MCAToday():
    date_time=datetime.now()
    date_time=str(date_time)
    # print(date_time[0:10]) #今天
    year=date_time[0:4]
    month=date_time[5:7]
    dates=int(date_time[8:10]) #10號

    if date_time[8:10]=='01'and int(date_time[11:13])<12: #本月第一天 and 12點以前
        if month in ['01']: #1月1日
            date_time=str(int(year)-1)+'-12-31'
        elif month in ['03']: #3月1日
            date_time=year+'-'+str(int(month)-1)+'-28'
        elif month in ['02','04','06','08','09','11']: #大月
            date_time=year+'-'+str(int(month)-1)+'-31'
        elif month in ['05','07','10','12']: #小月
            date_time=year+'-'+str(int(month)-1)+'-30' 
    elif int(date_time[11:13])<12: #12點以前
        date_time=date_time.replace(str(dates),str(dates-1)) #replace(原本str, 新str) 變成昨天
        # print(date_time[0:10])
        if dates<11:
            List=list(date_time)
            # print(List[4:6])
            List.insert(8,'0') #把0加回去
            date_time=''.join(List)
            # print(date_time[0:10]) #昨天
   
    return date_time[0:10]

if __name__=='__main__':
    print(MCAToday())
