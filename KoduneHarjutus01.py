


# Harjutus 1 koduseks tegemiseks.

# Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
# 	kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# 	eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 1p
# 	kood mis teavitab paaris või paaritust arvust - 1p
# 	kuvatakse programmi pealkiri - 1p
# 	kood kommenteeritud - 1p

number = int(input("Enter a number : "))

# if the number is divisible by 2, then even
# else is odd

if number%2==0:
    print(number, "paaris.")
else:
    print(number, "paaritu.")


