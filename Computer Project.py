import pymysql as x
def database():
    try:
        q=x.connect(host='localhost',user='root',password='utf8',database='pqr',charset='utf8')
        cur=q.cursor()
        s='create table rashan(sno int primary key ,item varchar(30), price int, Quantity int);'
        r=cur.execute(s)
        q.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        q.close()

def adr():
    n=int(input('Enter how many records you need:'))
    v="insert into rashan values(%s,%s,%s,%s)"
    for y in range (n):
        s=int(input('enter the serial number:'))
        i=input('enter the item:')
        p=int(input('enter the price:'))
        a=int(input('enter the quantity:'))
        try:
            q=x.connect(host='localhost',user='root',password='utf8',database='pqr',charset='utf8')
            cur=q.cursor()
            cur.execute(v,(s,i,p,a))
            q.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()
            q.close()



def modify():
    z=input('Enter the item name:')
    b=int(input('Enter the quantity of the item from the table:'))
    try:
        q=x.connect(host='localhost',user='root',password='utf8',database='pqr',charset='utf8')
        cur=q.cursor()
        u='update rashan SET item=%s where quantity= %s;'
        r=cur.execute(u,(z,b))
        q.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        q.close()


def abc():
    print('1.whole row')
    print('2.Specific ')
    print('3.Whole table')
    c=int(input('enter your choice:'))
    try:
        q=x.connect(host='localhost',user='root',password='utf8',database='pqr',charset='utf8')
        cur=q.cursor()
        if c==1:
            sno=int(input('enter ur desired serial number:'))
            d = "DELETE FROM rashan WHERE sno = %s"
            cur.execute(d, (sno,))
            q.commit()
        elif c==2:
            item=input('Enter the item name:')
            ds='delete from rashan where item = %s;'
            cur.execute(ds, (item,))
            q.commit()
        elif c==3:
            dt='Delete from rashan;'
            r=cur.execute(dt)
            q.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        q.close()

def showcase():
    try:
        q=x.connect(host='localhost',user='root',password='utf8',database='pqr',charset='utf8')
        cur=q.cursor()
        s=' select* from rashan;'
        r=cur.execute(s)
        rec=cur.fetchall()
        print(rec)
        q.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        q.close()

def menu():
    while True:
        print('1. Create Database')
        print('2. Add record')
        print('3. Modify')
        print('4. Delete records')
        print('5. Show record')
        c=int(input('enter your choice : '))
        if c==1:
            database()
            break
        elif c==2:
            adr()
            break
        elif c==3:
            modify()
            break
        elif c==4:
            abc()
            break
        elif c==5:
            showcase()

        else:
            print('enter valid input')

menu()











