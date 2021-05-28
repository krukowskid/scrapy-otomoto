import scrapy


class OtomotoItem(scrapy.Item):
    brand = scrapy.Field()
    model = scrapy.Field()
    price = scrapy.Field()
    price_currency = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    version = scrapy.Field()
    capacity = scrapy.Field()
    horse_power = scrapy.Field()
    fuel_type = scrapy.Field()
    transmission = scrapy.Field()
    type = scrapy.Field()
    number_of_doors = scrapy.Field()
    color = scrapy.Field()
    first_owner = scrapy.Field()
    origin_country = scrapy.Field()
    no_accidents = scrapy.Field()
    aso = scrapy.Field()
    condition = scrapy.Field()
    features = scrapy.Field()
    url = scrapy.Field()
    vin = scrapy.Field()
    seller = scrapy.Field()
    drivetrain = scrapy.Field()
    financing = scrapy.Field()
    invoice = scrapy.Field()
    ad_id = scrapy.Field()
    published_at = scrapy.Field()
    plates = scrapy.Field()
    registration_date = scrapy.Field()
