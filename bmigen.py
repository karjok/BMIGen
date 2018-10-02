#source
s="     "
sp="     =================================================="
#source color
lr=('\033[91m')
lg=('\033[92m')
y=('\033[93m')
lb=('\033[94m')
cy=('\033[36m')
x=('\033[0m')
#source style
bld=('\033[01m')
udl=('\033[04m')

#this is for header
def head():
		print(bld+lr+"            ____________________________________")
		print(bld+lr+"     ______|"+x,"            °•°BMIGen°•°          ",lr+"|______")
		print(bld+lr+"     ======|_____"+x,"Body Mass Index Generator",lr+"____|======")
		print(bld+lr+"     ================",y+"By:Karjok Pangesty",lr+"=============="+x)
		print("\n")
		
#menu
def menu():
		head()
		print(s+y+"[+]"+x,"MENU",y+"[+]\n")
		print(s+lr+"  1."+x,"Mulai !")
		print(s+lr+"  2."+x,"Tentang")
		print(s+lr+"  3."+x,"Tentang Pengembang")
		print(s+lr+"  0."+x,"Keluar\n")
		
		
		#input user
		usr_in=input(s+"Aku pilih > ")
		while usr_in != "1" and usr_in != "2" and usr_in != "3" and usr_in != "0":
				print(s+lr+"Input Salah !!"+x)
				usr_in=input(s+"Aku pilih > ")
		
		#proces for input
		if usr_in=="1":
				name=input(s+"Siapa namamu ? > ")
				sex=input(s+"Jenis kelamin (co/ce) ? > ")
				while sex != "co" and sex != "ce":
					print(lr+s+"Jenis kelamin harus jelas, cowok atau cewek !"+x)
					sex=input(s+"Jenis Kelamin > ")
				bb=int(input(s+"Berat Badan (Kg) > "))
				tb1=int(input(s+"Tinggi Badan (Cm) > "))
				tb2=tb1/100
				bmi= int(bb/(tb2*tb2))

				#male function
				def male():
							if bmi < 17:
									cc="Kurus :'("
							elif bmi >=17 and bmi <23:
									cc="Normal ^_^"
							elif bmi >=23 and bmi <27:
									cc="Gendut :D"
							else:
									cc="Obesitas :o"
							return cc
				#female function			
				def female():
							if bmi < 18:
									cc="Kurus :'("
							elif bmi >=18 and bmi <25:
									cc="Normal ^_^"
							elif bmi >=25 and bmi <27:
									cc="Gendut :D"
							else:
									cc="Obesitas :o"
							return cc
							
				#output 
				def output(hasil_bmi):
							print(lr+sp+"\n"+x)
							print(s+"Hei "+name+" !")
							print(s+"Berat Badanmu  = ",y, bb,x," Kg")
							print(s+"Tinggi Badanmu = ",y,tb2,x," M")
							print(s+"BMI kamu       = ",y,bmi,x)
							print(s+"Dari hasil di atas,")
							print(s+"ku simpulin kalo kamu orangnya "+bld ,hasil_bmi)
							print(lr+sp)
							
							
							go_back=input(s+y+"Lagi ? (y/n) ")
							while go_back !="y" and go_back !="n":
									go_back=input(s+y+"Lagi ? (y/n) ")
							if go_back == "n":
									print("\n")
									print(s+lr+"Exiting the tool...\n")
									exit()
									
				#fungsi rumus					
				if sex=="co":
							r=male()
							output(r)
							menu()
				else:
							r=female()
							output(r)
							menu()
							
		#proses input
		elif usr_in =="2":
				print(lr+"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"+x)
				print(lg+"Alat Apa ini !?\n")
				print("BMI (Body Mass Index) atau index berat tubuh adalah\nNilai indeks yang menentukan apakah orang tersebut kurus, \nnormal gemuk atau obesitas.\nTimbang susah-susah, ini gw buatin alatnya. baik kan gw ?\n")
				print("Kenapa gw mbuat alat kaya begini ?\nYa suka-suka gw lah. kan gw yg buat >:(\nSebenernya krna gw LDR, dan gapernah tau apakah pacar gw kurus apa gimana, \njadi gw bikin ini biar tau gitu :'v\nLDR sedih mhankk :' Tapi gw setia :*\n")
				print("Btw Terimakasih banyak kepada Allah SWT,\nsemua member AICA, BlackHole Scurity, CRABS, dan PythonID :*")
				print(lr+"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"+x)
				go_back=input(y+s+"klik 0 !")
				while go_back !="0":
						go_back=input(s+y+"klik 0 !")
				menu()
				
				
		#proses input
		elif usr_in =="3":
				print(lr+"+++++++++++++++++++++]"+x,"Tentang Pengembang",lr+"[++++++++++++++++++++++\n"+x)
				print(lg+bld+"Karjok Pangesty"+x)
				print(lg+"Dulu pas kecil badannya kecil, dan setelah besar badannya besar")
				print("Nggak suka sama cowok")
				print("LDR 4 tahun, hmm.. kalo mau,")
				print("Hubungin aja https:/t.me/om_karjok\n")
				print(lr+"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"+x)
				go_back=input(s+y+"klik 0 ! ")
				while go_back !="0":
						go_back=input(y+s+"klik 0 ! ")
				menu()
				
		else:
				print("\n")
				print(s+lr+"Exiting the tool...\n")
				exit()
menu()
