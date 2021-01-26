## Copy/pasted. MAKE SURE TO CHANGE ALL THIS TO FIT!

FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf

# RUN rm /etc/nginx/sites-enabled/default

COPY default.conf .

## Restart nginx after copying .conf
# RUN systemctl reload nginx
# sudo /opt/bitnami/ctlscript.sh restart nginx
