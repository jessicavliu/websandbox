#!/usr/bin/python

#SOME NOTES ABOUT STRUCTURING:
#I may want to separate into py files for separate dbs. It's hard keeping everything together.
#I'm making the language python. Make sure this works in python for wp_terms and wp_term_taxonomy.

import MySQLdb

db = MySQLdb.connect(host = 'localhost',
                     user = 'root',
                     passwd = 'Chiaroscuro2',
                     db = 'urop_summer_2017'
    	)

#creating a Cursor object
cursor = db.cursor()

#Specify data tables wanted. Regardless of the name of the site, the directories are numbered _2, _3, etc... so if we had some way of mapping the numbers to the site we wanted, then we could use the numbers to specify tables.

#make into class called Dataset? I need to think whether I want to do that kind of structure.

class DataSet:
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
		self.cursor = db.cursor()

	def getCursor(self):
		return self.cursor

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

	def get_commentmeta(self):
		pass
		#etc etc all the others
		#i forgot that python doesn't do encapsulation

#objec

#Preprocessing
#Deleting product-cat if exists, creating a table from inner join and populating it with info
cursor.execute("DROP TABLE IF EXISTS product_cat")
cursor.execute("CREATE TABLE product_cat as SELECT wp_term_taxonomy.term_id, wp_term_taxonomy.term_taxonomy_id, wp_terms.name,  wp_term_taxonomy.taxonomy, wp_term_taxonomy.description, wp_term_taxonomy.parent, wp_term_taxonomy.count FROM wp_terms INNER JOIN wp_term_taxonomy ON wp_terms.term_id = wp_term_taxonomy.term_id WHERE wp_term_taxonomy.taxonomy = 'product_cat'")

#couldn't inner join both tables because error is thrown w/ post_date. I've joined post_title to post_meta as a hack, but I need to fix this to connect both tables fully together.
cursor.execute("DROP TABLE IF EXISTS product_meta")
cursor.execute("CREATE TABLE product_meta as SELECT t1.post_title, t2.* FROM wp_posts AS t1 INNER JOIN wp_postmeta AS t2 ON t1.id = t2.post_id WHERE t1.post_type = 'product'")

###NOTE: check that data is not null. If data == empty set, errors will happen and my life will be sad.


###wp_terms and wp_term_taxonomy

#hack
tbl_header = "wp"

#1
#How many categories are there total?
def num_categories():
	sql = "SELECT COUNT(*) FROM " + tbl_header + "_term_taxonomy WHERE taxonomy = " + "\'" + "product_cat" + "\'" 
	cursor.execute(sql)
	#cursor.execute("SELECT COUNT(*) FROM wp_term_taxonomy WHERE taxonomy = 'product_cat'")
	data = cursor.fetchone()	
	return data[0]

#2
#List all categories
def list_categories():
	cursor.execute("SELECT name FROM product_cat")
	data = cursor.fetchall()
	data_list = []
	for row in data:
		data_list.append(row[0])
	return data_list

#3
#List all categories and the number of products they have
def list_categories_and_prods():
	cursor.execute("SELECT name, count FROM product_cat")
	data = cursor.fetchall()
	data_dict = {}
	for row in data:
		data_dict[row[0]] = row[1]
	return data_dict

#4
#Given a category x, how many products are there in x? 
def find_num_of_prods_in_cat(c):
	cursor.execute("SELECT count FROM product_cat where name = %s", [c])
	data = cursor.fetchone() 
	return data[0]

#5
#Which category has the most products?
#Store in a dictionary (name:count); find max
def cat_max_prods():
	cursor.execute("SELECT name, count from product_cat")
	data = cursor.fetchall()
	data_dict = {}
	for row in data:
		data_dict[row[0]] = row[1]
	return max(data_dict, key=data_dict.get)

#6
#Which category has the least products?
#Store in a dictionary (name:count); find min
def cat_min_prods():
	cursor.execute("SELECT name, count from product_cat")
	data = cursor.fetchall()
	data_dict = {}
	for row in data:
		data_dict[row[0]] = row[1]
	return min(data_dict, key=data_dict.get)

#7
#What is the description for category c?
#throw warning instead? something that's not normal input in a db so no one gets confused
def get_cat_description(c):
	cursor.execute("SELECT description from product_cat where name =%s", [c])
	data = cursor.fetchone()
	if data[0] == '':
		return "no description found"
	return data[0]

#7.1
###Return descriptions of all cats with name c
def get_cat_descriptions(c):
	sql = "SELECT description FROM product_cat where name = " + "\'" + c + "\'"
	cursor.execute(sql)
	data = cursor.fetchall()
	return [row[0] for row in data]

