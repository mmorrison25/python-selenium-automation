from behave import given, when


@given('Target site is launched')
def open_target_site(context):
    context.app.main_page.open_main()


@when('Cart icon is clicked')
def click_cart(context):
    context.app.main_page.click_cart()


@when('Sign In option is clicked')
def click_sign_in(context):
    context.app.header.click_sign_in_icon()


@when('Sign In is clicked from right side nav menu')
def click_sign_in_from_side_nav(context):
    context.app.acct_side_nav.click_sign_in_side_nav()


@when('Search for {product}')
def search_for_product(context, product):
    context.app.header.search_product()