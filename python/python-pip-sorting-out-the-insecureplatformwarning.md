Python, and pip. Sorting out the InsecurePlatformWarning on pip

You might be getting this message (or similar):

~/venv/iprs_client/local/lib/python2.7/site-packages/pip/_vendor/requests/packages/urllib3/util/ssl_.py:315:
SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name
Indication) extension to TLS is not available on this platform. This may cause
the server to present an incorrect TLS certificate, which can cause validation
failures. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#snimissingwarning.
  SNIMissingWarning

~/venv/iprs_client/local/lib/python2.7/site-packages/pip/_vendor/requests/packages/urllib3/util/ssl_.py:120:
InsecurePlatformWarning: A true SSLContext object is not available. This
prevents urllib3 from configuring SSL appropriately and may cause certain SSL
connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning

The solution is to install requests[security] with pip:

[In Ubuntu]

(venv)$ sudo apt-get install libffi-dev libssl-dev
(venv)$ pip install requests[security]
(venv)$ pip install --upgrade pip
(venv)$ pip install --upgrade requests

[In Fedora/CentOS]

# TODO

RESOURCES:
http://stackoverflow.com/questions/29134512/insecureplatformwarning-a-true-sslcontext-object-is-not-available-this-prevent
