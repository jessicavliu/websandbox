#!/usr/bin/python

#SOME NOTES ABOUT STRUCTURING:
#I may want to separate into py files for separate dbs. It's hard keeping everything together.
#I'm making the language python. Make sure this works in python for wp_terms and wp_term_taxonomy.

import MySQLdb


#Specify data tables wanted. Regardless of the name of the site, the directories are numbered _2, _3, etc... so if we had some way of mapping the numbers to the site we wanted, then we could use the numbers to specify tables.

#make into class called Dataset? I need to think whether I want to do that kind of structure.

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


		self.db = MySQLdb.connect(host = 'localhost',
                     user = 'root',
                     passwd = 'Chiaroscuro2',
                     db = 'urop_summer_2017'
    	)

		#creating a Cursor object
		self.cursor = self.db.cursor()

		#Preprocessing
		#Deleting product-cat if exists, creating a table from inner join and populating it with info
		self.cursor.execute("DROP TABLE IF EXISTS product_cat")
		self.cursor.execute("CREATE TABLE product_cat as SELECT wp_term_taxonomy.term_id, wp_term_taxonomy.term_taxonomy_id, wp_terms.name,  wp_term_taxonomy.taxonomy, wp_term_taxonomy.description, wp_term_taxonomy.parent, wp_term_taxonomy.count FROM wp_terms INNER JOIN wp_term_taxonomy ON wp_terms.term_id = wp_term_taxonomy.term_id WHERE wp_term_taxonomy.taxonomy = 'product_cat'")

		#couldn't inner join both tables because error is thrown w/ post_date. I've joined post_title to post_meta as a hack, but I need to fix this to connect both tables fully together.
		self.cursor.execute("DROP TABLE IF EXISTS product_meta")
		self.cursor.execute("CREATE TABLE product_meta as SELECT t1.post_title, t2.* FROM wp_posts AS t1 INNER JOIN wp_postmeta AS t2 ON t1.id = t2.post_id WHERE t1.post_type = 'product'")

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
	def insert_product(self, title, content):
		sql = "INSERT INTO " + self.posts + " (post_title, post_content, post_date, post_date_gmt, post_modified, post_modified_gmt, post_excerpt, to_ping, pinged, post_content_filtered, post_type) VALUES (" + "\'" + title + "\'" + ", " + "\'" + content + "\'" + ", NOW(), NOW(), NOW(), NOW(), '', '', '', '', 'product')" 
		self.cursor.execute(sql)
		self.db.commit()
		#except:
			#self.db.rollback()
			#print ("Error: could not insert")

	######UPDATE
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
	#uses created table product_meta. There is only one product_meta table, so I don't need to make a self.product meta/concat into string.

	##uhh need to be able to insert shit
	#17
	###What is the length of the prod(s) p?
	def find_prod_length(self, p):
		sql = "SELECT post_title, meta_value from product_meta where meta_key = '_length' and post_title = " + "\'" +  p + "\'" 
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		return [row[1] for row in data]

	#18
	#longest/smallest length prod in cat/store
	#AHHHSDFKLD ALSO HAVE TO INNER JOIN WITH wp_term_relationships and wp_term_taxonomy
	#draw this out next time
	'''def find_extrema_length(extrema, group = "store", c):
		if group == "store": 
			sql = "SELECT post_title, meta_value FROM wp_postmeta WHERE meta_key = '_length'"
		else: 
			sql = "SELECT post_title, meta_value FROM wp_postmeta WHERE meta_key = '_length' AND "

		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		for row in data:
			data_dict = {row[0]: row[1]} 
		#if data_dict has int values
		if extrema == "max":breturn max(data_dict, key=data_dict.get)
		else: return min(data_dict, key=data_dict.get)'''
	#not sure if this is correct
	#it's pseudocode anyway

	#list all prods in cat/store in a certain range	
	'''def find_prod_in_range(min, max):
		SELECT post_id, meta_key, meta_value from wp_postmeta where meta_key = '_length' and meta_value >= min and meta_value <= max'''

	#separated asc/desc for now
	#order prods based on length asc
	#SELECT post_id, meta_key, meta_value from wp_postmeta where meta_kkey = '_length' ORDER BY meta_value

	#order prods based on length desc
	#SELECT post_id, meta_key, meta_value from wp_postmeta where meta_kkey = '_length' ORDER BY meta_value DESC

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

