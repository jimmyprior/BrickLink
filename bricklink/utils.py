from xml.etree import ElementTree 

#https://www.bricklink.com/v2/wanted/upload.page

class BrickLinkXMLFile:
    def __init__(self):
        self.inventory = ElementTree.Element("INVENTORY")
    
    
    def add_item(
        self, 
        item_type : str, 
        item_id : int, 
        color : int = None, 
        max_price : int = None, 
        min_qty : int = None, 
        qty_filled : int = None, 
        condition : str = None, 
        remarks : str = None, 
        notify : str = None, 
        wanted_show : str = None, 
        wanted_list_id : str = None
        ):
        """
        item_type : S (for a set), P (for a part), M (for a minifigure), B (for a book), G (for a gear item), C (for a catalog), I (for an instruction manual), or O (for an original box)
        item_id : value is the Item No. for this item in the BrickLink catalog
        color : value is a color ID from the Color Guide
        max_price : value is a number greater than 0
        min_qty : value is a whole number greater than 0
        qty_filled : value is a number of the quantity of the item that you already have
        condition : N (for new) or U (for used)
        remarks : value is any text
        notify : Y for notify, 
        wanted_show : Leave blank or enter Y for this item to be included in item for sale queries or enter N for this item to not be included in item for sale queries.
        wanted_list_id : ID of your wanted list you wish to upload this item to.
        """
        item = ElementTree.SubElement(self.inventory, "ITEM") 
        
        for arg_name, value in locals().items():
            if value is None or not type(value) in (str, int):
                #item and self appear in vars str check keeps htem out
                continue 
            
            name = arg_name.replace("_", "").upper()
            attribute = ElementTree.SubElement(item, name)
            attribute.text = str(value)

         
    def save(self, file_name):
        tree = ElementTree.ElementTree(self.inventory)  
        tree.write(file_name)


    def __str__(self) -> str:
        return ElementTree.tostring(self.inventory).decode()
