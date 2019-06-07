import vk_api
import time
#import random
#import datetime

login, passw = "", ""https://github.com/dshedr/countbot/blob/master/print_via_console
def main(t):
	lm,rm,cm = 0, 0, 0 #Sea-ness
	lx,rx,cx = 0, 0, 0 #Crystal-ish
	ll,rl,cl = 0, 0, 0 #Azure-ish
	ly,ry,cy = 0, 0, 0 #Amber-ish
	lk,rk,ck = 0, 0, 0 #Cypress-ish
	lr,rr,cr = 0, 0, 0 #River-ish
	lp,rp,cp = 0, 0, 0 #Field-ish
	lo,ro,co = 0, 0, 0 #Lake-ish
	k, k1, k2, k3, k4 = 0, 0, 0, 0
	k5, k6, k7 = 0, 0, 0
	session = vk_api.VkApi(login, passw)
	session.auth(token_only = True)
	vk = session.get_api()
	data = vk.wall.get(owner_id=-44235988, count=50)
	for i in data['items']:
		for j in i['text']:
			if (j == '#relatedmedia'):
				lm += i['likes']['count']
				rm += i['reposts']['count']
				cm += i['comments']['count']
				k += 1
			if (j == '#followpushkin'):
				lx += i['likes']['count']
				rx += i['reposts']['count']
				cx += i['comments']['count']
				k1 += 1
			if (j == '#redbosses'):
				ll += i['likes']['count']
				rl += i['reposts']['count']
				cl += i['comments']['count']
				k2 += 1
			if (j == '#com.media'):
				ly += i['likes']['count']
				ry += i['reposts']['count']
				cy += i['comments']['count']
				k3 += 1
			if (j == '#media_republic'):
				lk += i['likes']['count']
				rk += i['reposts']['count']
				ck += i['comments']['count']
				k4 += 1
			if (j == '#5на200'):
				lr += i['likes']['count']
				rr += i['reposts']['count']
				cr += i['comments']['count']
				k5 += 1
			if (j == '#в_поле_медиа'):
				lp += i['likes']['count']
				rp += i['reposts']['count']
				cp += i['comments']['count']
				k6 += 1
			if (j == '#LTE'):
				lp += i['likes']['count']
				rp += i['reposts']['count']
				cp += i['comments']['count']
				k7 += 1
	print("Подсчёт #"+str(t)+"<br>")
	print("МОРСКОЙ<br>")
	print("Постов: "+str(k)+"<br>" )
	print(("Лайков = "+str(lm))+"<br>" )
	print(("Репостов = "+str(rm))+"<br>")
	print(("Комментариев = "+str(cm))+"<br>" )
	print(("ХРУСТАЛЬНЫЙ<br>")+"<br>")
	print("Постов: "+str(k1)+"<br>")
	print(("Лайков = "+str(lx))+"<br>" )
	print(("Репостов = "+str(rx))+"<br>" )
	print(("Комментариев = "+str(cx))+"<br>")
	print(("ЛАЗУРНЫЙ<br>")+"<br>" )
	print("Постов: "+str(k2)+"<br>")
	print(("Лайков = "+str(ll))+"<br>")
	print(("Репостов = "+str(rl))+"<br>")
	print(("Комментариев = "+str(cl))+"<br>")
	print(("КИПАРИСНЫЙ<br>")+"<br>")
	print("Постов: "+str(k4)+"<br>")
	print(("Лайков = "+str(lk))+"<br>")
	print(("Репостов = "+str(rk))+"<br>")
	print(("Комментариев = "+str(ck))+"<br>" )
	print(("ПОЛЕВОЙ<br>")+"<br>")
	print("Постов: "+str(k6)+"<br>")
	print(("Лайков = "+str(lp))+"<br>")
	print(("Репостов = "+str(rp))+"<br>")
	print(("Комментариев = "+str(cp))+"<br>")
	print(("ОЗЕРНЫЙ<br>")+"<br>")
	print("Постов: "+str(k7)+"<br>")
	print(("Лайков = "+str(lo))+"<br>")
	print(("Репостов = "+str(ro))+"<br>")
	print(("Комментариев = "+str(co))+"<br>")
	"""
	txt = "Подсчёт #"+str(t)+"<br>"
	txt += "МОРСКОЙ<br>"
	txt += "Постов: "+str(k)+"<br>"
	txt += ("Лайков = "+str(lm))+"<br>"
	txt += ("Репостов = "+str(rm))+"<br>"
	txt += ("Комментариев = "+str(cm))+"<br>"
	txt += ("ХРУСТАЛЬНЫЙ<br>")+"<br>"
	txt += "Постов: "+str(k1)+"<br>"
	txt += ("Лайков = "+str(lx))+"<br>"
	txt += ("Репостов = "+str(rx))+"<br>"
	txt += ("Комментариев = "+str(cx))+"<br>"
	txt += ("ЛАЗУРНЫЙ<br>")+"<br>"
	txt += "Постов: "+str(k2)+"<br>"
	txt += ("Лайков = "+str(ll))+"<br>"
	txt += ("Репостов = "+str(rl))+"<br>"
	txt += ("Комментариев = "+str(cl))+"<br>"
	txt += ("ЯНТАРНЫЙ<br>")+"<br>"
	txt += "Постов: "+str(k3)+"<br>"
	txt += ("Лайков = "+str(ly))+"<br>"
	txt += ("Репостов = "+str(ry))+"<br>"
	txt += ("Комментариев = "+str(cy))+"<br>"
	txt += ("КИПАРИСНЫЙ<br>")+"<br>"
	txt += "Постов: "+str(k4)+"<br>"
	txt += ("Лайков = "+str(lk))+"<br>"
	txt += ("Репостов = "+str(rk))+"<br>"
	txt += ("Комментариев = "+str(ck))+"<br>"
	txt += ("РЕЧНОЙ<br>")+"<br>"
	txt += "Постов: "+str(k5)+"<br>"
	txt += ("Лайков = "+str(lr))+"<br>"
	txt += ("Репостов = "+str(rr))+"<br>"
	txt += ("Комментариев = "+str(cr))+"<br>"
	txt += ("ПОЛЕВОЙ<br>")+"<br>"
	txt += "Постов: "+str(k6)+"<br>"
	txt += ("Лайков = "+str(lp))+"<br>"
	txt += ("Репостов = "+str(rp))+"<br>"
	txt += ("Комментариев = "+str(cp))+"<br>"
	txt += ("ОЗЕРНЫЙ<br>")+"<br>"
	txt += "Постов: "+str(k7)+"<br>"
	txt += ("Лайков = "+str(lo))+"<br>"
	txt += ("Репостов = "+str(ro))+"<br>"
	txt += ("Комментариев = "+str(co))+"<br>"
	#txt += "Время подсчёта: "+str(datetime.datetime.now())
	print(txt)
	random.seed()
	vk.messages.send(user_id=180757524,peer_id=2000000202,chat_id=202,message=txt,random_id=random.randint(1,999999))
	"""

	t = 0
	while(True):
		main(t)
		t += 1
		time.sleep(300)
