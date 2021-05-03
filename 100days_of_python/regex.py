from RegexGenerator import RegexGenerator
#myRegexGenerator = RegexGenerator("123-555-7676")
myRegexGenerator = RegexGenerator("PERICULOSIDADE 01/10/2010 08:00 10/10/20 Ativo")


print(myRegexGenerator)

print(myRegexGenerator.get_regex())
