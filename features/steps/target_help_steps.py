from behave import given, when, then


@given('Open Help page for Returns')
def open_help_returns(context):
    context.app.help_page.open_help_returns()


@when('Select {topic_name} option')
def select_help_topic(context, topic_name):
    context.app.help_page.select_help_topic(topic_name)


@then('Verify Returns page is opened')
def verify_returns_displayed(context):
    context.app.help_page.verify_returns_displayed()


@then('Delivery & Pickup page is displayed')
def verify_delivery_pickup_displayed(context):
    context.app.help_page.verify_delivery_pickup_displayed()