#7.2
###Does content s match the description for any cat?
def does_any_cat_match_search(s):
	sql = "SELECT name, description from product_cat"
	cursor.execute(sql)
	data = cursor.fetchall()
	for row in data:
		if row[0] != 'AUTO-DRAFT': #get rid of AUTO-DRAFT
			if row[1] == s: return True
	return False

#7.3
###Does content s exist for any category named c?
def does_search_match_cat(s, c):
	sql = "SELECT name, description FROM product_cat WHERE name =" + "\'" + c + "\'"
	cursor.execute(sql)
	data = cursor.fetchall()
	for row in data:
		if row[1] == s: return True
	return False

#7.4
###Does content s exist for a list of category c = [c1, c2, ...]?
def does_search_match_list_cat(s, c_list):
	for c in c_list:
		if does_search_match_cat(s, c): return True
	return False

#7.5
###Return instances where string s is content for a category.
def find_cat_match(s):
	sql = "SELECT name from product_cat where description = " + "\'" + s + "\'"
	cursor.execute(sql)
	data = cursor.fetchall()
	return [row[0] for row in data]

#7.6
###Return instances where string s is a substring for content for category
def find_cat_substring_match(s):
	sql = "SELECT name, description from product_cat"
	cursor.execute(sql)
	data = cursor.fetchall()
	data_list = []
	for row in data:
		if s in row[1]: data_list.append(row[0])
	return data_list

#8
#Does category c have a parent category?
def has_parent(c):
	cursor.execute("SELECT parent from product_cat where name = %s", [c])
	data = cursor.fetchone()
	return True if data[0] != 0 else False

#9
#What is the parent of category c?
#see 6 for throwing warnings not strings
def parent_of_cat(c):
	if has_parent(c):
		cursor.execute("SELECT parent from product_cat where name = %s", [c])
		data = cursor.fetchone()
		cursor.execute("SELECT name from product_cat where term_id = %s", [data[0]])
		data2 = cursor.fetchone()
		return data2[0]
	return ("no parent found")

#9.5
###List all parent categories
def list_parent_cats():
	sql = "SELECT name, parent FROM product_cat"
	cursor.execute(sql)
	data = cursor.fetchall()
	data_list = []
	for row in data:
		if row[1] == 0: data_list.append(row[0]) 
	return data_list

#-------------------------------------------------------------
#Product
###wp_posts

#10
###Given product name p, does p exist?
#val returned for non-existant prod is 0
#data returns the number of matches returned. 0 == empty set.
def exists_prod(p):
	cursor.execute("SELECT * FROM wp_posts where post_type = 'product' and post_title = %s",[p]) 
	data = cursor.fetchall()
	return True if data != () else False

#11
###List all product names
def list_prod_names():
	cursor.execute("SELECT t1.post_title FROM wp_posts t1 INNER JOIN wp_term_relationships t2 ON t1.id = t2.object_id INNER JOIN wp_term_taxonomy t3 ON t2.term_taxonomy_id = t3.term_taxonomy_id WHERE t3.taxonomy = 'product_cat' GROUP BY t1.id ORDER BY t1.id")
	data = cursor.fetchall()
	return[row[0] for row in data]

#12
###Return content/description of prod p
#May have to resort to sku. I can't differentiate between data with the same name.
def get_prod_description(p):
	cursor.execute("SELECT post_content FROM wp_posts where post_type = 'product' and post_title = %s", [p])
	data = cursor.fetchone()
	return data[0]

#13
##Return content/description of all prods with name p
def get_prod_descriptions(p):
	cursor.execute("SELECT post_content FROM wp_posts where post_type = 'product' and post_title = %s", [p])
	data = cursor.fetchall()
	return [row[0] for row in data]

#14
###Does content s match the description for any prod?
def does_search_match(s):
	cursor.execute("SELECT post_title, post_content from wp_posts where post_type = 'product'")
	data = cursor.fetchall()
	for row in data:
		if row[0] != 'AUTO-DRAFT': #get rid of AUTO-DRAFT
			if row[1] == s: return True
	return False

#14.5
###Does content s match the description for a prod(s) named p?
def does_search_match_prod(s, p):
	cursor.execute("SELECT post_title, post_content FROM wp_posts WHERE post_type = 'product'AND post_title =%s", [p])
	data = cursor.fetchall()
	for row in data:
		if row[1] == s: return True
	return False

#14.75
###Does content s match the description for a list of prods p?
def does_search_match_list_prods(s, p_list):
	for p in p_list:
		if does_search_match_prod(s, p): return True
	return False

#15.00
#14, 14.5, 14.75 but with substrings
#I need to make a spreadsheet for this, the labelling/keeping together similar questions is v confusing

#15
###Return instances where search s is description for a prod
def find_match(s):
	cursor.execute("SELECT post_title from wp_posts where post_type = 'product' and post_content = %s", [s])
	data = cursor.fetchall()
	return [row[0] for row in data]

