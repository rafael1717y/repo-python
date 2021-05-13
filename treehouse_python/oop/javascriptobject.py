class JavaScriptObject(dict):

    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)


jso = JavaScriptObject({'name': 'Rafael'})
jso.language = 'Python'
print(jso.name)
print(jso.language)
#print(jso.fake)



class Double(int):

    def __new__(*args, **kwargs):
        self = int.__new__(*args, **kwargs)
        self = self * 2
        return self

dobro1 = Double(6)
print(dobro1)

dobro2 = Double(10)
print(dobro2)