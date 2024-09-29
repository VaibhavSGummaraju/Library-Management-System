Python code



import numpy as np
import pandas as pd 
import mysql.connector
print('                    ===============================')
print('                      LIBRARY MANAGEMENT SYSTEM')
print('                    ===============================')
def start():
    while(True):
        print('1.books details')
        print('2.member details')
        print('3.transactions')
        print('4.exit')
        ch1=int(input('enter your choice:'))
        if(ch1==1):
            booksdetails_create()
        elif(ch1==2):
            memberdetails_create()
        elif(ch1==3):
            transactions_create()
        elif(ch1==4):
            print('       ==========================')
            print('             Thank You            ')
            print('       ==========================')
        break
def booksdetails_create():
         while(True):
              print('1.search book')
              print('2.display available books')
              print('3. go to previous screen ')
              ch2=int(input('enter your choice:'))
              if(ch2==1):
                  s_create()
              elif(ch2==2):
                  d_create()
              elif(ch2==3):
                  start()
                                
              else:
                break
                
            
def d_create():
     conn=mysql.connector.connect(host='localhost',user='root',password='Vaibhav@123',database='lms1')
     a=conn.cursor()
     a.execute('select *from books')
     data1=a.fetchall()
     for i in data1:
         print(i)
     conn.commit()    



def s_create():
    while(True):
        print('1.search by bookid')
        print('2.search by bookname')
        print('3.search by aurthor')
        print('4.search by genre')
        ch3 = int(input('enter your choice:'))
        if(ch3 == 1):
            bookid_create()
        elif(ch3 == 2):
            bookname_create()
        elif(ch3 == 3):
            aurthor_create()
        elif(ch3 == 4):
            genre_create()
        else:
            start()

def bookid_create():
    conn=mysql.connector.connect(host='localhost',user='root',password='Vaibhav@123',database='lms1')
    a=conn.cursor()
    book_id=int(input('enter book id:'))
    a.execute('select *from books where BookId= "'+str(book_id)+'"')
    data1=a.fetchall()
    print('bookid=',data1[0][0],'bookname=',data1[0][1],'genre=',data1[0][2],'author=',data1[0][3])
    for i in data1:
        print(i)
    a.close()    
        

        
def bookname_create():
    conn=mysql.connector.connect(host='localhost',user='root',password='Vaibhav@123',database='lms1')
    a=conn.cursor()
    book_name=input('enter the book name: ')
    a.execute('select *from books where BooksName= "'+book_name+'"')
    data1=a.fetchall()
    print('bookid=',data1[0][0],'bookname=',data1[0][1],'genre=',data1[0][2],'author=',data1[0][3])
    for i in data1:
        print(i)
    a.close()
    
    
def aurthor_create():
    conn=mysql.connector.connect(host='localhost',user='root',password='Vaibhav@123',database='lms1')
    a=conn.cursor()
    aurthor_name=input('enter the aurthor name:')
    a.execute('select *from books where author= "'+aurthor_name+'"')
    data1=a.fetchall()
    print('bookid=',data1[0][0],'bookname=',data1[0][1],'genre=',data1[0][2],'author=',data1[0][3])
    for i in data1:
        print(i)
    a.close()
        

def genre_create():
    conn=mysql.connector.connect(host='localhost',user='root',password='Vaibhav@123',database='lms1')
    a=conn.cursor()
    genre_name=input('enter the genre:')
    a.execute('select *from books where genre= "'+ genre_name +'"')
    data1=a.fetchall()
    print('bookid=',data1[0][0],'bookname=',data1[0][1],'genre=',data1[0][2],'author=',data1[0][3])
    for i in data1:
        print(i)
    a.close()

    

def memberdetails_create():
    while(True):
        print('1.Display members details')
        print('2.add member details')
        print('3.delete member details')
        print('4.search members')
        print('5.go to the previous option')
        ch4=int(input('Enter your choice:'))
        if(ch4==1):
            memdetails_create()
        elif(ch4==2):
            add_create()
        elif(ch4==3):
            delete_create()
        elif(ch4==4):
            search_create()
        elif(ch4==5):
                  start()
        else:
            break
        
    

def memdetails_create():
     conn=mysql.connector.connect(host='localhost',user='root',password='Vaibhav@123',database='lms1')
     a=conn.cursor()
     a.execute('select *from members')
     data1=a.fetchall()
     for i in data1:
         print(i)


def add_create():
    conn=mysql.connector.connect(host='localhost',user='root',password='Vaibhav@123',database='lms1')
    a=conn.cursor()
    #a.execute('select memberId *from members')
    a.execute('select *from members')
    data1=a.fetchall()
    for i in data1:
         print(i[1])
    membername=input('enter your name:')
    memberid=int(input('enter the next memberid:'))
    joindate=input('enter date:')
    a.execute('insert into members values("'+membername+'","'+str(memberid)+'","'+joindate+'")')
    a.execute('select *from members')
    data1=a.fetchall()
    for i in data1:
         for j in i:
             print(j,end='\t')
         print()
    conn.commit()     


