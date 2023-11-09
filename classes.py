class Customer:
    def __init__(self, customer_code, first_name, last_name):
      self.customer_code = customer_code
      self.first_name = first_name
      self.last_name = last_name

    def get_headerList():
      row=["CUSTOMER_CODE" , "FIRSTNAME" , "LASTNAME"]
      return row

    def get_attributes(self):
      row=[self.customer_code , self.first_name , self.last_name]
      return row




class Invoice:
    def __init__(self, customer_code, invoice_code, amount, date):
      self.customer_code = customer_code
      self.invoice_code = invoice_code
      self.amount = amount
      self.date = date

    def get_headerList():
      row=["CUSTOMER_CODE" , "INVOICE_CODE" , "AMOUNT" , "DATE"]
      return row

    def get_attributes(self):
      row=[self.customer_code , self.invoice_code , self.amount , self.date]
      return row




class InvoiceItem:
    def __init__(self, invoice_code, item_code, amount, quantity):
      self.invoice_code = invoice_code
      self.item_code = item_code
      self.amount = amount
      self.quantity = quantity

    def get_headerList():
      row=["INVOICE_CODE" , "ITEM_CODE" , "AMOUNT" , "QUANTITY"]
      return row

    def get_attributes(self):
      row=[self.invoice_code , self.item_code , self.amount , self.quantity]
      return row
