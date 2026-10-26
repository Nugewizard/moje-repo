pocet_pokusu = 3
pin = "heslo"
validated = False
for i in range(pocet_pokusu):
	try:
		if input("zadej heslo: ") == pin:
			print("ověřeno")
			validated = True
			break
				
		else:
			print(f"špatné heslo, zbývá {pocet_pokusu-i-1}")
	except Exception as err:
		print(f"objevil se error: {err}")
if not validated == True:
	print("max pocet pokusu")

