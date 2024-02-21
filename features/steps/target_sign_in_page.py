from behave import then


@then('Sign In form opened')
def verify_sign_in_form_opened(context):
    context.app.sign_in_page.verify_sign_in_form_opened()