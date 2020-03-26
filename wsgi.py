def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/plain')])
	resp = environ['QUERY_STRING'].split("&")
	resp = [bytes(str(item+"\r\n"),encoding='utf-8') for item in resp]
	return resp
