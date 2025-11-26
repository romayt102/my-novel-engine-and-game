import pygame
pygame.init()
def get_font(size):
	return pygame.font.Font("fonts/font.ttf", size)

# позиции по y 860; 890; 920; 950; 980; 1010; 1040;
# тексты персоонажей
slavya_text = get_font(40).render("Славия", True, "Yellow")
slavya_rect = (50,820)

dreamgirl_text = get_font(40).render("...", True, "White")
dreamgirl_rect = (50,820)

semyon_text = get_font(40).render("Семён", True, "LightGreen")
semyon_rect = (50,820)

# тексты слайдов
slayd_none_text = get_font(25).render("", True, "White")
slayd_none_rect = (50,860)

slayd_1_text_1 = get_font(25).render("Мне опять снился сон.", True, "White")
slayd_1_rect_1 = (50,860)

slayd_2_text_1 = get_font(25).render("Этот сон...", True, "White")
slayd_2_rect_1 = (50,860)

slayd_3_text_1 = get_font(25).render("Каждую ночь одно и то же.", True, "White")
slayd_3_rect_1 = (50,860)

slayd_4_text_1 = get_font(25).render("Но наутро, как обычно, всё забудется.", True, "White")
slayd_4_rect_1 = (50,860)

slayd_5_text_1 = get_font(25).render("Может быть, оно и к лучшему...", True, "White")
slayd_5_rect_1 = (50,860)

slayd_6_text_1 = get_font(25).render("Останутся только туманные воспоминания о приоткрытых, словно приглашающих куда-то воротах, рядом с которыми в камне застыли ", True, "White")
slayd_6_rect_1 = (50,860)

slayd_6_text_2 = get_font(25).render("два пионера.", True, "White")
slayd_6_rect_2 = (50,890)

slayd_7_text_1 = get_font(25).render("А ещё странная девочка... которая постоянно спрашивает:", True, "White")
slayd_7_rect_1 = (50,860)

slayd_8_text_1 = get_font(25).render("Ты пойдёшь со мной?", True, "White")
slayd_8_rect_1 = (50,860)

slayd_9_text_1 = get_font(25).render("Пойду?...", True, "White")
slayd_9_rect_1 = (50,860)

slayd_10_text_1 = get_font(25).render("Но куда?", True, "White")
slayd_10_rect_1 = (50,860)

slayd_11_text_1 = get_font(25).render("И зачем?..", True, "White")
slayd_11_rect_1 = (50,860)

slayd_12_text_1 = get_font(25).render("Да и где я вообще нахожусь?", True, "White")
slayd_12_rect_1 = (50,860)

slayd_13_text_1 = get_font(25).render("Конечно, случись всё на самом деле, наяву, стоило бы непременно испугаться.", True, "White")
slayd_13_rect_1 = (50,860)

slayd_14_text_1 = get_font(25).render("Как же иначе!", True, "White")
slayd_14_rect_1 = (50,860)

slayd_15_text_1 = get_font(25).render("Но это – всего лишь сон. Тот самый, который я вижу каждую ночь.", True, "White")
slayd_15_rect_1 = (50,860)

slayd_16_text_1 = get_font(25).render("А ведь всё это неспроста!", True, "White")
slayd_16_rect_1 = (50,860)

slayd_17_text_1 = get_font(25).render("Необязательно знать где и почему, чтобы понять – что-то происходит.", True, "White")
slayd_17_rect_1 = (50,860)

slayd_18_text_1 = get_font(25).render("Нечто, отчаянно требующее моего внимания.", True, "White")
slayd_18_rect_1 = (50,860)

slayd_19_text_1 = get_font(25).render("Ведь всё окружающее меня здесь – реально!", True, "White")
slayd_19_rect_1 = (50,860)

slayd_20_text_1 = get_font(25).render("Реально настолько, насколько реальны вещи в моей квартире; я бы мог открыть ворота, услышать скрип петель, смахнуть рукой", True, "White")
slayd_20_rect_1 = (50,860)

slayd_20_text_2 = get_font(25).render("осыпающуюся ржавчину, потянуть носом свежий прохладный воздух и поёжиться от холода.", True, "White")
slayd_20_rect_2 = (50,890)

slayd_21_text_1 = get_font(25).render("Мог бы, но для этого надо сдвинуться с места, сделать шаг, пошевелить рукой...", True, "White")
slayd_21_rect_1 = (50,860)

slayd_22_text_1 = get_font(25).render("А ведь это сон – я понимаю, но что дальше, что изменит моё понимание?", True, "White")
slayd_22_rect_1 = (50,860)

slayd_23_text_1 = get_font(25).render("Ведь здесь – словно по ту сторону потрескавшегося экрана старого телевизора, который из последних сил борется с помехами ", True, "White")
slayd_23_rect_1 = (50,860)

slayd_23_text_2 = get_font(25).render("и силится показать зрителям всё, не упустив ни малейшей детали.", True, "White")
slayd_23_rect_2 = (50,890)

slayd_24_text_1 = get_font(25).render("Но вот картинка теряет чёткость... Наверное, скоро просыпаться.", True, "White")
slayd_24_rect_1 = (50,860)

slayd_25_text_1 = get_font(25).render("Может быть, спросить у неё что-то? У девочки.", True, "White")
slayd_25_rect_1 = (50,860)

slayd_26_text_1 = get_font(25).render("Как же её зовут...", True, "White")
slayd_26_rect_1 = (50,850)

slayd_27_text_1 = get_font(25).render("Например про звёзды...", True, "White")
slayd_27_rect_1 = (50,860)

slayd_28_text_1 = get_font(25).render("Хотя почему про звёзды?", True, "White")
slayd_28_rect_1 = (50,860)

slayd_29_text_1 = get_font(25).render("Можно же спросить про ворота! Да, про ворота!", True, "White")
slayd_29_rect_1 = (50,860)

slayd_30_text_1 = get_font(25).render("Вот она удивится.", True, "White")
slayd_30_rect_1 = (50,860)

slayd_31_text_1 = get_font(25).render("Или лучше про букву ё.", True, "White")
slayd_31_rect_1 = (50,860)

slayd_32_text_1 = get_font(25).render("Хорошая была буква...", True, "White")
slayd_32_rect_1 = (50,860)

slayd_33_text_1 = get_font(25).render("Как будто её больше нет!", True, "White")
slayd_33_rect_1 = (50,860)

slayd_34_text_1 = get_font(25).render("И какое отношение буквы, ворота и звёзды имеют к этому месту?", True, "White")
slayd_34_rect_1 = (50,860)

slayd_35_text_1 = get_font(25).render("Ведь если мне каждую ночь снится этот сон, который потом всё равно забудется, надо искать разгадку здесь и сейчас!", True, "White")
slayd_35_rect_1 = (50,890)

slayd_36_text_1 = get_font(25).render("А вот, если присмотреться, можно увидеть Магелланово Облако...", True, "White")
slayd_36_rect_1 = (50,860)

slayd_37_text_1 = get_font(25).render("Словно попал в южное полушарие!", True, "White")
slayd_37_rect_1 = (50,860)
