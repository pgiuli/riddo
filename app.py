from urllib.parse import parse_qs

redirs = {
    'blog':'https://blog.giuli.cat',
    'github':'https://github.com/pgiuli',
    'instagram':'https://instagram.com/pxxgl'
          }


def parse_query_parameters(query_string):
    # Use parse_qs to parse the query string into a dictionary
    parameters_dict = parse_qs(query_string)

    return parameters_dict

#WIP: redirect managing
#def add_redir()

def app(environ, start_response):

    path = environ['PATH_INFO'][1:] #The [1:] removes the '/' from the string 
    #print(f'Path is {path}')
    site = redirs.get(path)
    #print(f'Site is {site}')

    params = parse_query_parameters(environ['QUERY_STRING'])
    print(params)

    if site != None:
        start_response('302 Found', [('Location', site)])
    
    else:
        start_response('200 OK', [('Content-Type', 'text/plain')])

    message = "If you're seeing this either I messed up or you didn't add a correct path!\n"
    
    debug_info = f'Accessed path: {path}\nEquivalent site (none if invalid): {site}'

    response = '\n'.join([message, debug_info])
    return [response.encode()]
