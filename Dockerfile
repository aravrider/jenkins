# Use the CentOS base image
FROM centos:7

# Install Apache HTTP Server
RUN yum install httpd -y

# Install net-tools
RUN yum install net-tools -y

# Copy the HTML file to the Apache document root
COPY index.html /var/www/html/index.html

# Expose port 80 to the outside world
EXPOSE 80

# Start the Apache HTTP Server
CMD ["httpd", "-D", "FOREGROUND"]
