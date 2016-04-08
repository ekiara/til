
If you have a server where you want all visitors who reach the root directory:

www.example.com/

To be redirected to a directory /mail/, then you do this:

In /etc/nginx/sites-available/default

server {
    location / {
        rewrite ^/$ /mail/ permanent;
    }
}
