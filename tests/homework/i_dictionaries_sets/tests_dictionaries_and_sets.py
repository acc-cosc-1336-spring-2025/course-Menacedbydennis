import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class TestInventoryFunctions(unittest.TestCase):

    def test_add_inventory(self):
        widgets = {}

        # Add a new widget
        add_inventory(widgets, "Widget1", 10)
        self.assertEqual(widgets["Widget1"], 10)

        # Update the quantity of existing widget
        add_inventory(widgets, "Widget1", 25)
        self.assertEqual(widgets["Widget1"], 35)

        # Reduce the quantity of existing widget
        add_inventory(widgets, "Widget1", -10)
        self.assertEqual(widgets["Widget1"], 25)

    def test_remove_inventory_widget(self):
        widgets = {"Widget1": 15, "Widget2": 30}

        # Remove an existing widget
        result = remove_inventory_widget(widgets, "Widget1")
        self.assertEqual(result, "Record deleted")
        self.assertNotIn("Widget1", widgets)

        # Ensure Widget2 is still there
        self.assertIn("Widget2", widgets)

        # Try to remove a non-existent widget
        result = remove_inventory_widget(widgets, "Widget3")
        self.assertEqual(result, "Item not found")

if __name__ == "__main__":
    unittest.main()
