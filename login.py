data={"username" : "ace","password" : "1234"}
user=input("masukkan user name anda:")
password=input("masukkan password anda:")
if user==data["username"]:
	if password !=data["password"]:
		print("password salah")
	else:
		print("login berhasil")
else:
	print("username salah")
		
		
	