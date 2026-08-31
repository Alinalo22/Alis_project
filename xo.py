from random import randint

print('𝑛𝑎𝑚𝑒 𝑡ℎ𝑒 𝑔𝑎𝑚𝑒= ꧁ܥ‌‍‌‍‍وـز꧂ (𝑑𝑜𝑜𝑧)')

try:
	with open('game1xo.txt', 'r') as f:
		line1 =f.readline()
		line2 =f.readline()
		line3 =f.readline()
		line4 =f.readline()
		line5 =f.readline()
		line6 =f.readline()
		line7 =f.readline()
		coins=float(line1)
		pay=int(line2)
		win_player=int(line3)
		win_bot=int(line4)
		mosavi=int(line5)
		name1=line6
		shm=list(line7)
except:
	coins=0
	pay=0
	win_player=0
	win_bot=0
	mosavi=0
	shm=[]
	name1=input('P͟͟L͟͟A͟͟Y͟͟E͟͟R͟͟1 esmeto vared kon ')

a='1'
b='2'
c='3'
d='4'
e='5'
f='6'
g='7'
h='8'
i='9'
ai=0
cs='1'
pat=0
p='🟢'
o='❌'
li='maker : Ali inalo'
bn=[[a, b, c],[d, e, f],[g, h, i],[a, d, g],[b, e, h],[c, f, i],[a, e, i],[c, e, g]]
FS=['1','2','3','4','5','6','7','8','9']
print('')
while True:
	if ai==1:
		ai=0
		if pat==0:
			if botwiner==1:
				coins=coins-1
			elif botp=='1':
				coins=coins+.5
			elif botp=='2':
				coins=coins+1
			elif botp=='3':
				coins=coins+2
			elif botp=='4':
				coins=coins+3
		pat=0
		while True:
			print('______________________________________________________')
			print('1. new game▶️')
			print('2. shop 🛒')
			print('3. makers 👨‍💻')
			print('4. User Info👤')
			print('5. Help 🆘')
			print('6. exit🚪')
			cs=input('adad mored nazar ra vared konid?')
			if cs=='1':
				break
			if cs=='2':
				print('Welcome to shop🛒')
				print('itemi ke ghablan kharidari kardid baraye entekab poli az shoma kam nemishavad🫡')
				print('your coins🪙:',coins)
				print('''
🎨  Shapeshifting mark:
  1. 🟢  Green  →  0 coins
  2. ⭕  Red  →  0 coins
  3. ⭐  Star  →  3 coins
  4. ❤️  Heart   →  3 coins
  5. 🔥  Fire   →  5 coins
  6. 💎  Diamond  →  5 coins
  7. 🌟  Shining star  →  7 coins
  8. 👑  Crown   →  10 coins
''')
	
				shop = input('adad mored nazar ra vared konid🛍️')
	
				if shop == '1':
					p = '🟢'
					print('Your mark changed to 🟢!')
					
				elif shop == '2':
					p ='⭕'
					print('Your mark changed to ⭕!')
					
				elif shop == '3':
					if '1' in shm:
						p = '⭐'
						print('Your mark changed to ⭐!')
					elif coins - 3 >= 0:
						coins = coins - 3
						p = '⭐'
						shm.append('1')
						print('⭐ Done! ✅')
						pay=pay+3
					else:
						print('Not enough coins! 🤦🏻')
					
				elif shop == '4':
					if '2' in shm:
						p = '❤️'
						print('Your mark changed to ❤️!')
					elif coins - 3 >= 0:
						coins = coins - 3
						p = '❤️'
						shm.append('2')
						print('❤️ Done! ✅')
						pay=pay+3
					else:
						print('Not enough coins! 🤦🏻')
					
				elif shop == '5':
					if '3' in shm:
						p = '🔥'
						print('Your mark changed to 🔥!')
					elif coins - 5 >= 0:
						coins = coins - 5
						p = '🔥'
						shm.append('3')
						print('🔥 Done! ✅')
						pay=pay+5
					else:
						print('Not enough coins! 🤦🏻')
					
				elif shop == '6':
					if '4' in shm:
						p = '💎'
						print('Your mark changed to 💎!')
					elif coins - 5 >= 0:
						coins = coins - 5
						p = '💎'
						shm.append('4')
						print('💎 Done! ✅')
						pay=pay+5
					else:
						print('Not enough coins! 🤦🏻')
					
				elif shop == '7':
					if '5' in shm:
						p = '🌟'
						print('Your mark changed to 🌟!')
					elif coins - 7 >= 0:
						coins = coins - 7
						p = '🌟'
						shm.append('5')
						print('🌟 Done! ✅')
						pay=pay+7
					else:
						print('Not enough coins! 🤦🏻')
					
				elif shop == '8':
					if '6' in shm:
						p = '👑'
						print('Your mark changed to 👑!')
					elif coins - 10 >= 0:
						coins = coins - 10
						p = '👑'
						shm.append('6')
						print('👑 Done! ✅')
						pay=pay+10
					else:
						print('Not enough coins! 🤦🏻')
					
				else:
					print('Invalid number!')
				
			elif cs=='3':
				print('𝗠𝗮𝗸𝗲𝗿🧑🏽‍💻: 𓄂𝐀𝐥𝐢.𝐢𝐧𝐚𝐥𝐨')
				print('𝗛𝗲𝗹𝗽𝗲𝗿🆘: 𓅓𝐌𝐫.𝐌𝐚𝐣𝐥𝐞𝐬𝐢')
				print("""⚡Vizhegi haye Monhaser be Farde Bazi(ویژگی های منحصربفرد بازی)
1.تعداد خط های نسبتاً کم📝
2.بازی با ربات🤖
3.داشتن سه سطح دشواری برای ربات🧠
4.بازی دو نفره👥
5. شاپ و خرید انواع مهره از آن🛒
6.منوی کاربردی و مناسب📜
7.سیستم سکه🪙
""")
				
			elif cs=='4':
				gam=win_player+win_bot+mosavi
				if gam>0:
					winp=(int((win_player*100)/gam))
					winb=(int((win_bot*100)/gam))
					mosav=(int((mosavi*100)/gam))
				
				print('your name💳:',name1)
				print('𝘆𝗼𝘂𝗿 𝗰𝗼𝗶𝗻𝘀🪙:',coins)
				print('🏆 Wins:', win_player,f'{winp}%')
				print('🤖 Bot Wins:', win_bot,f'{winb}%')
				print('🤝 Draws:', mosavi,f'{mosav}%')
				print('📊 Total Games:', win_player + win_bot + mosavi)
				ww=input('mikhay esmet ro edit koni?')
				if ww=='آره' or ww=='بله' or ww=='yes' or ww=='are' or ww=='bale':
					ww=input('esm jadid ra wared kon: ')
					name1=ww
					print('esm jdid shoma sabt shod✅')
			elif cs=='5':
				print("""
🎯 هدف بازی:
-------------
هدف اصلی این بازی، قرار دادن ۳ علامت پشت سر هم در یک 
ردیف، ستون یا قطر است. هر بازیکن تلاش می‌کند که 
نسبت به حریف خود جلوتر باشد و بازی را ببرد.

🎮 نحوه بازی:
-------------
بازی روی یک صفحه ۳×۳ انجام می‌شود که هر خانه آن با 
اعداد ۱ تا ۹ شماره‌گذاری شده است. دو بازیکن به نوبت 
یکی از این خانه‌ها را با وارد کردن عدد مربوطه انتخاب 
کرده و علامت خود را در آن قرار می‌دهند. بازی به همین 
ترتیب ادامه پیدا می‌کند تا زمانی که یکی از بازیکنان 
برنده شود یا همه خانه‌ها پر شوند.

🤖 ربات‌ها:
-----------
این بازی دارای چندین سطح مختلف برای بازی با ربات 
است که هر کدام سبک بازی متفاوتی دارند:

• سطح easy   →  برنده شدن ۰.۵ سکه
• سطح normal →  برنده شدن ۱ سکه
• سطح Hard   →  برنده شدن ۲ سکه
• سطح iranmode → برنده شدن ۳ سکه

• باخت به هر کدام از این ربات‌ها = ۱ سکه منفی

هرچه سطح بالاتر باشد، ربات قدرتمندتر است و سکه
برنده شدن مقابل آن نیز بیشتر است.
بازی دو نفره هیچ سکه برای بازنده یا برنده ندارد
 برنده شدن:🏆
------------
برنده کسی است که بتواند اولین بار ۳ علامت خود را 
به صورت پشت سر هم در یکی از حالت‌های زیر قرار دهد:
- یک ردیف افقی
- یک ستون عمودی
- یک قطر

⚖️ تساوی:
---------
اگر تمام ۹ خانه صفحه پر شود و هیچ یک از بازیکنان 
نتوانسته باشد ۳ علامت پشت سر هم بچیند، بازی با 
نتیجه مساوی به پایان می‌رسد.

💡 نکات مهم:
------------
- هر خانه فقط یک بار قابل انتخاب است
- ورودی‌ها باید بین ۱ تا ۹ باشند
- در صورتی که خانه‌ای تکراری انتخاب شود، نوبت شما از دست می‌رود
- پس از پایان هر بازی، امکان شروع مجدد وجود دارد

🎮 شروع بازی:
-------------
پس از اجرای برنامه، مراحل زیر را دنبال کنید:
۱. انتخاب حالت بازی (تک‌نفره با ربات یا دو‌نفره)
۲. انتخاب سطح دشواری (در حالت تک‌نفره)
۳. وارد کردن نام بازیکنان
۴. شروع بازی و لذت بردن!

📞 پشتیبانی:
------------
در صورت مشاهده هرگونه باگ یا مشکل، لطفاً از طریق
آیدی زیر با ما در ارتباط باشید:

🆔 @lionpars

📍 این آیدی در پیام‌رسان‌های سروش و روبیکا فعال است.
""")
			
			elif cs=='6':
				with open('game1xo.txt', 'w') as f:
					f.write(f'{coins}\n')
					f.write(f'{pay}\n')
					f.write(f'{win_player}\n')
					f.write(f'{win_bot}\n')
					f.write(f'{mosavi}\n')
					f.write(f'{name1}\n')
					f.write(f'{shm}')
				print('𝗴𝗼𝗼𝗱𝗯𝗮𝘆👋🏽')
				exit()
	else:
		if cs=='1':
			a='1'
			b='2'
			c='3'
			d='4'
			e='5'
			f='6'
			g='7'
			h='8'
			i='9'
			botwiner=0
			
			bot=input('𝕞𝕚𝕜𝕙𝕒𝕪 𝕓𝕒𝕫𝕚 𝕕𝕠 𝕟𝕒𝕗𝕒𝕣𝕖 𝕓𝕖𝕣𝕚 𝕪𝕒 𝕓𝕒 𝕣𝕠𝕓𝕠𝕥?')
			if bot=='robot':
				print('1.𝙚𝙖𝙨𝙮 2.𝙣𝙤𝙧𝙢𝙖𝙡 3.𝙃𝙖𝙧𝙙 4.𝙞𝙧𝙖𝙣𝙢𝙤𝙙𝙚')
				botp=input('𝘼𝙙𝙖𝙙 𝙗𝙖𝙯𝙞 𝙢𝙤𝙧𝙚𝙙 𝙣𝙖𝙯𝙖𝙧𝙚𝙩𝙤 𝙬𝙖𝙧𝙚𝙙 𝙠𝙤𝙣')
			if bot!= 'robot':
				name2=input('P͟͟L͟͟A͟͟Y͟͟E͟͟R͟͟2 esmeto vared kon ')
				print(name2,'=',o)
			print(name1,'=',p)
			
			FS=['1','2','3','4','5','6','7','8','9']
	
			while True:
				print('┏━━━┳━━━┳━━━┓')
				print(f'┃ {a} ‌┃ {b}  ‌┃ {c} ‌┃')
				print('┣━━━╋━━━╋━━━┫')
				print(f'┃ {d} ┃  {e} ┃ {f} ‌┃')
				print('┣━━━╋━━━╋━━━┫')
				print(f'┃ {g} ┃ {h}  ┃ {i} ┃')
				print('┗━━━┻━━━┻━━━┛')
				#انتخاب عدد کاربر
				ap=input(f'{name1 } 𝐀𝐃𝐀𝐃 𝐕𝐀𝐑𝐄𝐃 𝐊𝐎𝐍 ')
				if ap==a:
					if a!='1':
						print(name1,'in adad ghablan entekhab shode')
					else:
						a=p
						FS[0] = 'Ali'
				
				elif ap==b:
					if b!='2':
						print(name1,'in adad ghablan entekhab shode')
					else:
						b=p
						FS[1] = 'Ali'
				
				elif ap=='3':
					if c!='3':
						print(name1,'in adad ghablan entekhab shode')
					else:
						c=p
						FS[2] = 'Ali'
				
				elif ap=='4':
					if d!='4':
						print(name1,'in adad ghablan entekhab shode')
					else:
						d=p
						FS[3] = 'Ali'
				
				elif ap=='5':
					if e!='5':
						print(name1,'in adad ghablan entekhab shode')
					else:
						e=p
						FS[4] = 'Ali'
				
				elif ap=='6':
					if f!='6':
						print(name1,'in adad ghajblan entekhab shode')
					else:
						f=p
						FS[5] = 'Ali'
				
				elif ap=='7':
					if g!='7':
						print(name1,'in adad ghablan entekhab shode')
					else:
						g=p
						FS[6] = 'Ali'
				
				elif ap=='8':
					if h!='8':
						print(name1,'in adad ghablan entekhab shode')
					else:
						h=p
						FS[7] = 'Ali'
				
				elif ap=='9':
					if i!='9':
						print(name1,'in adad ghablan entekhab shode')
					else:
						i=p
						FS[8] = 'Ali'
				
				if (a==p and b==p and c==p) or (a==p and d==p and g==p) or (a==p and e==p and i==p) or (c==p and f==p and i==p) or (c==p and e==p and g==p) or (i==p and h==p and g==p) or (d==p and e==p and f==p) or (b==p and e==p and h==p):
					print(f'{name1}{(p)} WƗNɆɌ👑🙌🏻')
					print('')
					print('┏━━━┳━━━┳━━━┓')
					print(f'┃ {a} ‌┃ {b}  ‌┃ {c} ‌┃')
					print('┣━━━╋━━━╋━━━┫')
					print(f'┃ {d} ┃  {e} ┃ {f} ‌┃')
					print('┣━━━╋━━━╋━━━┫')
					print(f'┃ {g} ┃ {h}  ┃ {i} ┃')
					print('┗━━━┻━━━┻━━━┛')
					ai=ai+1
					win_player=win_player+1
					break
				if a!='1' and b!='2' and c!='3' and d!='4' and e!='5' and f!='6' and g!='7' and h!='8' and i!='9':
					print('')
					print('[𝗯𝗮𝘇𝗶 𝗽𝗮𝘁 𝘀𝗵𝗼𝗱]🤜🏻🤛🏻')
					ai=ai+1
					pat=pat+1
					mosavi=mosavi+1
					break
				# ربات
				if bot == 'robot':
					if botp=='1':
						while True:
							botr = randint(0,8)
							if FS[botr] != 'Ali' and FS[botr] != 'bot' and FS[botr] != p and FS[botr] != o:
								if FS[botr] == '1':
									a = '❌'
								elif FS[botr] == '2':
									b = '❌'
								elif FS[botr] == '3':
									c = '❌'
								elif FS[botr] == '4':
									d = '❌'
								elif FS[botr] == '5':
									e = '❌'
								elif FS[botr] == '6':
									f ='❌'
								elif FS[botr] == '7':
									g ='❌'
								elif FS[botr] == '8':
									h = '❌'
								elif FS[botr] == '9':
									i = '❌'
								FS[botr] = 'bot'
								break
					
					if botp=='2':
						bn = [[a, b, c], [d, e, f], [g, h, i], [a, d, g], [b, e, h], [c, f, i], [a, e, i], [c, e, g]]
						li='maker : Ali inalo'
						#انتخاب عدد ربات برای دفاع↓
						for x in bn:
							if x[0]==p and x[1]==p and x[2] not in [p,'❌','Ali','bot']:
								li=x[2]
								break
							elif x[0]==p and x[2]==p and x[1] not in [p,'❌','Ali','bot']:
								li=x[1]
								break
							elif x[2]==p and x[1]==p and x[0] not in [p,'❌','Ali','bot']:
								li=x[0]
								break
								#پیدا کردن عددی که ربات برای دفاع انتخاب کرده↓
						if li!='maker : Ali inalo':
							if li=='1':
								a = '❌'
							elif li == '2':
								b = '❌'
							elif li == '3':
								c = '❌'
							elif li == '4':
								d = '❌'
							elif li == '5':
								e = '❌'
							elif li == '6':
								f = '❌'
							elif li == '7':
								g = '❌'
							elif li == '8':
								h = '❌'
							elif li == '9':
								i = '❌'
							FS[int(li)-1]='bot'
						elif a!='1' and b!='2' and c!='3' and d!='4' and e!='5' and f!='6' and g!='7' and h!='8' and i!='9':
							print('')
							print('[𝗯𝗮𝘇𝗶 𝗽𝗮𝘁 𝘀𝗵𝗼𝗱]🤜🏻🤛🏻')
							mosavi=mosavi+1
							pat=pat+1
							ai=ai+1
							break
						else:
							while True:
								botr = randint(0,8)
								if FS[botr] != 'Ali' and FS[botr] != 'bot' and FS[botr] != p and FS[botr] != '❌':
									if FS[botr] == '1':
										a = '❌'
									elif FS[botr] == '2':
										b = '❌'
									elif FS[botr] == '3':
										c = '❌'
									elif FS[botr] == '4':
										d = '❌'
									elif FS[botr] == '5':
										e = '❌'
									elif FS[botr] == '6':
										f = '❌'
									elif FS[botr] == '7':
										g = '❌'
									elif FS[botr] == '8':
										h = '❌'
									elif FS[botr] == '9':
										i = '❌'
									FS[botr] = 'bot'
									break
					
					if botp=='3':
						bn = [[a, b, c], [d, e, f], [g, h, i], [a, d, g], [b, e, h], [c, f, i], [a, e, i], [c, e, g]]
						lil='thanks for play my game'
						if a!='1' and b!='2' and c!='3' and d!='4' and e!='5' and f!='6' and g!='7' and h!='8' and i!='9':
							print('')
							print('[𝗯𝗮𝘇𝗶 𝗽𝗮𝘁 𝘀𝗵𝗼𝗱]🤜🏻🤛🏻')
							mosavi=mosavi+1
							pat=pat+1
							ai=ai+1
							break
						for x in bn:
							if x[0]==o and x[1]==o and x[2] not in [p,'❌','Ali','bot']:
								lil=x[2]
								break
							elif x[0]==o and x[2]==o and x[1] not in [p,'❌','Ali','bot']:
								lil=x[1]
								break
							elif x[2]==o and x[1]==o and x[0] not in [p,'❌','Ali','bot']:
								lil=x[0]
								break
								
						for x in bn:
							if x[0]==p and x[1]==p and x[2] not in [p,'❌','Ali','bot']:
								li=x[2]
								break
							elif x[0]==p and x[2]==p and x[1] not in [p,'❌','Ali','bot']:
								li=x[1]
								break
							elif x[2]==p and x[1]==p and x[0] not in [p,'❌','Ali','bot']:
								li=x[0]
								break
								
						if lil != 'thanks for play my game':
							if lil=='1':
								a = '❌'
							elif lil == '2':
								b = '❌'
							elif lil == '3':
								c = '❌'
							elif lil == '4':
								d = '❌'
							elif lil == '5':
								e = '❌'
							elif lil == '6':
								f = '❌'
							elif lil == '7':
								g = '❌'
							elif lil == '8':
								h = '❌'
							elif lil == '9':
								i = '❌'
							FS[int(lil)-1]='bot'
						elif li!='maker : Ali inalo':
							if li=='1':
								a = '❌'
								FS[0]='bot'
							elif li == '2':
								b = '❌'
								FS[1]='bot'
							elif li == '3':
								c = '❌'
								FS[2]='bot'
							elif li == '4':
								d = '❌'
								FS[3]='bot'
							elif li == '5':
								e = '❌'
								FS[4]='bot'
							elif li == '6':
								f = '❌'
								FS[5]='bot'
							elif li == '7':
								g = '❌'
								FS[6]='bot'
							elif li == '8':
								h = '❌'
								FS[7]='bot'
							elif li == '9':
								i = '❌'
								FS[8]='bot'
						else:
							while True:
								botr = randint(0,8)
								if FS[botr] != 'Ali' and FS[botr] != 'bot' and FS[botr] != p and FS[botr] != '❌':
									if FS[botr] == '1':
										a = '❌'
										FS[0]='bot'
									elif FS[botr] == '2':
										b = '❌'
										FS[1]='bot'
									elif FS[botr] == '3':
										c = '❌'
										FS[2]='bot'
									elif FS[botr] == '4':
										d = '❌'
										FS[3]='bot'
									elif FS[botr] == '5':
										e = '❌'
										FS[4]='bot'
									elif FS[botr] == '6':
										f = '❌'
										FS[5]='bot'
									elif FS[botr] == '7':
										g = '❌'
										FS[6]='bot'
									elif FS[botr] == '8':
										h = '❌'
										FS[7]='bot'
									elif FS[botr] == '9':
										i = '❌'
										FS[8]='bot'
									break
			
					if botp=='4':
						bn = [[a, b, c], [d, e, f], [g, h, i], [a, d, g], [b, e, h], [c, f, i], [a, e, i], [c, e, g]]
						lil='thanks for play my game'
						if a!='1' and b!='2' and c!='3' and d!='4' and e!='5' and f!='6' and g!='7' and h!='8' and i!='9':
							print('')
							print('[𝗯𝗮𝘇𝗶 𝗽𝗮𝘁 𝘀𝗵𝗼𝗱]🤜🏻🤛🏻')
							pat=pat+1
							mosavi=mosavi+1
							ai=ai+1
							break
						for x in bn:
							if x[0]==o and x[1]==o and x[2] not in [p,'❌','Ali','bot']:
								lil=x[2]
								break
							elif x[0]==o and x[2]==o and x[1] not in [p,'❌','Ali','bot']:
								lil=x[1]
								break
							elif x[2]==o and x[1]==o and x[0] not in [p,'❌','Ali','bot']:
								lil=x[0]
								break
						
						li = 'maker : Ali inalo'
						for x in bn:
							if x[0]==p and x[1]==p and x[2] not in [p,'❌','Ali','bot']:
								li=x[2]
								break
							elif x[0]==p and x[2]==p and x[1] not in [p,'❌','Ali','bot']:
								li=x[1]
								break
							elif x[2]==p and x[1]==p and x[0] not in [p,'❌','Ali','bot']:
								li=x[0]
								break
						
						if lil != 'thanks for play my game':
							if lil=='1':
								a = '❌'
								FS[0]='bot'
							elif lil == '2':
								b = '❌'
								FS[1]='bot'
							elif lil == '3':
								c = '❌'
								FS[2]='bot'
							elif lil == '4':
								d = '❌'
								FS[3]='bot'
							elif lil == '5':
								e = '❌'
								FS[4]='bot'
							elif lil == '6':
								f = '❌'
								FS[5]='bot'
							elif lil == '7':
								g = '❌'
								FS[6]='bot'
							elif lil == '8':
								h = '❌'
								FS[7]='bot'
							elif lil == '9':
								i = '❌'
								FS[8]='bot'
						elif li != 'maker : Ali inalo':
							if li=='1':
								a = '❌'
								FS[0]='bot'
							elif li == '2':
								b = '❌'
								FS[1]='bot'
							elif li == '3':
								c = '❌'
								FS[2]='bot'
							elif li == '4':
								d = '❌'
								FS[3]='bot'
							elif li == '5':
								e = '❌'
								FS[4]='bot'
							elif li == '6':
								f = '❌'
								FS[5]='bot'
							elif li == '7':
								g = '❌'
								FS[6]='bot'
							elif li == '8':
								h = '❌'
								FS[7]='bot'
							elif li == '9':
								i = '❌'
								FS[8]='bot'
						else:
							if e == '5':
								e = '❌'
								FS[4] = 'bot'
							elif a == '1':
								a = '❌'
								FS[0] = 'bot'
							elif c == '3':
								c = '❌'
								FS[2] = 'bot'
							elif g == '7':
								g = '❌'
								FS[6] = 'bot'
							elif i == '9':
								i = '❌'
								FS[8] = 'bot'
							else:
								while True:
									botr = randint(0, 3)
									if botr == 0 and b == '2':
										b = '❌'
										FS[1] = 'bot'
										break
									elif botr == 1 and d == '4':
										d = '❌'
										FS[3] = 'bot'
										break
									elif botr == 2 and f == '6':
										f = '❌'
										FS[5] = 'bot'
										break
									elif botr == 3 and h == '8':
										h = '❌'
										FS[7] = 'bot'
										break
					if (a==p and b==p and c==p) or (a==p and d==p and g==p) or (a==p and e==p and i==p) or (c==p and f==p and i==p) or (c==p and e==p and g==p) or (i==p and h==p and g==p) or (d==p and e==p and f==p) or (b==p and e==p and h==p):
						print('┏━━━┳━━━┳━━━┓')
						print(f'┃ {a} ‌┃ {b}  ‌┃ {c} ‌┃')
						print('┣━━━╋━━━╋━━━┫')
						print(f'┃ {d} ┃  {e} ┃ {f} ‌┃')
						print('┣━━━╋━━━╋━━━┫')
						print(f'┃ {g} ┃ {h}  ┃ {i} ┃')
						print('┗━━━┻━━━┻━━━┛')
						print('')
						print(f'{name1}{(p)} WƗNɆɌ👑🙌🏻')
						ai=ai+1
						win_player=win_player+1
						break
					if (a==o and b==o and c==o) or (a==o and d==o and g==o) or (a==o and e==o and i==o) or (c==o and f==o and i==o) or (c==o and e==o and g==o) or (i==o and h==o and g==o) or (d==o and e==o and f==o) or (b==o and e==o and h==o):
						print('┏━━━┳━━━┳━━━┓')
						print(f'┃ {a} ‌┃ {b}  ‌┃ {c} ‌┃')
						print('┣━━━╋━━━╋━━━┫')
						print(f'┃ {d} ┃  {e} ┃ {f} ‌┃')
						print('┣━━━╋━━━╋━━━┫')
						print(f'┃ {g} ┃ {h}  ┃ {i} ┃')
						print('┗━━━┻━━━┻━━━┛')
						print('🤖 ẄЇṄṄЁṚ🥇')
						botwiner=botwiner+1
						ai=ai+1
						win_bot=win_bot+1
						break