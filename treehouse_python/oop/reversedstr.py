"""
O método new opera na classe e não na instância.
Unsafe usar super inside new. Por isso str.__new__() ao invés de super().__init__()
Lista usa-se __init__ um vez que é mutável
"""

class ReversedStr(str):

    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs) # herda classe string e usa-se new ao invés de __init__ pq é objeto imutável
        self = self[::-1]
        return self


rs = ReversedStr('hello')
print(rs)
print(len(rs))