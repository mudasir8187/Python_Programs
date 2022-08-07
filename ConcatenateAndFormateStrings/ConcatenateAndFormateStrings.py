print("                Concatenate Strings                    ")
print("                                                       ")
a="Mudasir"
b="Ali"
c=a+b
print(c)
print(a+" "+b)
print("                                                       ")
print("                Formate Strings                        ")
# We can't combine Strings and Integers together but with the help of formate string we can do that 
print("                                                       ")
age=21
txt="My name is Moni, I'm {}"
print(txt.format(age))
print("                                                       ")
print("                Placing unlimited arguments            ")
print("                                                       ")
x="Moni"
y=1102
z="Bs"
txt="I'm {},my roll no is {} and I'm in grade {}"
print(txt.format(x,y,z))