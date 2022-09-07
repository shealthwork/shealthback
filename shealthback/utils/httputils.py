# UTF-8 Format
UTF_8 = "utf-8"

def get_request_msg(request):
    """
    Given the HTTP request for a POST method, this digs into the body,
    converts it into utf-8 format and returns back the msg for further
    parsing to application logic

    Note : Since there are many ways to do this, have moved this to a function
    so that in case, any other method is used in future, it can be changed
    here

    Input
    -----
    request - HTTP request

    Output
    ------
    Returns the decoded msg in utf-8 format back
    """

    rqst_msg = request.body.decode(UTF_8)

    return rqst_msg