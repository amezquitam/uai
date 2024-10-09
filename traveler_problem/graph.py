
class Edge:
    def __init__(self, name, value):
        self._name = name
        self._value = value
    
    @property
    def name(self):
        return self._name
    
    @property
    def value(self):
        return self._value


class Link:
    def __init__(self, origin: Edge, destiny: Edge, value):
        self._origin = origin
        self._destiny = destiny
        self._value = value

    @property
    def origin(self):
        return self._origin
    
    @property
    def destiny(self):
        return self._destiny
    
    @property
    def value(self):
        return self._value


class Graph:
    def __init__(self, edges: list[Edge] = [], complete: bool = False, value_func = lambda x, y: None):
        self._edges = {}
        self._complete = complete
        self._conections: dict[str, dict[str, Link]] = {}
        self._value_func = value_func

        for origin in edges:
            self._edges[origin.name] = origin

        if complete:
            for origin in edges:
                for destiny in edges:
                    if origin != destiny:
                        self._conections.setdefault(origin.name, {})
                        self._conections[origin.name][destiny.name] = Link(origin, destiny, value_func(origin.value, destiny.value))
        else:
            for origin in edges:
                self._conections.setdefault(origin.name, {})
    
    def link(self, edge_origin: str, edge_destiny: str, value=None):
        origin, destiny = self.get(edge_origin), self.get(edge_destiny)
        self._conections[edge_origin][edge_destiny] = Link(
            origin, destiny, value or self._value_func(origin.value, destiny.value)
        )

    def get_neighbors(self, edge_name) -> set[Edge]:
        return set(map(lambda link: link.destiny, self._conections[edge_name].values()))
    
    def get_links(self, edge_name) -> set[Link]:
        return set(self._conections[edge_name].values())
    
    def link_value_of(self, origin_name: str, destiny_name: str) -> set[Link]:
        return self._conections[origin_name][destiny_name].value

    def get(self, edge_name) -> Edge:
        return self._edges[edge_name]

    