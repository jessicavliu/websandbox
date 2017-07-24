from ProductDataSet import ProductDataSet
from CategoryDataSet import CategoryDataSet

from Product import Product
from Category import Category

tbl_header = "wp_2"
catset = CategoryDataSet(tbl_header)
prodset = ProductDataSet(tbl_header)

#Selling colors

#----
#INSERT

#---
#testing how to make parent cats work so I can figure out how products with parent cats work:P 
'''c1 = Category("salmon", "salmon desc", None)
c2 = Category("pale salmon", "pale salmon desc", c1)
catset.insert_category(c1)
catset.insert_category(c2)'''

#testing whether Product works
'''p1 = Product(title = "cod", content = "only good in korean soup", parent_category = None)
p2 = Product(title = "salmon fish", content = "a fish", parent_category = c1)
p3 = Product(title = "salmon sushi", content = "more prettily packaged salmon fish", parent_category = c1)
p4 = Product(title = "salmon roe", content = "even though i think it is comparable to the color of salmon fish, if not darker", parent_category = c2)

prodset.insert_product(p1)
prodset.insert_product(p2)
prodset.insert_product(p3)
print(prodset.insert_product(p4))'''
#---

#1)insert cat pink - success
c_pink = Category("pink", "X11 pinks", None)
#catset.insert_category(c_pink)

#2)insert prod pink under cat pink - success
p_pink = Product(title = "pink", content = "FFC0CB", parent_category = c_pink)
#prodset.insert_product(p_pink)


#3)insert all other prod pinks - success
#TODO:create fn to mass insert products
p_lightpink = Product(title = "light pink", content = "FFC0CB", parent_category = c_pink)
p_hotpink = Product(title = "hot pink", content = "FFB6C1", parent_category = c_pink)
p_deeppink = Product(title = "deep pink", content = "FF69B4", parent_category = c_pink)
p_palevioletred = Product(title = "pale violet red", content = "DB7093", parent_category = c_pink)
p_mediumvioletred = Product(title = "medium violet red", content = "C71585", parent_category = c_pink)

'''prodset.insert_product(p_lightpink)
prodset.insert_product(p_hotpink)
prodset.insert_product(p_deeppink)
prodset.insert_product(p_palevioletred)
prodset.insert_product(p_mediumvioletred)'''

#4)insert all cats except for blue and cyan
def mass_insert_cats(cat_list): #having var names is absolutely necessary here. I need to reference the Category objects for product parents. 
	for c in cat_list:
		catset.insert_category(c)

c_green = Category("green", "X11 greens", None)
c_purple = Category("purple/violet/magenta", "X11 purples/violets/magentas", None)
c_red = Category("red", "X11 reds", None)
c_orange = Category("orange", "X11 oranges", None)
c_yellow = Category("yellow", "X11 yellows", None)
c_white = Category("white", "X11 whites", None)
c_brown = Category("brown", "X11 browns", None)
c_grayblack = Category("gray/black", "X11 grays/blacks", None)
cat_list = [c_green, c_purple, c_red, c_orange, c_yellow, c_white, c_brown, c_grayblack]

#mass_insert_cats(cat_list)

#5)insert green prods
def mass_insert_prods(prod_list): #I don't know if it's imperative to have prod var names. 
	for p in prod_list:
		prodset.insert_product(p)
#20
p_darkolivegreen = Product("dark olive green", "556B2F", c_green)
p_olive = Product("olive", "808000", c_green)
p_olivedrab = Product("olive drab", "6B8E23", c_green)
p_yellowgreen = Product("yellow green", "9ACD32", c_green)
p_limegreen = Product("lime green", "32CD32", c_green)
p_lime = Product("lime", "00FF00", c_green)
p_lawngreen = Product("lawn green",	"7CFC00", c_green)
p_chartreuse = Product("chartreuse", "7FFF00", c_green)
p_greenyellow = Product("green yellow", "ADFF2F", c_green)
p_springgreen = Product("spring green", "00FF7F", c_green)
p_mediumspringgreen = Product("medium spring green", "00FA9A", c_green)
p_lightgreen = Product("light green", "90EE90", c_green)
p_palegreen = Product("pale green", "98FB98", c_green)
p_darkseagreen = Product("dark sea green", "8FBC8F", c_green)
p_mediumaquamarine = Product("medium aquamarine", "66CDAA", c_green)
p_mediumseagreen = Product("medium sea green", "3CB371", c_green)
p_seagreen = Product("sea green","2E8B57", c_green)
p_forestgreen = Product("forest green", "228B22", c_green)
p_green = Product("green", "008000", c_green)
p_darkgreen = Product("dark green", "006400", c_green)

