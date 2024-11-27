(0 chars long)
[stderr]: Traceback (most recent call last):
  File "./0-hbtn_status.py", line 9, in <module>
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
  File "/usr/lib/python3.4/urllib/request.py", line 161, in urlopen
    return opener.open(url, data, timeout)
  File "/usr/lib/python3.4/urllib/request.py", line 469, in open
    response = meth(req, response)
  File "/usr/lib/python3.4/urllib/request.py", line 579, in http_response
    'http', request, response, code, msg, hdrs)
  File "/usr/lib/python3.4/urllib/request.py", line 507, in error
    return self._call_chain(*args)
  File "/usr/lib/python3.4/urllib/request.py", line 441, in _call_chain
    result = func(*args)
  File "/usr/lib/python3.4/urllib/request.py", line 587, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 403: Forbidden

(879 chars long)
[Expected]
Body response:
	- type: <class 'bytes'>
	- content: b'OK'
	- utf8 content: OK

(78 chars long)
[stderr]: [Anything]
(0 chars long)
