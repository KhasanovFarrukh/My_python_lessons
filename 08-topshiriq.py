# 8-DARS. RO'YXATLAR BILAN ISHLASH

"""O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring"""
davlatlar = ['AQSH', 'Falastin', 'Rossiya', 'Misr', "BAA"]
print(davlatlar)
# Output: ['AQSH', 'Falastin', 'Rossiya', 'Misr', 'BAA']

"""Ro'yxatning uzunligini konsolga chiqaring"""
print(f"davlatlar ro\'yxatining uzunligi {len(davlatlar)} ga teng")
# Output: davlatlar ro'yxatining uzunligi 5 ga teng

"""sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring"""
print(sorted(davlatlar))
# Output: ['AQSH', 'BAA', 'Falastin', 'Misr', 'Rossiya']

"""sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring"""
print(sorted(davlatlar, reverse=True))
# Output: ['Rossiya', 'Misr', 'Falastin', 'BAA', 'AQSH']

"""Asl ro'yxatni qaytadan konsolga chiqaring"""
print(davlatlar)
# Output: ['AQSH', 'Falastin', 'Rossiya', 'Misr', 'BAA']

"""reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring"""
davlatlar.reverse()
print(davlatlar)
# Output: ['BAA', 'Misr', 'Rossiya', 'Falastin', 'AQSH']

"""sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring."""
davlatlar.sort()
print(davlatlar)
# Output: ['AQSH', 'BAA', 'Falastin', 'Misr', 'Rossiya']
davlatlar.sort(reverse=True)
print(davlatlar)
# Output: ['Rossiya', 'Misr', 'Falastin', 'BAA', 'AQSH'] 

"""120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing"""
juft = list(range(120, 1200, 2))
print(juft)
# Output: [120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164,
# 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 256, 258, 260, 262, 264, 266, 268, 270, 272, 274, 276, 278, 280, 282, 284, 286, 288, 290, 292, 294, 296, 298, 300, 302, 304, 306, 308, 310, 312, 314, 316, 318, 320, 322, 324, 326, 328, 330, 332, 334, 336, 338, 340, 342, 344, 346, 348, 350, 352, 354, 356, 358, 360, 362, 364, 366, 368, 370, 372, 374, 376, 378, 380, 382, 384, 386, 388, 390, 392, 394, 396,
# 398, 400, 402, 404, 406, 408, 410, 412, 414, 416, 418, 420, 422, 424, 426, 428, 430, 432, 434, 436, 438, 440, 442, 444, 446, 448, 450, 452, 454, 456, 458, 460, 462, 464, 466, 468, 470, 472, 474, 476, 478, 480, 482, 484, 486, 488, 490, 492, 494, 496, 498, 500, 502, 504, 506, 508, 510, 512, 514, 516, 518, 520, 522, 524, 526, 528, 530, 532, 534, 536, 538, 540, 542, 544, 546, 548, 550, 552, 554, 556, 558, 560, 562, 564, 566, 568, 570, 572, 574, 576, 578, 580, 582, 584, 586, 588, 590, 592, 594, 596, 598, 600, 602, 604, 606, 608, 610, 612, 614, 616, 618, 620, 622, 624, 626, 628,
# 630, 632, 634, 636, 638, 640, 642, 644, 646, 648, 650, 652, 654, 656, 658, 660, 662, 664, 666, 668, 670, 672, 674, 676, 678, 680, 682, 684, 686, 688, 690, 692, 694, 696, 698, 700, 702, 704, 706, 708, 710, 712, 714, 716, 718, 720, 722, 724, 726, 728, 730, 732, 734, 736, 738, 740, 742, 744, 746, 748, 750, 752, 754, 756, 758, 760, 762, 764, 766, 768, 770, 772, 774, 776, 778, 780, 782, 784, 786, 788, 790, 792, 794, 796, 798, 800, 802, 804, 806, 808, 810, 812, 814, 816, 818, 820, 822, 824, 826, 828, 830, 832, 834, 836, 838, 840, 842, 844, 846, 848, 850, 852, 854, 856, 858, 860,
# 862, 864, 866, 868, 870, 872, 874, 876, 878, 880, 882, 884, 886, 888, 890, 892, 894, 896, 898, 900, 902, 904, 906, 908, 910, 912, 914, 916, 918, 920, 922, 924, 926, 928, 930, 932, 934, 936, 938, 940, 942, 944, 946, 948, 950, 952, 954, 956, 958, 960, 962, 964, 966, 968, 970, 972, 974, 976, 978, 980, 982, 984, 986, 988, 990, 992, 994, 996, 998, 1000, 1002, 1004, 1006, 1008, 1010, 1012, 1014, 1016, 1018, 1020, 1022, 1024, 1026, 1028, 1030, 1032, 1034, 1036, 1038, 1040, 1042, 1044, 1046, 1048, 1050, 1052, 1054, 1056, 1058, 1060, 1062, 1064, 1066, 1068, 1070, 1072, 1074, 1076, 1078, 1080, 1082, 1084, 1086, 1088, 1090, 1092, 1094, 1096, 1098, 1100, 1102, 1104, 1106, 1108, 1110, 1112, 1114, 1116, 1118, 1120, 1122, 1124, 1126, 1128, 1130, 1132, 1134, 1136, 1138, 1140, 1142, 1144, 1146, 1148, 1150, 1152, 1154, 1156, 1158, 1160, 1162, 1164, 1166, 1168, 1170, 1172, 1174, 1176, 1178, 1180, 1182, 1184, 1186, 1188, 1190, 1192, 1194, 1196, 1198]

"""Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring"""
print(sum(juft))
# Output: 355860

"""Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring"""
print(max(juft) - min(juft))
# Output: 1078

"""Ro'yxatdagi elementlar sonini hisoblang"""
print(len(juft))
# Output: 540

"""Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring"""
print(f"Ro\'yxat boshidagi 20 ta son: {juft[:20]}")
print(f"Ro\'yxat o\'rtasidagi 20 ta son: {juft[270:291]}")
print(f"Ro\'yxat oxiridagi 20 ta son: {juft[521:]}")
# Output: Ro'yxat boshidagi 20 ta son: [120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158]
# Output: Ro'yxat o'rtasidagi 20 ta son: [660, 662, 664, 666, 668, 670, 672, 674, 676, 678, 680, 682, 684, 686, 688, 690, 692, 694, 696, 698, 700]
# Output: Ro'yxat oxiridagi 20 ta son: [1162, 1164, 1166, 1168, 1170, 1172, 1174, 1176, 1178, 1180, 1182, 1184, 1186, 1188, 1190, 1192, 1194, 1196, 1198]

"""Taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting"""
taomlar = ['manti', 'shashlik', 'qaymoq', 'sho\'rva', 'qovurilgan tuxum']
print(taomlar)
#Output: ['manti', 'shashlik', "qaymoq", "sho'rva", 'qovurilgan tuxum']

"""Nonushta degan yangi ro'yxatga taomlardan nusxa oling.
Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing"""
nonushta = taomlar[:]
nonushta.remove('manti')
nonushta.remove('shashlik')
nonushta.remove('sho\'rva')
nonushta.append('kolbasa')
nonushta.append('asal')
print(nonushta)
#Output: ['qaymoq', 'qovurilgan tuxum', 'kolbasa', 'asal']

"""Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring."""
nonushta = tuple(nonushta)
print(nonushta)
# Output: ('qaymoq', 'qovurilgan tuxum', 'kolbasa', 'asal')
nonushta[0] = 'qaymoq va non'
# Output: TypeError: 'tuple' object does not support item assignment