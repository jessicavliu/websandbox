#!/usr/bin/python

#SOME NOTES ABOUT STRUCTURING:
#I may want to separate into py files for separate dbs. It's hard keeping everything together.

import MySQLdb
from Product import Product
from Category import Category

class ProductDataSet:
	#def __init__(self, tbl_header):
	tbl_header = ""

	commentmeta = ""
	comments =  ""
	links = ""
	options = ""
	postmeta = ""
	posts = ""
	term_relationships = ""
	term_taxonomy = ""
	termmeta = ""
	terms = ""
	usermeta = ""
	users = ""

	db = None
	cursor = None

	def __init__(self, tbl_header):
		self.tbl_header = tbl_header

		self.commentmeta = self.tbl_header + "_commentmeta"
		self.comments = self.tbl_header + "_comments"
		self.links = self.tbl_header + "_links"
		self.options = self.tbl_header + "_options"
		self.postmeta = self.tbl_header + "_postmeta"
		self.posts = self.tbl_header + "_posts"
		self.term_relationships = self.tbl_header + "_term_relationships"
		self.term_taxonomy = self.tbl_header + "_term_taxonomy"
		self.termmeta = self.tbl_header + "_termmeta"
		self.terms = self.tbl_header + "_terms"
		self.usermeta = self.tbl_header + "_usermeta"
		self.users = self.tbl_header + "_users"

		self.product_cat = self.tbl_header + "_product_cat"
		self.product_meta = self.tbl_header + "_product_meta"

		self.db = MySQLdb.connect(host = 'localhost',
                     user = 'root',
                     passwd = 'Chiaroscuro2',
                     db = 'urop_summer_2017'
                     )
		self.cursor = self.db.cursor()

		#Preprocessing
		#Deleting product_cat if exists, creating a view from inner join and populating it with info
		
		#self.cursor.execute("DROP VIEW IF EXISTS product_cat")
		#self.cursor.execute("CREATE VIEW product_cat as SELECT wp_term_taxonomy.term_id, wp_term_taxonomy.term_taxonomy_id, wp_terms.name,  wp_term_taxonomy.taxonomy, wp_term_taxonomy.description, wp_term_taxonomy.parent, wp_term_taxonomy.count FROM wp_terms INNER JOIN wp_term_taxonomy ON wp_terms.term_id = wp_term_taxonomy.term_id WHERE wp_term_taxonomy.taxonomy = 'product_cat'")

		sql_drop_productcat = "DROP VIEW IF EXISTS %s" % self.product_cat
		sql_create_productcat = "CREATE VIEW %s as SELECT t2.term_id, t2.term_taxonomy_id, t1.name,  t2.taxonomy, t2.description, t2.parent, t2.count FROM %s t1 INNER JOIN %s t2 ON t1.term_id = t2.term_id WHERE t2.taxonomy = 'product_cat'" % (self.product_cat, self.terms, self.term_taxonomy)
		
		self.cursor.execute(sql_drop_productcat)
		self.cursor.execute(sql_create_productcat)

		#couldn't inner join both tables because error is thrown w/ post_date. I've joined post_title to post_meta as a hack, but I need to fix this to connect both tables fully together.
		
		#self.cursor.execute("DROP VIEW IF EXISTS product_meta")
		#self.cursor.execute("CREATE VIEW product_meta as SELECT t1.post_title, t2.* FROM wp_posts AS t1 INNER JOIN wp_postmeta AS t2 ON t1.id = t2.post_id WHERE t1.post_type = 'product'")
		sql_drop_productmeta = "DROP VIEW IF EXISTS %s" % self.product_meta
		sql_create_productmeta = "CREATE VIEW %s as SELECT t1.post_title, t2.* FROM %s AS t1 INNER JOIN %s AS t2 ON t1.id = t2.post_id WHERE t1.post_type = 'product'" % (self.product_meta, self.posts, self.postmeta)
		
		self.cursor.execute(sql_drop_productmeta)
		self.cursor.execute(sql_create_productmeta)

		###NOTE: check that data is not null. If data == empty set, errors will happen and my life will be sad.

	def getCursor(self):
		return self.cursor

	def getDb(self):
		return self.db

	def setTblHeader(self, tbl_header):
		self.tbl_header = tbl_header

		self.commentmeta = self.tbl_header + "_commentmeta"
		self.comments = self.tbl_header + "_comments"
		self.links = self.tbl_header + "_links"
		self.options = self.tbl_header + "_options"
		self.postmeta = self.tbl_header + "_postmeta"
		self.posts = self.tbl_header + "_posts"
		self.term_relationships = self.tbl_header + "_term_relationships"
		self.term_taxonomy = self.tbl_header + "_term_taxonomy"
		self.termmeta = self.tbl_header + "_termmeta"
		self.terms = self.tbl_header + "_terms"
		self.usermeta = self.tbl_header + "_usermeta"
		self.users = self.tbl_header + "_users"

	def getTblHeader():
		return self.tbl_header
	
	def get_commentmeta(self):
		return self.commentmeta
		#etc etc all the others

	#####INSERT
	###Add params
	'''def insert_product(self, title, content, cat_name = None):
		#insert into post
		sql_post = "INSERT INTO " + self.posts + " (post_title, post_content, post_date, post_date_gmt, post_modified, post_modified_gmt, post_excerpt, to_ping, pinged, post_content_filtered, post_type) VALUES (" + "\'" + title + "\'" + ", " + "\'" + content + "\'" + ", NOW(), NOW(), NOW(), NOW(), '', '', '', '', 'product')" 
		self.cursor.execute(sql_post)

		#get inserted_prod_id
		sql_inserted_prod_id = "SELECT LAST_INSERT_ID()"
		self.cursor.execute(sql_inserted_prod_id)
		inserted_prod_id = self.cursor.fetchone()[0]

		#insert into term_relationships that term_taxonomy_id = 2 (stands for simple product type. This is an assumption that all product types inserted are simple.)
		sql_term_relationships_2 = "INSERT INTO " + self.term_relationships + " (object_id, term_taxonomy_id) VALUES (" + str(inserted_prod_id) + ", 2)"
		self.cursor.execute(sql_term_relationships_2)

		#insert into term_relationships that term_taxonomy_id = category and its parent groups.
		cat_term_taxonomy_id = None
		if cat_name != None:
			sql_cat_term_taxonomy_id = "SELECT t2.term_taxonomy_id FROM " + self.terms + " as t1 INNER JOIN " + self.term_taxonomy + " as t2 ON t1.term_id = t2.term_id where t1.name = " + "\'" + cat_name + "\'"
			self.cursor.execute(sql_cat_term_taxonomy_id)
			cat_term_taxonomy_id = self.cursor.fetchone()[0]

			#supplies error for the case that a cat name is given but couldn't find the term taxonomy id for it;__;
			if cat_name != None and cat_term_taxonomy_id == None: return "Error: could not find category with given name"

			#TODO: add recursive functionality so this can also be done for parent groups
			sql_term_relationships_cat = "INSERT INTO " + self.term_relationships + "(object_id, term_taxonomy_id) VALUES (" + str(inserted_prod_id )+ ", " + str(cat_term_taxonomy_id) + ")"
			self.cursor.execute(sql_term_relationships_cat)

		self.db.commit()
		#except:
			#self.db.rollback()
			#print ("Error: could not insert")'''

	def insert_product(self, p):
		#insert into post
		sql_post = "INSERT INTO " + self.posts + " (post_title, post_content, post_date, post_date_gmt, post_modified, post_modified_gmt, post_excerpt, to_ping, pinged, post_content_filtered, post_type) VALUES (" + "\'" + p.get_title() + "\'" + ", " + "\'" + p.get_content() + "\'" + ", NOW(), NOW(), NOW(), NOW(), '', '', '', '', 'product')" 
		self.cursor.execute(sql_post)

		#get inserted_prod_id
		sql_inserted_prod_id = "SELECT LAST_INSERT_ID()"
		self.cursor.execute(sql_inserted_prod_id)
		inserted_prod_id = self.cursor.fetchone()[0]

		#insert into term_relationships that term_taxonomy_id = 2 (stands for simple product type. This is an assumption that all product types inserted are simple.)
		sql_term_relationships_2 = "INSERT INTO " + self.term_relationships + " (object_id, term_taxonomy_id) VALUES (" + str(inserted_prod_id) + ", 2)"
		self.cursor.execute(sql_term_relationships_2)

		#insert into term_relationships that term_taxonomy_id = category and its parent groups.
		cat_term_taxonomy_id = None
		has_parent_category = p.has_parent_category()
		child = p

		while has_parent_category:
			parent_category = child.get_parent_category() #category object

			#fetch term_taxonomy_id
			sql_cat_term_taxonomy_id = "SELECT t2.term_taxonomy_id FROM " + self.terms + " as t1 INNER JOIN " + self.term_taxonomy + " as t2 ON t1.term_id = t2.term_id where t1.name = " + "\'" + parent_category.get_name() + "\'"
			self.cursor.execute(sql_cat_term_taxonomy_id)
			cat_term_taxonomy_id = self.cursor.fetchone()[0]

			#throws error for the case that a cat name is given but couldn't find the term taxonomy id for it;__;
			if p.has_parent_category() and cat_term_taxonomy_id == None: return "Error: could not find category with given name"

			#insert product-cat relationship in term_relationships
			sql_term_relationships_cat = "INSERT INTO " + self.term_relationships + "(object_id, term_taxonomy_id) VALUES (" + str(inserted_prod_id )+ ", " + str(cat_term_taxonomy_id) + ")"
			self.cursor.execute(sql_term_relationships_cat)

			#fetch count from term_taxonomy, increment by 1, and update term_taxonomy for every relation prod-cat relationship made
			sql_get_count = "SELECT count FROM " + self.term_taxonomy + " where term_taxonomy_id = "  + str(cat_term_taxonomy_id) 
			self.cursor.execute(sql_get_count)
			count = self.cursor.fetchone()[0]
			count = count + 1
			sql_update_count = "UPDATE " + self.term_taxonomy + " SET count = " + str(count) + " WHERE term_taxonomy_id = " + str(cat_term_taxonomy_id) 
			self.cursor.execute(sql_update_count)

			#if type = Product remove type
			if type(child) == type(p): child = None
			
			child = parent_category #product 1st time, but category afterwards
			has_parent_category = child.has_parent_category() 


		#insert productmeta
		self.insert_product_meta(p)

		self.db.commit()
		#except:
			#self.db.rollback()
			#print ("Error: could not insert")



	#a very hackish method for inserting productmeta. i think i'll remain separate as a helper method for insert_products. Ideally inserting into post, post_term_relationships, and postmeta should be done all at once, but sometimes people forget. 
	#TODO: modularize by separating post, post_term_rel, and postmeta ops into separate methods, the call them with insertprod.

	#TODO: make a Product object and set this as one of the main setters? makes sense that a product should have everything in posts + postmeta
	#default values are values generated by inserting a prod via gui w/o assigning it to a cat
	'''def set_productmeta_dict(self, _wp_page_template = "default", _wc_review_count = "0", _wc_rating_count = "a:0:{}", _wc_average_rating = "0", _edit_lock = "", _edit_last = "", _sku = "", _regular_price = "", _sale_price = "", _sale_price_dates_from = "", _sale_price_dates_to = "", total_sales = "0", _tax_status = "taxable", _tax_class = "", _manage_stock = "no", _backorders = "no", _sold_individually = "no", _weight = "", _length = "", _width = "", _height = "", _upsell_ids = "a:0:{}", _crosssell_ids = "a:0:{}", _purchase_note = "", _default_attributes = "a:0:{}", _virtual = "no", _downloadable = "no", _product_image_gallery = "", _download_limit = "-1", _download_expiry = "-1", _stock = None, _stock_status = "instock", _product_version = "3.0.9", _price = ""):
		return {
			"_wp_page_template":_wp_page_template, 
			"_wc_review_count":_wc_review_count, 
			"_wc_rating_count":_wc_rating_count, 
			"_wc_average_rating":_wc_average_rating, 
			"_edit_lock":_edit_lock, 
			"_edit_last":_edit_last, 
			"_sku":_sku, 
			"_regular_price":_regular_price, 
			"_sale_price":_sale_price, 
			"_sale_price_dates_from":_sale_price_dates_from, 
			"_sale_price_dates_to":_sale_price_dates_to, 
			"_total_sales":_total_sales, 
			"_tax_status":_tax_status, 
			"_tax_class":_tax_class, 
			"_manage_stock":_manage_stock, 
			"_backorders":_backorders, 
			"_sold_individually":_sold_individually, 
			"_weight":_weight, 
			"_length":_length, 
			"_width":_width, 
			"_height":_height, 
			"_upsell_ids":_upsell_ids, 
			"_crosssell_ids":_crosssell_ids, 
			"_purchase_note":_purchase_note, 
			"_default_attributes":_default_attributes, 
			"_virtual":_virtual, 
			"_downloadable":_downloadable, 
			"_product_image_gallery":_product_image_gallery, 
			"_download_limit":_download_limit, 
			"_download_expiry":_download_expiry, 
			"_stock":_stock, 
			"_stock_status":_stock_status, 
			"_product_version":_product_version, 
			"_price":_price
			}'''
           
	'''def insert_product_meta(self, prod_name, meta_dict):
		sql_prod_id_from_name = "SELECT id from " + self.posts + " where post_title = " + "\'" + prod_name + "\'" + "and post_type = 'product'"
		self.cursor.execute(sql_prod_id_from_name)
		prod_id = self.cursor.fetchone()[0]

		for item in meta_dict.items():
			sql_productmeta_key_value = "INSERT INTO " + self.postmeta + "(post_id, meta_key, meta_value) VALUES (" + str(prod_id) + ", " + "\'" + str(item[0]) + "\'" +  ", " + "\'" + str(item[1]) + "\'" +  ")"
			self.cursor.execute(sql_productmeta_key_value)
		self.db.commit()'''

	def insert_product_meta(self, p):
		sql_prod_id_from_name = "SELECT id from " + self.posts + " where post_title = " + "\'" + p.get_title() + "\'" + "and post_type = 'product'"
		self.cursor.execute(sql_prod_id_from_name)
		prod_id = self.cursor.fetchone()[0]

		for item in p.get_prod_meta_dict().items():
			sql_productmeta_key_value = "INSERT INTO " + self.postmeta + "(post_id, meta_key, meta_value) VALUES (" + str(prod_id) + ", " + "\'" + str(item[0]) + "\'" +  ", " + "\'" + str(item[1]) + "\'" +  ")"
			self.cursor.execute(sql_productmeta_key_value)
		self.db.commit()

	######UPDATE
	#idk if update_product_description works
	def update_product_description(self, prod_name, description):
		try:
			sql = "UPDATE " +  self.posts + " SET post_content = " + "\'" + description + "\'" "where post_title = " + "\'" + prod_name + "\'"
			self.cursor.execute(sql)
			self.db.commit()
		except:
			self.db.rollback()
			print("Error: could not update")

	

	###DELETE
	#condition is where, group by, etc.
	def delete_product(self, clause):
		sql = "DELETE FROM " + self.posts + " where post_type = 'product'" 
		sql += clause
		try:
			self.cursor.execute(sql)
			self.db.commit()
		except:
			self.db.rollback()
			print("Error: could not delete")


	#####READ
	#--------------
	#Product
	###wp_posts

	#10
	###Given product name p, does p exist?
	#val returned for non-existant prod is 0
	#data returns the number of matches returned. 0 == empty set.
	def exists_prod(self, p):
		sql = "SELECT * FROM " + self.posts + " where post_type = 'product' and post_title = " + "\'" + p + "\'"
		self.cursor.execute(sql) 
		data = self.cursor.fetchall()
		return True if data != () else False

	#11
	###List all product names
	def list_prod_names(self):
		sql = "SELECT t1.post_title FROM " + self.posts + " t1 INNER JOIN " + self.term_relationships + " t2 ON t1.id = t2.object_id INNER JOIN " + self.term_taxonomy + " t3 ON t2.term_taxonomy_id = t3.term_taxonomy_id WHERE t3.taxonomy = 'product_cat' GROUP BY t1.id ORDER BY t1.id"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		return[row[0] for row in data]

	#12
	###Return content/description of prod p
	#May have to resort to sku. I can't differentiate between data with the same name.
	def get_prod_description(self, p):
		sql = "SELECT post_content FROM " + self.posts + " where post_type = 'product' and post_title = " + "\'" + p + "\'"
		self.cursor.execute(sql)
		data = self.cursor.fetchone()
		return data[0] if data != None else None

	#13
	##Return content/description of all prods with name p
	def get_prod_descriptions(self, p):
		sql = "SELECT post_content FROM " + self.posts + " where post_type = 'product' and post_title = " + "\'" + p + "\'"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		return [row[0] for row in data]

	#14
	###Does content s match the description for any prod?
	def does_search_match(self, s):
		sql = "SELECT post_title, post_content from " + self.posts + " where post_type = 'product'"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		for row in data:
			if row[0] != 'AUTO-DRAFT': #get rid of AUTO-DRAFT
				if row[1] == s: return True
		return False

	#14.5
	###Does content s match the description for a prod(s) named p?
	def does_search_match_prod(self, s, p):
		sql = "SELECT post_title, post_content FROM " + self.posts + " WHERE post_type = 'product'AND post_title = " + "\'" + p + "\'"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		for row in data:
			if row[1] == s: return True
		return False

	#14.75
	###Does content s match the description for a list of prods p?
	def does_search_match_list_prods(self, s, p_list):
		for p in p_list:
			if self.does_search_match_prod(s, p): return True
		return False

	#15.00
	#14, 14.5, 14.75 but with substrings

	#15
	###Return instances where search s is description for a prod
	def find_match(self, s):
		sql = "SELECT post_title from " + self.posts  + " where post_type = 'product' and post_content = " + "\'" + s + "\'"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		return [row[0] for row in data]

	#16
	###Return instances where string c is a substring for content for a prod
	#not sure what data structure the queries go in.
	def find_substring_match(self, s):
		sql = "SELECT post_title, post_content from " + self.posts + " where post_type = 'product'"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		data_list = []
		for row in data:
			if s in row[1]: data_list.append(row[0])
		return data_list

	#------------------------------------------------------
	###wp_postmeta
	#uses created view product_meta. There is only one product_meta table, so I don't need to make a self.product meta/concat into string.

	#17
	###What is the length of the prod(s) p?
	def find_prod_length(self, p):
		sql = "SELECT post_title, meta_value from product_meta where meta_key = '_length' and post_title = " + "\'" +  p + "\'" 
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		return [row[1] for row in data]

	#18
	#longest/smallest length prod in cat/store
	def find_extrema_length(self, extrema = "max", group = "store"):
		sql = "SELECT distinct post_title, meta_value FROM product_meta WHERE meta_key = '_length'"
		
		if group != "store":
			try:  
				sql += " AND cat_name = " + "\'" + group + "\'"
			except: return "Error: not concatenating AND clause"
		
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		
		has_len_value = False	
		for row in data:
			data_dict = {row[0]: row[1]} 
			if not has_len_value:	#if there exists a len value, and has_len_value is False, set it to True
				if row[1] != '' and row[1] != None: has_len_value = True

		if has_len_value:	#if there exists a len value, eval extrema
			if extrema == "max": return max(data_dict, key=data_dict.get)
			else: return min(data_dict, key=data_dict.get)
		else: return "Can't compare: check that you have length values"	#else don't bother

	#19
	#order prods based on length asc/desc
	def order_prods_by_length(self, order = "asc"):
		sql = "SELECT post_title, meta_value from product_meta where meta_key = '_length' ORDER BY meta_value"
		if order.lower() == "desc":
			sql += " DESC"

		self.cursor.execute(sql)
		data = self.cursor.fetchall()

		return data



	#list all prods in cat/store in a certain range	
	'''def find_prod_in_range(min, max):
		SELECT post_id, meta_key, meta_value from wp_postmeta where meta_key = '_length' and meta_value >= min and meta_value <= max'''



	#THESE ARE BASICALLY THE SAME AS LENGTH. MAKE SURE LENGTH WORKS BEFORE PROCEEDING.
	#what is the width	
	#longest/smallest width prod in cat/store	
	#list all prods in cat/store in a certain range	
	#order prods based on length asc/desc

	#what is the height	
	#longest/smallest height prod in cat/store	
	#list all prods in cat/store in a certain range	
	#order prods based on length asc/desc

	#what is the sku
	#is there an sku that matches <input>

	#what are the prod attributes
	#are there prod attributes that match <input>
	#are there prods that have <input> as a prod attribute

	# what is the sale price's begin date	
	#list all sale prices in cat beginning within this time range (day, week, month)	
	#list all sale prices in store beginning within this time range (day, week, month)

	# what is the sale price's end date	
	#list all sale prices in cat ending within this time range (day, week, month)	
	#list all sale prices in store ending within this time range (day, week, month)


