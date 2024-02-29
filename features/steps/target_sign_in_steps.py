from behave import given, when, then


@given('Open sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()


@when('Sign In page opened')
def verify_sign_in_page_opened(context):
    context.app.sign_in_page.verify_sign_in_page_opened()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original window:', context.original_window)


@when('Click on Target terms and conditions link')
def click_terms_and_conditions_link(context):
    context.app.sign_in_page.click_terms_and_conditions_link()
    print('All windows:', context.driver.window_handles)


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.sign_in_page.switch_to_new_window()
    print('Current window:', context.driver.current_window_handle)


@then('Sign In page opened')
def verify_sign_in_page_opened(context):
    context.app.sign_in_page.verify_sign_in_page_opened()


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page_opened(context):
    context.app.sign_in_page.verify_terms_and_conditions_page_opened()


@then('User can close new window and switch back to original')
def close_window_and_switch_back_to_original(context):
    context.driver.close()
    context.app.sign_in_page.switch_to_window_by_id(context.original_window)
    print('After switching back:', context.original_window)