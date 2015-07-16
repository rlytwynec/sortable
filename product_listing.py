class Product:
    def __init__(self, product_name, manufacturer, model, announced_date, family = ""):
        self.product_name = product_name
        self.manufacturer = manufacturer
        self.model = model
        self.announced_date = announced_date
        self.family = family

    def getProduct(self):
        return self.product_name

    def getManufacturer(self):
        return self.manufacturer

    def getFamily(self):
        return self.family

    def getModel(self):
        return self.model

    def getAnnounced(self):
        return self.announced_date

    def isProduct(self, title):
        if self.product_name.lower() in title.lower():
            return True
        else:
            return False

    def isManufacturer(self, title):
        if self.manufacturer.lower() in title.lower():
            return True
        else:
            return False

    def isFamily(self, title):
        if self.family.lower() in title.lower():
            return True
        else:
            return False

    def isModel(self, title):
        if self.model.lower() in title.lower():
            return True
        else:
            return False

    def isAnnounced(self, title):
        if self.announced_date.lower() in title.lower():
            return True
        else:
            return False

    def isMatch(self, title):
        # Pad model and family with spaces
        # Prevents matching "model 123" with "model 1234"
        model_word = " " + self.model + " "
        family_word = " " + self.family + " "
        # Pad title in case model/family is at the start or end of the string
        title_padded = " " + title + " "

        # Test for match and return result
        if model_word in title_padded and family_word in title_padded:
            return True
        else:
            return False




class Listing:
    def __init__(self, title, manufacturer, currency, price, json):
        self.title = title
        self.manufacturer = manufacturer
        self.currency = currency
        self.price = price
        self.json = json

    def getTitle(self):
        return self.title

    def getManufacturer(self):
        return self.manufacturer

    def getCurrency(self):
        return self.currency

    def getPrice(self):
        return self.price

    def getJSON(self):
        return self.json