def delete_create():
    conn=mysql.connector.connect(host='localhost',user='root',password='Vaibhav@123',database='lms1')
    a=conn.cursor()
    name_delete=input('enter the name to be deleted:')
    a.execute('DELETE FROM members WHERE membername = %s', (name_delete,))
    a.execute('select *from members')
    data1=a.fetchall()
    for i in data1:
        print(i)
    print('members details deleted successfully')
    
    conn.commit()

    
def search_create():
    while(True):
        print('1.search by name')
        print('2.search by memberId')
        ch3=int(input('enter your choice:'))
        if(ch3==1):
            name_create()
        if(ch3==2):
            member_id()
        else:
            print('invalid input')
            
        
def name_create():
    conn=mysql.connector.connect(host='localhost',user='root',password='Vaibhav@123',database='lms1')
    a=conn.cursor()
    name=input('enter the name:')
    a.execute('select *from members where name="'+name+'"')
    data1=a.fetchall()
    for i in data1:
        print(i)


def member_id():
    conn=mysql.connector.connect(host='localhost',user='root',password='Vaibhav@123',database='lms1')
    a=conn.cursor()
    memberid=int(input('enter the memberid:'))
    a.execute('select *from members where memberId="'+str(memberid)+'"')
    data1=a.fetchall()
    for i in data1:
        print(i)



def transactions_create():
    while(True):
        print('1.modify book details')
        print('2.show graph')
        print('3.go back to previous options')
        ch5=int(input('enter your choice'))
    
        if(ch5==1):
            modify_create()
        elif(ch5==2):
            graph_create()
        elif(ch5==3):
            start()
    
        else:
            break
        

def modify_create():
    while(True):
            print('1.add books details')
            print('2.update books details')
            print('3.delete books details')
            print('4.go back to previous options')
            ch=int(input('enter your choice'))
            if(ch==1):
                addbooks_create()
            elif(ch==2):
                updatebooks_create()
            elif(ch==3):
                deletebooks_create()
            elif(ch==4):
                  start()
            else:
                break
        
def addbooks_create():
    conn=mysql.connector.connect(host='localhost',user='root',password='Vaibhav@123',database='lms1')
    a=conn.cursor()
    bookname=input('enter bookname:')
    bookid=int(input('enter bookid:'))
    genre=input('enter the book genre:')
    author=input('enter the name of the author of the book:')
    price=int(input('enter book price:'))
    copies=int(input('enter number of copies available:'))
    a.execute('insert into books values("'+str(bookid)+'","'+bookname+'","'+genre+'","'+author+'","'+str(price)+'","'+str(copies)+'")')
    a.execute('select *from books')
    print('books details added successfully')
    data1=a.fetchall()
    for i in data1:
        print(i)
    conn.commit()

def deletebooks_create():
    conn=mysql.connector.connect(host='localhost',user='root',password='Vaibhav@123',database='lms1')
    a=conn.cursor()
    bookname=input('enter bookname:')
    a.execute('delete from books where booksname="'+bookname+'"')
    a.execute('select *from books')
    print('book details deleted successfully')
    data1=a.fetchall()
    for i in data1:
        print(i)
    conn.commit()
    
    
def updatebooks_create():
    conn=mysql.connector.connect(host='localhost',user='root',password='Vaibhav@123',database='lms1')
    a=conn.cursor()
    bookid=input('enter bookid:')
    a.execute('select *from books where BookId= "'+str(bookid)+'"')
    data1=a.fetchall()
    print('bookid=',data1[0][0],'bookname=',data1[0][1],'genre=',data1[0][2],'author=',data1[0][3])
    for i in data1:
        print(i)
    copies=int(input('enter number of copies available:'))
    a.execute('update books set copiesavailable="'+str(copies)+'" where bookid="'+bookid+'"')
    a.execute('select *from books')
    print('book details updated successfully')
    data1=a.fetchall()
    for i in data1:
        print(i)
    conn.commit()


def graph_create():
    import matplotlib.pyplot as plt
    import numpy as np
    comp=np.array(['harry potter','wings of fire','da vince code'])
    emp=np.array([80,30,50])
    plt.bar(comp,emp)
    plt.xlabel('books name')
    plt.ylabel('copies available')
    plt.title('bar graph')
    plt.show()

while(True):
    print('1.books details')
    print('2.member details')
    print('3.transactions')
    print('4.exit')
    ch1=int(input('enter your choice:'))
    if(ch1==1):
        booksdetails_create()
    elif(ch1==2):
        memberdetails_create()
    elif(ch1==3):
        transactions_create()
    elif(ch1==4):
        print('       ==========================')
        print('             Thank You            ')
        print('       ==========================')
    break
         
else:
    print('invalid choice')
