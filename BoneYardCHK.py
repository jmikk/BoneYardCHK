from nsdotpy.session import NSSession


UA=input("USER_AGENT: ")
password=input("password for fresh finds")
email=input("email for your new pups")


session = NSSession("BoneYardCHK", "1.0.0", "9003", UA)

with open("list.txt","r") as f:
	pups = f.readlines()
for each in pups:
	if session.can_nation_be_founded(each.strip()):
		if not session.create_nation(each.strip(),password,email,"I love 9003","I love 9003","I love 9003"):
			input("Wait a bit and try this one again cuz you hit the limit")