class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html = ""
        for prop in self.props:
            html += " " + prop
            html += "="
            html += self.props[prop]
    
    def __repr__(self):
        return  f"{self.tag} {self.value} {self.children} {self.props}"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        
        if self.tag is None:
            return self.value
        
        html_string = f"""<{self.tag}{super().props_to_html() if self.props else ""}>{self.value}</{self.tag}>"""

        return html_string