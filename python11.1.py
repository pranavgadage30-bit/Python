#id,title,author,name-->curd
#(1,"xyz",("abc",900))
books=()

while True:
    print("library management system\n1.Add Book\n2.Update book\n3.Display book\n4.Delete book\n5.Exit")
    choice=int(input("Enter the choice:"))
   
    if choice==1:
        id=input("Enter book id:")
        title=input("Enter book name:")
        authorname=input("Enter author name:")
        price=float(input("Enter the book price:"))
        
        new_book=(id,title,(authorname,price))
        books=books+(new_book,)  
        print("BOOK ADDED SUCCESSFULLY")
   
    elif choice==2:
        user_ip=input("Enterthe book id to update:")
        book_list=list(books)
        found=False
        
        for i in range(len(books)):
            if book_list[i][0]==user_ip:
                title=input("Enter book name:")
                authorname=input("Enter author name:")
                price=float(input("Enter the book price:"))
                
                book_list[i]=(user_ip,title,(authorname,price))
                found=True
        books=tuple(book_list)

        if found:
            print("DATA UPDATED")
        else:
            print("ID NOT FOUND")
   
    elif choice==3:
        print("BOOK DETAILS ARE")
        for info in books:
            print(f"ID:{info[0]}")
            print(f"Title:{info[1]}")
            print(f"Author Name:{info[2][0]}")
            print(f"Price:{info[2][1]}")
   
    elif choice==4:
        user_ip=input("Enter book id to delete:")
        book_list=list(books)
        found=False
        
        for book in book_list:
            if book[0]==user_ip:
                book_list.remove(book)
                found=True
                break
        books=tuple(book_list)
        
        if found:
            print("Book Deleted")
        else:
            print("Id not found")
            
    elif choice==5:
        print("EXIT")
        break;
   
    else:
        print("INVALID INPUT")