def pt(title=None, text=None):
    """
    Use the print function to print a title and an object coverted to string
    :param title:
    :param text:
    """
    if text is None:
        text = title
        title = "------------------------"
    else:
        title += ':'
    print(str(title) + " \n " + str(text))