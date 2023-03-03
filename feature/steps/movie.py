mfrom behave import given, when, then

@given(u'I navigate to the movie pages')
def nav(context):
    """ 
    Navigate to the customers page
    """
    context.browser.get('https://margocastle-centergenius-5000.codio-box.uk/movie')

@when(u'I click on the link to customer details')
def click(context):
    """ 
    Find the desired link
    """
    context.browser.find_element_by_partial_link_text('2').click()

@then(u'I should see the imdb score of movie')
def details(context):
    """ 
    if successful, then we should be directed to the customer page
    """
    # use print(context.browser.page_source) to aid debugging
    print(context.browser.page_source)
    assert context.browser.current_url == 'https://margocastle-centergenius-5000.codio-box.uk/imdbmovie'
    assert '01595 Amanda Loaf' in context.browser.page_source