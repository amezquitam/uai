
from unittest import TestCase

from graph import Graph, Edge

edges = [
    Edge('Santa Marta', [20, 10]),
    Edge('Barranquilla', [0, 0]),
    Edge('Cartagena', [-30, -20]),
]

class GraphTest(TestCase):

    def test_get_neighbour(self):
        test_graph = Graph(
            edges, complete=True, 
            value_func=lambda A, B: ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5
        )

        self.assertIn(
            test_graph.get('Barranquilla'), test_graph.get_neighbors('Santa Marta')
        )

        self.assertAlmostEqual(test_graph.link_value_of('Santa Marta', 'Barranquilla'), 500 ** 0.5)
    
    def test_link(self):
        test_graph = Graph(edges, complete=False)

        test_graph.link('Santa Marta', 'Barranquilla', 100)
        test_graph.link('Barranquilla', 'Cartagena', 170)
        test_graph.link('Cartagena', 'Santa Marta', 300)

        self.assertIn(
            test_graph.get('Santa Marta'), test_graph.get_neighbors('Cartagena')
        )

        self.assertIn(
            test_graph.get('Barranquilla'), test_graph.get_neighbors('Santa Marta')
        )

        self.assertIn(
            test_graph.get('Cartagena'), test_graph.get_neighbors('Barranquilla')
        )

        self.assertEqual(test_graph.link_value_of('Cartagena', 'Santa Marta'), 300)
        self.assertEqual(test_graph.link_value_of('Barranquilla', 'Cartagena'), 170)
        self.assertEqual(test_graph.link_value_of('Santa Marta', 'Barranquilla'), 100)
