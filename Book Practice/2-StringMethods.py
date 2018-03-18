#Page 24
#Some String Methods
name = 'ada lovelace'
print(name.title()) #capitlize first letter of each word (?)
print(name.upper()) #upper case method
print(name.lower()) #lower case method


#Page 25
#Concatenating Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

message = "Hello, " + full_name.title() + "!"
print(message)


#Page 26
print("Python")
print("\tPython") #note, " and ' both refer to Strings

print("Languages:\n\tPythin\n\tC\n\tJavaScript")


#Page 27
favorite_language = 'python ' #notice there is an extra space at the end
print(favorite_language + ".")
favorite_language.rstrip() #takes out the spaces, BUT doesn't save anywhere
print(favorite_language + ".") #we still see the space here
favorite_language = favorite_language.rstrip() #NOW we are saving it
print(favorite_language + ".") #no longer wee the space here

# .lstrip() --> takes whitespace out from the left
# .strip()  --> takes whitespace out from both sides


#Page 28
message = "One of Python's strengths is its diverse community."
# ^ You can have the ' inside the string because you are using double quotation marks
# If you try to do it with single quotation marks, it will be a syntax error
# And vice versa...
