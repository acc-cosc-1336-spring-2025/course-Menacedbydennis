def add_inventory(widgets: dict, widget_name: str, quantity: int):
    """Adds a widget to inventory or updates its quantity."""
    if widget_name in widgets:
        widgets[widget_name] += quantity  # Update quantity if widget exists
    else:
        widgets[widget_name] = quantity  # Add new widget

def remove_inventory_widget(widgets: dict, widget_name: str) -> str:
    """Removes a widget from inventory if it exists."""
    if widget_name in widgets:
        del widgets[widget_name]  # Remove widget
        return "Record deleted"
    return "Item not found"

