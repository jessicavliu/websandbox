from ProductDataSet import ProductDataSet
from CategoryDataSet import CategoryDataSet

tbl_header = "wp_2"
catset = CategoryDataSet(tbl_header)
prodset = ProductDataSet(tbl_header)

#Selling colors

#----
#INSERT

#1)insert cat pink - success
'''name = "pink"
description = "X11 pinks"
catset.insert_category(name, description, parent = 0)'''


#2)insert prod pink under cat pink - success
#prodset.insert_product(title = "pink", content = "FFC0CB", cat_name = "pink")


#3)insert all other prod pinks - success
'''prodset.insert_product(title = "light pink", content = "FFC0CB", cat_name = "pink")
prodset.insert_product(title = "hot pink", content = "FFB6C1", cat_name = "pink")
prodset.insert_product(title = "deep pink", content = "FF69B4", cat_name = "pink")
prodset.insert_product(title = "pale violet red", content = "DB7093", cat_name = "pink")
prodset.insert_product(title = "medium violet red", content = "C71585", cat_name = "pink")'''


#4)insert all cats except for blue and cyan
'''catset.insert_category("green", "X11 greens", parent = 0)
catset.insert_category("purple/violet/magenta", "X11 purples/violets/magentas", parent = 0)
catset.insert_category("red", "X11 reds", parent = 0)
catset.insert_category("orange", "X11 oranges", parent = 0)
catset.insert_category("yellow", "X11 yellows", parent = 0)
catset.insert_category("white", "X11 whites", parent = 0)
catset.insert_category("brown", "X11 browns", parent = 0)
catset.insert_category("gray/black", "X11 grays/blacks", parent = 0)'''


#5)update product 1st pink by inserting productmeta

#yep this should definitely be a product attribute. rip oop
meta_dict = prodset.set_productmeta_dict(_wp_page_template = "default", _wc_review_count = "0", _wc_rating_count = "a:0:{}", _wc_average_rating = "0", _edit_lock = "", _edit_last = "", _sku = "", _regular_price = "", _sale_price = "", _sale_price_dates_from = "", _sale_price_dates_to = "", total_sales = 0, _tax_status = "taxable", _tax_class = "", _manage_stock = "no", _backorders = "no", _sold_individually = "no", _weight = "", _length = "", _width = "", _height = "", _upsell_ids = "a:0:{}", _crosssell_ids = "a:0:{}", _purchase_note = "", _default_attributes = "a:0:{}", _virtual = "no", _downloadable = "no", _product_image_gallery = "", _download_limit = "-1", _download_expiry = "-1", _stock = None, _stock_status = "instock", _product_version = "3.0.9", _price = "") 

#prodset.insert_product_meta("pink", meta_dict)


#6)update remaining pinks by inserting productmeta
#used same meta_dict
'''prodset.insert_product_meta("light pink", meta_dict)
prodset.insert_product_meta("hot pink", meta_dict)
prodset.insert_product_meta("deep pink", meta_dict)
prodset.insert_product_meta("pale violet red", meta_dict)
prodset.insert_product_meta("medium violet red", meta_dict)'''

#intermission) make product and cat objects first. the level of code that's mushing together in insertprod() makes me sad

#7)insert all prod colors and their metadata except for blue and cyan
#green

#8)insert blue and cyan

#9)insert prods for blue and cyan 
