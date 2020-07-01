from string import Template
import datetime

#using str.template and substitute
str = "the quick brown $animal $action over the grapes"
template = Template(str)
print(template.substitute(animal="fox",action="jumped"))

dict = {
    "animal": "cow",
    "action": "jumped"
}

print(template.substitute(dict))

#using str.format
foo = "foo"
bar = 123
print("output = {1} {0}".format(foo,bar))
print("output = {var1:x} {var1:b} {var2}".format(var2=foo,var1=bar))

#string interpolation
now=datetime.datetime.now()
print(f"{foo} product has a price of {bar*2}")
print(f"{now:%B %d %Y}")
