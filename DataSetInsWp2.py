import CatProdExcelReader as cpxlrd

from ProductDataSet import ProductDataSet
from CategoryDataSet import CategoryDataSet

from Product import Product
from Category import Category

tbl_header = "wp_2"
catset = CategoryDataSet(tbl_header)
prodset = ProductDataSet(tbl_header)

#Selling colors
#METHODS

def mass_insert_cats(cat_dict): 
	for c in cat_dict:
		catset.insert_category(cat_dict[c])

def mass_insert_prods(prod_dict): 
	for p in prod_dict:
		prodset.insert_product(prod_dict[p])

def mass_delete_cats(cat_dict):
	for c in cat_dict:
		catset.delete_cat(cat_dict[c])

def mass_delete_prods(prod_dict):
	for p in prod_dict:
		prodset.delete_product(prod_dict[p])

#---
#INSERT

path = "/Users/jessicaliu/Dropbox (MIT)/mit/classes/2016/1Summer/EIT UROP/websandbox/sample-prods.xlsx"
cat_dict = cpxlrd.get_cat_dict_from_cells(path, 1, 2, 12)
prod_dict = cpxlrd.get_prod_dict_from_cells(path, 2, 2, 141, cat_dict)

#updating product meta for length
for p in prod_dict:
	prod_dict[p].set_product_meta_dict({"_length":len(prod_dict[p].title)})

#mass_insert_cats(cat_dict)
#mass_insert_prods(prod_dict)

#mass_delete_prods(prod_dict)
#mass_delete_cats(cat_dict)

#------

#for c in cat_dict:
	#catset.insert_category(cat_dict[c])

#for p in prod_dict:
	#prodset.insert_product(prod_dict[p])
	#prodset.delete_product(prod_dict[p])