# mbd-cms-template

Minneapolis Ballet Dancers or MBD is a non profit organization that groups ballet dancers from the twin cities.

This template introduces the html templates and plugins necessary to build MBDs website using DJANGO CMS platform
 
##### Install
 Add -e git+https://github.com/ti3r/mbd-cms-template.git#egg=mbd_cms_template to your requirements.txt
 Add mbd_cms_template to the list of INSTALLED_APPS in your settings.py file
 Add the following templates to CMS_TEMPLATES in your settings.py
    ('mbd_template/mbd.html','MBD Home'),
    ('mbd_template/contact.html','MBD Contact Us'),
    ('mbd_template/about.html','MBD About'),
    ('mbd_template/full_width.html','MBD Full Width Page'),