#--------------------------------------------------------
###wp_comments, wp_commentmeta
###Return list of all reviews for product x
#Note: currently using post title = x but may have to change to unique branding like id = x
'''SELECT t1.comment_id, t1.comment_content, t2.post_title
FROM wp_comments t1
INNER JOIN  wp_posts t2
ON t1.comment_post_id = t2.id
WHERE t2.post_title = x'''

###Return rating for comments for product x
#Note: currently using post title = x 
#but may have to change to unique branding
#like id = x
'''SELECT meta_value 
FROM wp_comment_meta t1
INNER JOIN wp_comments t2
ON t1.comment_id = t2.comment_id
INNER JOIN wp_posts t3
ON t2.comment_post_id = t3.id
WHERE t1.meta_key = "rating"
AND t3.post_title = x'''

###Return most recent review for p
'''SELECT meta_value, comment_content
FROM wp_comment_meta t1
INNER JOIN wp_comments t2
ON t1.comment_id = t2.comment_id
INNER JOIN wp_posts t3
ON t2.comment_post_id = t3.id
WHERE t1.meta_key = "rating"
AND t3.post_title = x
ORDER BY '''

#Return if p has > epsilon reviews
#Return related products for p (customers also bought, recommended)
#NO ANSWER

#Sorting. Is a category because these answers are hard to find=__=
#What is the highest rated/most popular/etc product in catagory x?
#NO ANSWER

