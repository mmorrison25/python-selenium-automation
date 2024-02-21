from behave import when, then


@when('Add to cart button is clicked')
def add_item_to_cart(context):
    context.app.search_results_page.add_item_to_cart()


@then('Search results for {expected_product} are shown')
def verify_search_results_shown(context, expected_product):
    context.app.search_results_page.verify_search_results_shown(expected_product)