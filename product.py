from trytond.osv import fields, OSV

class Product(OSV):
    "Product"
    _name = "product.product"
    _description = __doc__
    _inherits = {'product.template': 'product_template'}

    product_template = fields.Many2One('product.template', 'Product Template',
                                        required=True)
    code = fields.Char("Code", size=1,) # TODO will be change to None
                                        # when implemeted
    description = fields.Text("Description",)


    def name_search(self, cursor, user, name,  args=None, operator='ilike',
                    context=None, limit=80):
        if not args:
            args=[]
        ids = self.search(cursor, user, [('code','=',name)]+ args, limit=limit,
                          context=context)
        if not ids:
            ids = self.search(cursor, user, [('name',operator,name)]+ args,
                              limit=limit, context=context)
        result = self.name_get(cursor, user, ids, context)
        return result

Product()