#16
###Return instances where string c is a substring for content for a prod
#not sure what data structure the queries go in.
def find_substring_match(s):
	cursor.execute("SELECT post_title, post_content from wp_posts where post_type = 'product'")
	data = cursor.fetchall()
	data_list = []
	for row in data:
		if s in row[1]: data_list.append(row[0])
	return data_list

#------------------------------------------------------
###wp_postmeta

##uhh need to be able to insert shit

#17
###What is the length of the prod(s) p?
def find_prod_length(p):
	sql = "SELECT post_title, meta_value from product_meta where meta_key = '_length' and post_title = " + "\'" +  p + "\'" 
	cursor.execute(sql)
	data = cursor.fetchall()
	return [row[1] for row in data]

#18
#longest/smallest length prod in cat/store
def find_extrema_length(extrema, group="store"):
	sql = "SELECT post_title, meta_value from wp_postmeta where meta_key = '_length'"
	cursor.execute(sql)
	data = cursor.fetchall()
	data_dict = {row[0]: row[1]} for row in data
	return data_dict
	if extrema = "max":
		return max()
	else:
		return min(all)
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

#---
#Saving output into vars
#idk if necessary but seems like good practice

#---
#Printing out output
#Make into test cases
#1
print("How many categories are there total?")
print(num_categories())
print()

#2
print("List all categories")
print(list_categories())
print()

#3
print("List all categories and the number of prods they have.")
print(list_categories_and_prods())
print()

#4
c = 'Music'
print("Given the category " + c + ", how many products are there in " + c + "?")
print(find_num_of_prods_in_cat(c))
print()

#5
print("Which category has the most products?")
print(cat_max_prods())
print()

#6
print("Which category has the least products?")
print(cat_min_prods())
print()

#7
c = 'Music'
print("What is the description for category " + c + "?")
print(get_cat_description(c))
print()

#7.1
c = 'Music'
print("Return descriptions of all categories with name " + c)
print(get_cat_descriptions(c))
print()

#7.2
s = "test"
print("Does content s exist for any category descriptions?")
print(does_any_cat_match_search(s))
print()

#7.3
s = "test"
c = "Music"
print("Does content s exist for any category named c?")
print(does_search_match_cat(s, c))
print()

#7.4
#works for strings that are not actually cat names
s = "test"
c_list = ["Singles", "Music"]
print("Does content s exist for a list of category c = [c1, c2, ...]?")
print(does_search_match_list_cat(s, c_list))
print()

#7.5
#test further
s = "test"
print("Return instances where string s is content for a category.")
print(find_cat_match(s))
print()

#7.6
s = ""
print("Return instances where string s is a substring for content for category.")
print(find_cat_substring_match(s))
print()

#8
c = 'Music'
print("Does category " + c + " have a parent category?")
print(has_parent(c))
print()

#9
c = 'Hoodies'
print ("What is the parent of category " + c + "?")
print(parent_of_cat(c))
print()

#9.5
print("List all parent categories")
print(list_parent_cats())
print()

#10
p = "Woo Ninja"
print("Given product name " + p + ", does it exist?")
print(exists_prod(p))
print()

#11
print("List all product names")
print(list_prod_names())
print()

#12
p = 'Woo Ninja'
print("Return description of prod p")
print(get_prod_description(p))
print()

#13
p = 'Woo Ninja'
print("Return description of all prods with name p")
print(get_prod_descriptions(p))
print()

#14
s = 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.'
print("Does content c exist for any prod?")
print(does_search_match(s))
print()

#14.5
s = 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.'
p = 'Woo Ninja'
print("Does content s match the description for a prod(s) named p?")
print(does_search_match_prod(s, p))
print()

#14.75
#inserting new prod. reqs: no description
#when formulating test cases paste this and other insertions at the top
#look up MERGE
#cursor.execute("IF EXISTS (SELECT * FROM wp_posts WHERE post_type = 'product' and post_title = 'Test 14.75.')")

s = 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.'
p_list = ['Test 14.75', 'Woo Ninja']
print("Does content s match the description for a list of prods p?")
print(does_search_match_list_prods(s, p_list))
print()

#15
s = 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.'
print("Return instances where string s is content for a prod")
print(find_match(s))
print()

#16
s = 'Pellentesque'
print("Return instances where string c is a substring for content for a prod")
print(find_substring_match(s))
print()

#17
p = 'Woo Ninja'
print("What is the length of prod(s) p?")
print(find_prod_length(p))
print()

#18
print("List all prods in cat in a certain range")
print()
print()

#19
print("longest/smallest length prod in cat/store")
print()
print()

#20
print("order prods based on length asc/desc")
print()
print()


#sql = "SELECT post_title from wp_posts where post_type = 'product' and post_content = " + "\'" + s + "\'"

#---
db.close()

