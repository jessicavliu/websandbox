#!/usr/bin/pythonx

#Specify data tables wanted. Regardless of the name of the site, the directories are numbered _2, _3, etc... so if we had some way of mapping the numbers to the site we wanted, then we could use the numbers to specify tables.

#make into class called Dataset? I need to think whether I want to do that kind of structure.

import MySQLdb

class CategoryDataSet:
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

		self.db = MySQLdb.connect(host = 'localhost',
                     user = 'root',
                     passwd = 'Chiaroscuro2',
                     db = 'urop_summer_2017'
                     )
		self.cursor = self.db.cursor()

		#Preprocessing
		#Deleting product-cat if exists, creating a table from inner join and populating it with info
		
		#self.cursor.execute("DROP TABLE IF EXISTS product_cat")
		#self.cursor.execute("CREATE TABLE product_cat as SELECT wp_term_taxonomy.term_id, wp_term_taxonomy.term_taxonomy_id, wp_terms.name,  wp_term_taxonomy.taxonomy, wp_term_taxonomy.description, wp_term_taxonomy.parent, wp_term_taxonomy.count FROM wp_terms INNER JOIN wp_term_taxonomy ON wp_terms.term_id = wp_term_taxonomy.term_id WHERE wp_term_taxonomy.taxonomy = 'product_cat'")
		self.cursor.execute("DROP VIEW IF EXISTS product_cat")
		self.cursor.execute("CREATE VIEW product_cat as SELECT wp_term_taxonomy.term_id, wp_term_taxonomy.term_taxonomy_id, wp_terms.name,  wp_term_taxonomy.taxonomy, wp_term_taxonomy.description, wp_term_taxonomy.parent, wp_term_taxonomy.count FROM wp_terms INNER JOIN wp_term_taxonomy ON wp_terms.term_id = wp_term_taxonomy.term_id WHERE wp_term_taxonomy.taxonomy = 'product_cat'")

		#couldn't inner join both tables because error is thrown w/ post_date. I've joined post_title to post_meta as a hack, but I need to fix this to connect both tables fully together.
		
		#self.cursor.execute("DROP TABLE IF EXISTS product_meta")
		#self.cursor.execute("CREATE TABLE product_meta as SELECT t1.post_title, t2.* FROM wp_posts AS t1 INNER JOIN wp_postmeta AS t2 ON t1.id = t2.post_id WHERE t1.post_type = 'product'")
		self.cursor.execute("DROP VIEW IF EXISTS product_meta")
		self.cursor.execute("CREATE VIEW product_meta as SELECT t1.post_title, t2.* FROM wp_posts AS t1 INNER JOIN wp_postmeta AS t2 ON t1.id = t2.post_id WHERE t1.post_type = 'product'")

		###NOTE: check that data is not null. If data == empty set, errors will happen and my life will be sad.

	def setTblHeader(self, tbl_header):
		self.tbl_header = tbl_header

	def setTblNames(self):
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

	def getCursor(self):
		return self.cursor
	def getDb(self):
		return self.db

	def get_commentmeta(self):
		pass
		#etc etc all the others

	#####INSERT
	###Add params
	#example for insert_category
	def insert_product(self, title, content):
		sql = "INSERT INTO " + self.posts + " (post_title, post_content, post_date, post_date_gmt, post_modified, post_modified_gmt, post_excerpt, to_ping, pinged, post_content_filtered, post_type) VALUES (" + "\'" + title + "\'" + ", " + "\'" + content + "\'" + ", NOW(), NOW(), NOW(), NOW(), '', '', '', '', 'product')" 
		self.cursor.execute(sql)
		self.db.commit()

	def insert_category(self, name, description, parent = 0):
		sql_term = "INSERT INTO " + self.terms + " (name, slug) VALUES (" + "\'" + name + "\'" + ", " + "\'" + name.lower() + "\'" + ")"
		self.cursor.execute(sql_term)

		sql_term_taxonomy = "INSERT INTO " + self.term_taxonomy + " (term_id, taxonomy, description, parent)" + "VALUES (LAST_INSERT_ID(), 'product_cat', " + "\'" + description + "\'" + ", " + str(parent) + ")"
		self.cursor.execute(sql_term_taxonomy)
		self.db.commit()
	######UPDATE
	'''def update_product_description(self, prod_name, description):
		try:
			sql = "UPDATE wp_posts SET post_content = " + "\'" + description + "\'" "where post_title = " + "\'" + prod_name + "\'"
			self.cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
			print("Error: could not update")'''

	#insert_product('test2', 'testing test2')

	#####READ
	###wp_terms and wp_term_taxonomy
		#uses created table product_meta. There is only one product_meta table, so I don't need to make a self.product meta/concat into string.

	#1
	#How many categories are there total?
	def num_categories(self):
		sql = "SELECT COUNT(*) FROM " + self.term_taxonomy + " WHERE taxonomy = " + "\'" + "product_cat" + "\'" 
		self.cursor.execute(sql)
		data = self.cursor.fetchone()	
		return data[0]

	#2
	#List all categories
	def list_categories(self):
		sql = "SELECT name FROM product_cat"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		data_list = []
		for row in data:
			data_list.append(row[0])
		return data_list

	#3
	#List all categories and the number of products they have
	def list_categories_and_prods(self):
		sql = "SELECT name, count FROM product_cat"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		data_dict = {}
		for row in data:
			data_dict[row[0]] = row[1]
		return data_dict

	#4
	#Given a category x, how many products are there in x? 
	def find_num_of_prods_in_cat(self, c):
		sql = "SELECT count FROM product_cat where name = " + "\'" + c + "\'"
		self.cursor.execute(sql)
		data = self.cursor.fetchone() 
		return data[0]

	#5
	#Which category has the most products?
	#Store in a dictionary (name:count); find max
	def cat_max_prods(self):
		sql = "SELECT name, count from product_cat"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		data_dict = {}
		for row in data:
			data_dict[row[0]] = row[1]
		return max(data_dict, key=data_dict.get)

	#6
	#Which category has the least products?
	#Store in a dictionary (name:count); find min
	def cat_min_prods(self):
		sql = "SELECT name, count from product_cat"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		data_dict = {}
		for row in data:
			data_dict[row[0]] = row[1]
		return min(data_dict, key=data_dict.get)

	#7
	#What is the description for category c?
	#throw warning instead? something that's not normal input in a db so no one gets confused
	def get_cat_description(self, c):
		sql = "SELECT description from product_cat where name = " + "\'" + c + "\'"
		self.cursor.execute(sql)
		data = self.cursor.fetchone()
		if data[0] == '':
			return "no description found"
		return data[0]

	#7.1
	###Return descriptions of all cats with name c
	def get_cat_descriptions(self, c):
		sql = "SELECT description FROM product_cat where name = " + "\'" + c + "\'"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		return [row[0] for row in data]

	#7.2
	###Does content s match the description for any cat?
	def does_any_cat_match_search(self, s):
		sql = "SELECT name, description from product_cat"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		for row in data:
			if row[0] != 'AUTO-DRAFT': #get rid of AUTO-DRAFT
				if row[1] == s: return True
		return False

	#7.3
	###Does content s exist for any category named c?
	def does_search_match_cat(self, s, c):
		sql = "SELECT name, description FROM product_cat WHERE name =" + "\'" + c + "\'"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		for row in data:
			if row[1] == s: return True
		return False

	#7.4
	###Does content s exist for a list of category c = [c1, c2, ...]?
	def does_search_match_list_cat(self, s, c_list):
		for c in c_list:
			if self.does_search_match_cat(s, c): return True
		return False

	#7.5
	###Return instances where string s is content for a category.
	def find_cat_match(self, s):
		sql = "SELECT name from product_cat where description = " + "\'" + s + "\'"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		return [row[0] for row in data]

	#7.6
	###Return instances where string s is a substring for content for category
	def find_cat_substring_match(self, s):
		sql = "SELECT name, description from product_cat"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		data_list = []
		for row in data:
			if s in row[1]: data_list.append(row[0])
		return data_list

	#8
	#Does category c have a parent category?
	def has_parent(self, c):
		sql = "SELECT parent from product_cat where name = " + "\'" + c + "\'"
		self.cursor.execute(sql)
		data = self.cursor.fetchone()
		return True if data[0] != 0 else False

	#9
	#What is the parent of category c?
	#see 6 for throwing warnings not strings
	def parent_of_cat(self, c):
		if self.has_parent(c):
			sql = "SELECT parent from product_cat where name = " + "\'" + c + "\'"
			self.cursor.execute(sql)
			data = self.cursor.fetchone()
			sql = "SELECT name from product_cat where term_id = " + "\'" + str(data[0]) + "\'"
			self.cursor.execute(sql)
			data2 = self.cursor.fetchone()
			return data2[0]
		return ("no parent found")

	#9.5
	###List all parent categories
	def list_parent_cats(self):
		sql = "SELECT name, parent FROM product_cat"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		data_list = []
		for row in data:
			if row[1] == 0: data_list.append(row[0]) 
		return data_list

