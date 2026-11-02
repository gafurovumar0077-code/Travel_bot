# c1) mutible in ivazshavanda meboshad yane int mo adad 
# medihem va dokhilashro metavonem ivaz kunem ammo unmutiblero boshad str tuple meboshand ki mo metavonem ivaz kunem bo 
# yak du tarzho ammo adresashon hamun memonad yane dar pamyat hamonro ne balki yaktoi digar mesozad monandi hamon fakat ivas mekunad.
# c2) try-except-finally  in baroi on ast ki mo  ashibkaro chi tavr nishon dodanashro khudamon medihem 
# va misli popitka kardan agar shavad barorad agar nashavad oshibkaro niz tarzi barovardanashro medinem va dar baze joyho misli sangish istifoda mebarem.
# c3) tuple in unmutable yane ivaznashavanda ast va teztar kor mekunad az sababi on ki yagon metod nadorad farkiyatash az list hamin ast
#  list boshad mutable meboshad matod dorad as in sabab korash sustar ast dar holate istifoda burdan lozim ast ki mo naznacheniyari ivas kardan lozim nest
# c4) peremenni in misli nom meboshad va mo onro medihem to in ki dar on yak kor yo yagon znacheniyaro dar khud kanul kunad 
#  tipi dannikh inho baroi anik kardani znacheniya meboshad misol int-in adaro kabul mekunad, str-in text kabul mekunad, bool-in true yo false budanro vazvrachat mekunad, float-in bo adadhoi asdahdor kor mekunad.

# c5
# def fibonacci(n)
#     a=[]
#     s=int(n)
#     cnt=0
#     for i in range(s):
        
        
         

# c6
# a=list(i for i in range(1, 50) if i%3==0)
# print(a)




# c7
# with open("tex.txt", "r") as file:
#     cnt=0
#     for i in file:
#         cnt+=1
#     print(cnt)
        

# c8
# def word_count(text):
#     cnt = {}
#     for word in text.lower().split():
#         cnt[word]=cnt.get(word,0)+1
#     print(cnt)
# word_count("Hello, hello! Python is great. Python is fun.")




# c9
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner=owner
#         self.balance=balance

#     def deposit(self, amount):
#         self.balance+=amount
#         print(f"{amount} added successfully")

#     def withdraw(self, amount):
#         if amount>self.balance:
#             print("Маблағ кофӣ нест")
#         else:
#             self.balance-=amount
#             print(f"{amount} withdrawn successfully")

#     def __str__(self):
#         return f"Owner: {self.owner}, Balance: {self.balance}"

# account=BankAccount("Alice", 1000)
# print(account)
# account.deposit(500)
# account.withdraw(2000)
# print(account)







# c10
# from time import *

# def timing_decorator(func):
#     def second():
#         s=time()
#         print(f"sec: {time()-s}")
#         return func()
#     return second

# @timing_decorator
# def mil():
#     return sum(range(1, 1000000))
# print(mil())











def wer(num):
    def rew(nam):
        return num+nam
    return rew

print(wer(1,1))

