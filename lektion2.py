user_name = input("skriv ditt namn")
print(f"hej{user_name}! vad kul att du är här")

user_age = input ("skriv din ålder i år: ")
print(f"tack vad fint att du är {user_age} år gammal")
user_age_converted = int(user_age)
if user_age_converted >= 93:
    print("du får köra permobil")
else:
    print("q")
