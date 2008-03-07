from trytond.osv import fields, OSV


class Category(OSV):
    "Product Category"
    _name = "product.category"
    _description = __doc__
    _order = "parent,name"

    name = fields.Char('Name', size=64, required=True)
    complete_name = fields.Function('complete_name', type="char", string='Name')
    parent = fields.Many2One('product.category','Parent Category', select=True)
    childs = fields.One2Many('product.category', 'parent',
            string='Child Categories')

    def complete_name(self, cursor, user, obj_id, name, value, arg,
            context=None):
        res = self.name_get(cursor, user, ids, context)
        return dict(res)

    def name_get(self, cursor, user, ids, context=None):
        if not len(ids):
            return []
        categories = self.browse(cursor, user, ids, context=context)
        res = []
        for category in categories:
            if category.parent:
                name = category.parent.name+' / '+ category.name
            else:
                name = category.name
            res.append((category.id, name))
        return res

Category()