prod_list = [p_darkolivegreen, p_olive, p_olivedrab, p_yellowgreen, p_limegreen, p_lime, p_lawngreen, p_chartreuse, p_greenyellow, p_springgreen, p_mediumspringgreen, p_lightgreen, p_palegreen, p_darkseagreen, p_mediumaquamarine, p_mediumseagreen, p_seagreen, p_forestgreen, p_green, p_darkgreen]

#mass_insert_prods(prod_list)

#6)insert blue and cyan
c_blue = Category("blue", "X11 blues", None)
c_cyan = Category("cyan", "X11 cyans", c_blue)

cat_list = [c_blue, c_cyan]
#mass_insert_cats(cat_list)

#7)insert prods for blue and cyan 
#15 prods
p_lightsteelblue = Product("light steel blue", "B0C4DE", c_blue)
p_powderblue = Product("powder blue", "B0E0E6", c_blue)
p_lightblue = Product("light blue", "AD D8 E6", c_blue)	
p_skyblue = Product("sky blue", "87 CE EB", c_blue)
p_lightskyblue=Product("light sky blue", "87 CE FA", c_blue)	
p_deepskyblue=Product("deep sky blue", "00 BF FF", c_blue)
p_dodgerblue = Product("dodger blue", "1E 90 FF", c_blue)
p_cornflowerblue = Product("corn flower blue", "64 95 ED", c_blue)	
p_steelblue=Product("steel blue", "46 82 B4", c_blue)
p_royalblue = Product("royal blue", "41 69 E1", c_blue)
p_blue = Product("blue", "00 00 FF", c_blue)
p_mediumblue = Product("medium blue", "00 00 CD", c_blue)  
p_darkblue = Product("dark blue", "00 00 8B", c_blue)
p_navy = Product("navy", "00 00 80", c_blue)
p_midnightblue = Product("midnight blue", "19 19 70", c_blue)	 

prod_list_blue = [p_lightsteelblue, p_powderblue, p_lightblue, p_skyblue, p_lightskyblue, p_deepskyblue, p_dodgerblue, p_cornflowerblue, p_steelblue, p_royalblue, p_blue, p_mediumblue, p_darkblue, p_navy, p_midnightblue]

#mass_insert_prods(prod_list_blue)

#12 prods
p_aqua = Product("aqua", "00FFFF", c_cyan)	  
p_cyan = Product("cyan", "00FFFF", c_cyan) 
p_lightcyan = Product("light cyan", "E0FFFF", c_cyan)
p_paleturquoise = Product("pale turquoise", "AFEEEE", c_cyan)
p_aquamarine = Product("aquamarine", "7FFFD4", c_cyan)
p_turquoise = Product("turquoise", "40E0D0", c_cyan)
p_mediumturquoise = Product("medium turquoise", "48D1CC", c_cyan)
p_darkturquoise = Product("dark turquoise", "00CED1", c_cyan)
p_lightseagreen = Product("light sea green", "20B2AA", c_cyan)
p_cadetblue = Product("cadet blue", "5F9EA0", c_cyan)
p_darkcyan = Product("dark cyan", "008B8B", c_cyan)
p_teal = Product("teal", "008080", c_cyan)

prod_list_cyan = [p_aqua, p_cyan, p_lightcyan, p_paleturquoise, p_aquamarine, p_turquoise, p_mediumturquoise, p_darkturquoise, p_lightseagreen, p_cadetblue, p_darkcyan, p_teal]

#mass_insert_prods(prod_list_cyan)

#np = no parent. this isn't .006 =__=
c_del_np = Category("deletable", "deletable, no parent", None)
c_del_p = Category("deletable", "deletable, has parent", c_pink)
#catset.insert_category(c_del_np)
#catset.insert_category(c_del_p)
#catset.delete_cat(c_del_np)
catset.delete_cat(c_del_p)
