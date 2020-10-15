    def add(self,b):
        poly = SparsePoly()
        node = self.head
        b_node = b.head
        while (node != None and b_node != None):
            if(node.data.expon == b_node.data.expon):
                poly.insert(poly.size(), Term(node.data.coeff+ b_node.data.coeff,node.data.expon))
                node = node.link
                b_node = b_node.link
            elif(node.data.expon > b_node.data.expon):
                poly.insert(poly.size(), Term(node.data.coeff,node.data.expon))
                node = node.link
            else:
                poly.insert(poly.size(), Term(n_node.data.coeff,b_node.data.expon))
                b_node = b_node.link
        return poly