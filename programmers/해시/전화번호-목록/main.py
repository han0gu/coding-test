def solution(phone_book):
    len_phone_book = len(phone_book)
    phone_book.sort()
    
    for i in range(len_phone_book-1):
        for j in range(i+1, len_phone_book):
            v1 = phone_book[i]
            v2 = phone_book[j]
            
            if v2.startswith(v1):
                return False
            
    return True