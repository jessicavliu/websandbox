
class Product:

	title=""
	content=""
	parent_category=None

	wp_page_template=""
	wc_review_count=""
	wc_rating_count=""  
	wc_average_rating=""  
	edit_lock=""
	edit_last=""
	sku=""
	regular_price=""  
	sale_price=""
	sale_price_dates_from=""  
	sale_price_dates_to=""
	total_sales=""
	tax_status=""
	tax_class=""
	manage_stock="" 
	backorders=""
	sold_individually="" 
	weight=""
	length=""
	width=""
	height=""
	upsell_ids=""
	crosssell_ids=""  
	purchase_note=""
	default_attributes="" 
	virtual=""
	downloadable="" 
	product_image_gallery=""  
	download_limit=""
	download_expiry=""
	stock=""
	stock_status=""  
	product_version="" 
	price=""

	def __init__(self, title, content, parent_category):
		self.title = title
		self.content = content
		self.parent_category = parent_category

		self.wp_page_template = _wp_page_template
		self.wc_review_count = _wc_review_count
		self.wc_rating_count = _wc_rating_count 
		self.wc_average_rating = _wc_average_rating 
		self.edit_lock = _edit_lock
		self.edit_last = _edit_last 
		self.sku = _sku
		self.regular_price = _regular_price 
		self.sale_price = ""
		self.sale_price_dates_from = "" 
		self.sale_price_dates_to = ""
		self.total_sales = "0"
		self.tax_status = "taxable"
		self.tax_class = "" 
		self.manage_stock = "no" 
		self.backorders = "no"
		self.sold_individually = "no" 
		self.weight = ""
		self.length = "" 
		self.width = ""
		self.height = "" 
		self.upsell_ids = "a:0:{}"
		self.crosssell_ids = "a:0:{}"
		self.purchase_note = ""
		self.default_attributes = "a:0:{}"
		self.virtual = "no"
		self.downloadable = "no" 
		self.product_image_gallery = "" 
		self.download_limit = "-1"
		self.download_expiry = "-1" 
		self.stock = None
		self.stock_status = "instock"
		self.product_version = "3.0.9"
		self.price = ""

	def __init__(self, title, content, parent_category, _wp_page_template = "default", _wc_review_count = "0", _wc_rating_count = "a:0:{}", _wc_average_rating = "0", _edit_lock = "", _edit_last = "", _sku = "", _regular_price = "", _sale_price = "", _sale_price_dates_from = "", _sale_price_dates_to = "", _total_sales = "0", _tax_status = "taxable", _tax_class = "", _manage_stock = "no", _backorders = "no", _sold_individually = "no", _weight = "", _length = "", _width = "", _height = "", _upsell_ids = "a:0:{}", _crosssell_ids = "a:0:{}", _purchase_note = "", _default_attributes = "a:0:{}", _virtual = "no", _downloadable = "no", _product_image_gallery = "", _download_limit = "-1", _download_expiry = "-1", _stock = None, _stock_status = "instock", _product_version = "3.0.9", _price = ""):
		
		self.title = title
		self.content = content
		self.parent_category = parent_category

		self.wp_page_template = _wp_page_template
		self.wc_review_count = _wc_review_count
		self.wc_rating_count = _wc_rating_count 
		self.wc_average_rating = _wc_average_rating 
		self.edit_lock = _edit_lock
		self.edit_last = _edit_last 
		self.sku = _sku
		self.regular_price = _regular_price 
		self.sale_price = _sale_price
		self.sale_price_dates_from = _sale_price_dates_from 
		self.sale_price_dates_to = _sale_price_dates_to
		self.total_sales = _total_sales
		self.tax_status = _tax_status
		self.tax_class = _tax_class 
		self.manage_stock = _manage_stock 
		self.backorders = _backorders
		self.sold_individually = _sold_individually 
		self.weight = _weight
		self.length = _length 
		self.width = _width
		self.height = _height 
		self.upsell_ids = _upsell_ids 
		self.crosssell_ids = _crosssell_ids 
		self.purchase_note = _purchase_note 
		self.default_attributes = _default_attributes 
		self.virtual = _virtual
		self.downloadable = _downloadable 
		self.product_image_gallery = _product_image_gallery 
		self.download_limit = _download_limit
		self.download_expiry = _download_expiry 
		self.stock = _stock
		self.stock_status = _stock_status 
		self.product_version = _product_version 
		self.price = _price
	
	def set_title(self, _title):
		self.title = _title

	def get_title(self):
		return self.title

	def set_content(self, _content):
		self.content = _content

	def get_content(self):
		return self.content

	def set_parent_category(self, _category):
		self.parent_category = _category

	def get_parent_category(self):
		return self.parent_category

	def set_wp_page_template(self, _wp_page_template):
		self.wp_page_template = _wp_page_template

	def get_wp_page_template(self):
		return self.wp_page_template

	def set_wc_review_count(self, _wc_review_count):
		self.wc_review_count = _wc_review_count

	def get_wc_review_count(self):
		return self.wc_review_count

	def set_wc_rating_count(self, _wc_rating_count):
		self.wc_rating_count = _wc_rating_count

	def get_wc_rating_count(self):
		return self.wc_rating_count

	def set_wc_average_rating(self, _wc_average_rating):
		self.wc_average_rating = _wc_average_rating

	def get_wc_average_rating(self):
		return self.wc_average_rating

	def set_edit_lock(self, _edit_lock):
		self.edit_lock = _edit_lock

	def get_edit_lock(self):
		return self.edit_lock

	def set_edit_last(self, _edit_last):
		self.edit_last = _edit_last

	def get_edit_last(self):
		return self.edit_last

	def set_sku(self, _sku):
		self.sku = _sku

	def get_sku(self):
		return self.sku

	def set_regular_price(self, _regular_price):
		self.regular_price = _regular_price

	def get_regular_price(self):
		return self.regular_price

	def set_sale_price(self, _sale_price):
		self.sale_price = _sale_price

	def get_sale_price(self):
		return self.sale_price

	def set_sale_price_dates_from(self, _sale_price_dates_from):
		self.sale_price_dates_from = _sale_price_dates_from

	def get_sale_price_dates_from(self):
		return self.sale_price_dates_from

	def set_sale_price_dates_to(self, _sale_price_dates_to):
		self.sale_price_dates_to = _sale_price_dates_to

	def get_sale_price_dates_to(self):
		return self.sale_price_dates_to

	def set_total_sales(self, _total_sales):
		self.total_sales = _total_sales

	def get_total_sales(self):
		return self.total_sales

	def set_tax_status(self, _tax_status):
		self.tax_status = _tax_status

	def get_tax_status(self):
		return self.tax_status

	def set_tax_class(self, _tax_class):
		self.tax_class = _tax_class

	def get_tax_class(self):
		return self.tax_class

	def set_manage_stock(self, _manage_stock):
		self.manage_stock = _manage_stock

	def get_manage_stock(self):
		return self.manage_stock

	def set_backorders(self, _backorders):
		self.backorders = _backorders

	def get_backorders(self):
		return self.backorders

	def set_sold_individually(self, _sold_individually):
		self.sold_individually = _sold_individually

	def get_sold_individually(self):
		return self.sold_individually

	def set_weight(self, _weight):
		self.weight = _weight

	def get_weight(self):
		return self.weight

	def set_length(self, _length):
		self.length = _length

	def get_length(self):
		return self.length

	def set_width(self, _width):
		self.width = _width

	def get_width(self):
		return self.width

	def set_height(self, _height):
		self.height = _height

	def get_height(self):
		return self.height

	def set_upsell_ids(self, _upsell_ids):
		self.upsell_ids = _upsell_ids

	def get_upsell_ids(self):
		return self.upsell_ids

	def set_crosssell_ids(self, _crosssell_ids):
		self.crosssell_ids = _crosssell_ids

	def get_crosssell_ids(self):
		return self.crosssell_ids

	def set_purchase_note(self, _purchase_note):
		self.purchase_note = _purchase_note

	def get_purchase_note(self):
		return self.purchase_note

	def set_default_attributes(self, _default_attributes):
		self.default_attributes = _default_attributes

	def get_default_attributes(self):
		return self.default_attributes

	def set_virtual(self, _virtual):
		self.virtual = _virtual

	def get_virtual(self):
		return self.virtual

	def set_downloadable(self, _downloadable):
		self.downloadable = _downloadable

	def get_downloadable(self):
		return self.downloadable

	def set_product_image_gallery(self, _product_image_gallery):
		self.product_image_gallery = _product_image_gallery

	def get_product_image_gallery(self):
		return self.product_image_gallery

	def set_download_limit(self, _download_limit):
		self.download_limit = _download_limit

	def get_download_limit(self):
		return self.download_limit

	def set_download_expiry(self, _download_expiry):
		self.download_expiry = _download_expiry

	def get_download_expiry(self):
		return self.download_expiry

	def set_stock(self, _stock):
		self.stock = _stock

	def get_stock(self):
		return self.stock

	def set_stock_status(self, _stock_status):
		self.stock_status = _stock_status

	def get_stock_status(self):
		return self.stock_status

	def set_product_version(self, _product_version):
		self.product_version = _product_version

	def get_product_version(self):
		return self.product_version

	def set_price(self, _price):
		self.price = _price

	def get_price(self):
		return self.price

	def get_prod_meta_dict(self):
		return {"_wp_page_template":self.wp_page_template, 
			"_wc_review_count":self.wc_review_count, 
			"_wc_rating_count":self.wc_rating_count, 
			"_wc_average_rating":self.wc_average_rating, 
			"_edit_lock":self.edit_lock, 
			"_edit_last":self.edit_last, 
			"_sku":self.sku, 
			"_regular_price":self.regular_price, 
			"_sale_price":self.sale_price, 
			"_sale_price_dates_from":self.sale_price_dates_from, 
			"_sale_price_dates_to":self.sale_price_dates_to, 
			"_total_sales":self.total_sales, 
			"_tax_status":self.tax_status, 
			"_tax_class":self.tax_class, 
			"_manage_stock":self.manage_stock, 
			"_backorders":self.backorders, 
			"_sold_individually":self.sold_individually, 
			"_weight":self.weight, 
			"_length":self.length, 
			"_width":self.width, 
			"_height":self.height, 
			"_upsell_ids":self.upsell_ids, 
			"_crosssell_ids":self.crosssell_ids, 
			"_purchase_note":self.purchase_note, 
			"_default_attributes":self.default_attributes, 
			"_virtual":self.virtual, 
			"_downloadable":self.downloadable, 
			"_product_image_gallery":self.product_image_gallery, 
			"_download_limit":self.download_limit, 
			"_download_expiry":self.download_expiry, 
			"_stock":self.stock, 
			"_stock_status":self.stock_status, 
			"_product_version":self.product_version, 
			"_price":self.price
			}

	def has_parent_category(self):
		return True if self.parent_category != None else False