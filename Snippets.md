
<!-- Drop Down Div -->

<style>
    .dropdown:hover .dropdown-menu {
        display: block;
    }
    summary::marker {
    content: ""; /* Hide the pseudo-element */
    }
</style>

<details >
    <summary>
    <div class="">Reply</div>
    </summary>
    <details-menu role="menu" class="origin-topf-right relative right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none">
    <div class="pyf-1" role="none">
        <form method="POST" class="p-1 d-flex" action="#" role="none">
            <input type="text"  class="with-border" name="" id="">
            <button type="submit" class="block w-fulfl text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900" role="menuitem">
            <ion-icon name="send"></ion-icon>
        </button>
        </form>
    </div>
    </details-menu>
</details>





<!-- Reply Comment DIV -->
<div class="flex mr-12" style="margin-right: 20px;">
    <div class="w-10 h-10 rounded-full relative flex-shrink-0">
        <img src="{{request.user.profile.image.url}}" style="width: 40px; height: 40px;" alt="" class="absolute h-full rounded-full w-full">
    </div>
    <div>
        <div class="text-gray-700 py-2 px-3 rounded-md bg-gray-100 relative lg:ml-5 ml-2 lg:mr-12 dark:bg-gray-800 dark:text-gray-100">
            <p class="leading-6">{{c.comment}}</p>
            <div class="absolute w-3 h-3 top-3 -left-1 bg-gray-100 transform rotate-45 dark:bg-gray-800"></div>
        </div>
    </div>
</div>



<!-- Sweet alert -->
<script src="https://unpkg.com/sweetalert2@7.8.2/dist/sweetalert2.all.js"></script>
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>


<!-- Detail Page Scroller Style to calculate height -->
<div class="reply-div{{c.id}}" style="overflow-y: auto; max-height: 200px;">




<!-- Update Profile image snippers -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">

<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
  <!-- Column 1: Profile Image -->
  <div class="bg-gray-200 p-4">
    <div class="relative">
      <img src="profile.jpg" alt="Profile Picture" class="w-24 h-24 rounded-full">
      <label for="profileInput" class="absolute bottom-0 right-0 p-2 bg-white rounded-full cursor-pointer">
        <i class="fas fa-pen text-blue-500"></i>
      </label>
      <input type="file" id="profileInput" class="hidden">
    </div>
  </div>


  <div class="bg-blue-200 p-4">
    <div class="relative">
      <img src="cover.jpg" alt="Cover Image" class="w-full h-32 object-cover rounded-lg">
      <label for="coverInput" class="absolute bottom-0 right-0 p-2 bg-white rounded-full cursor-pointer">
        <i class="fas fa-pen text-blue-500"></i>
      </label>
      <input type="file" id="coverInput" class="hidden">
    </div>
  </div>
</div>


<!-- Password reset completed -->
{% extends 'partials/base.html' %}
{% load static %}
{% load widget_tweaks  %}
{% block content %}

<style>
    #id_new_password1{
        border: 1px solid black;
        width: 100%;
        height: 50px;
        border-radius: 10px;
        font-family: poppins;
    }
    #id_new_password2{
        border: 1px solid black;
        width: 100%;
        height: 50px;
        border-radius: 10px;
        font-family: poppins;
    }
    #id_old_password{
        border: 1px solid black;
        width: 100%;
        height: 50px;
        border-radius: 10px;
        font-family: poppins;
    }
</style>
    <div class="main_content">
        <div class="mcontainer">
            <div class="bg-white lg:divide-x lg:flex lg:shadow-md rounded-md shadow lg:rounded-xl overflow-hidden lg:m-0 -mx-4">
                {% include 'partials/settings_sidebar.html' %}
                <div class="lg:w-2/3">
                    <div class="lg:flex lg:flex-col justify-between lg:h-full">
                        <div class="lg:px-10 lg:py-8 p-6">
                            <h3 class="font-bold mb-2 text-xl"> Password Changed Successfully <i class="fas fa-check-circle"></i></h3>
                            <p><small>Congratulations your password have been changed.</small></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
{% endblock content %}





<!-- All My Django Packages Installed on my MAchine -->
aiohttp==3.8.4
aiosignal==1.3.1
asgiref==3.7.2
async-timeout==4.0.2     
asynctest==0.13.0        
attrs==23.1.0
autobahn==23.1.2
Automat==22.10.0
autopep8==2.0.2
backports.zoneinfo==0.2.1
beautifulsoup4==4.12.2   
boto3==1.20.26
botocore==1.23.54
certifi==2023.5.7
cffi==1.15.1
channels==4.0.0
channels-redis==4.1.0
charset-normalizer==3.1.0
constantly==15.1.0
coreapi==2.3.3
coreschema==0.0.4
coverage==3.7.1
crispy-bootstrap5==0.7
cryptography==41.0.2
daphne==4.0.0
datetime-truncate==1.1.1
defusedxml==0.7.1
diff-match-patch==20200713
dj-database-url==0.5.0
Django==3.2.18
django-admin-charts==1.3.0
django-allauth==0.54.0
django-anymail==9.1
django-audit-log==0.7.0
django-auto-logout==0.5.0
django-bootstrap-datepicker-plus==5.0.3
django-bootstrap4==23.1
django-bower==5.2.0
django-chartjs==2.3.0
django-ckeditor==6.0.0
django-ckeditor-5==0.1.6
django-cors-headers==3.14.0
django-countries==7.5.1
django-crispy-forms==2.0
django-daraja==1.3.0
django-dbbackup==4.0.2
django-debug-toolbar==1.3.0
django-decouple==2.1
django-dotenv==1.4.2
django-environ==0.9.0
django-extensions==3.2.3
django-filter==0.9.2
django-formset-js-improved==0.5.0.2
django-grappelli==2.14.3
django-helcim==0.9.1
django-heroku==0.3.1
django-htmx==1.14.0
django-import-export==3.1.0
django-jazzmin==2.6.0
django-jet==1.0.8
django-jet-reboot==1.3.3
django-jquery-js==3.1.1
django-js-asset==1.2.2
django-mailgun-provider==0.2.3
django-mapbox-location-field==2.0.0
django-mathfilters==1.0.0
django-memoize==2.3.1
django-multiselectfield==0.1.12
django-nvd3==0.9.7
django-ordered-model==3.7.4
django-otp==1.2.2
django-paypal==2.0
django-phonenumber-field==7.1.0
django-plaintext-password==0.1.0
django-ranged-response==0.2.0
django-recaptcha==3.0.0
django-rest-auth==0.4.0
django-rest-framework==0.1.0
django-simple-captcha==0.5.18
django-six==1.0.5
django-social-share==2.2.1
django-static-fontawesome==5.14.0.0
django-storages==1.12.3
django-taggit==3.0.0
django-templated-mail==1.1.1
django-tinymce==3.6.1
django-user-agents==0.4.0
django-utils-six==2.0
django-widget-tweaks==1.4.8
djangorestframework==3.13.1
djangorestframework-simplejwt==5.2.0
djoser==2.0.5
drf-spectacular==0.26.2
drf-yasg==1.21.5
environs==9.5.0
et-xmlfile==1.1.0
frozenlist==1.3.3
geoip2==4.6.0
html5lib==0.99999
hyperlink==21.0.0
idna==3.4
importlib-metadata==2.1.3
importlib-resources==5.12.0
incremental==22.10.0
inflection==0.5.1
itypes==1.2.0
Jinja2==3.1.2
jmespath==0.10.0
jsonschema==4.17.3
Markdown==2.6.2
MarkupPy==1.14
MarkupSafe==2.1.2
marshmallow==3.19.0
maxminddb==2.2.0
msgpack==1.0.5
multidict==6.0.4
mysql-connector==2.2.9
numpy==1.21.6
oauthlib==3.2.2
odfpy==1.4.1
openpyxl==3.1.2
packaging==23.1
pandas==1.3.5
paypal-payouts-sdk==1.0.0
paypalhttp==1.0.1
paypalrestsdk==1.13.1
pep8==1.7.1
phonenumbers==8.13.17
Pillow==9.5.0
pkgutil-resolve-name==1.3.10
psycopg2==2.9.6
psycopg2-binary==2.9.5
pyasn1==0.5.0
pyasn1-modules==0.3.0
pycodestyle==2.10.0
pycparser==2.21
pydantic==1.10.7
pygame==2.4.0
PyJWT==2.6.0
pyOpenSSL==23.1.1
PyPDF2==1.24
pyrsistent==0.19.3
python-dateutil==2.8.2
python-decouple==3.5
python-dotenv==0.21.1
python-http-client==3.3.7
python-nvd3==0.14.2
python-slugify==1.1.4
python3-openid==3.2.0
pytz==2023.3
PyYAML==6.0
redis==4.6.0
requests==2.28.2
requests-oauthlib==1.3.1
responses==0.23.1
rjsmin==1.1.0
ruamel.yaml==0.17.26
ruamel.yaml.clib==0.2.7
s3transfer==0.5.2
sendgrid==3.6.5
sendgrid-django==4.2.0
service-identity==21.1.0
shortuuid==1.0.11
six==1.9.0
soupsieve==2.4.1
South==1.0.2
sqlparse==0.4.3
stripe==5.4.0
tablib==3.4.0
tomli==2.0.1
Twisted==22.10.0
twisted-iocpsupport==1.0.3
txaio==23.1.1
types-PyYAML==6.0.12.9
typing-extensions==4.5.0
ua-parser==0.16.1
Unidecode==1.3.6
uritemplate==4.1.1
urllib3==1.26.15
user-agents==2.2.0
validate-email==1.3
whitenoise==5.2.0
xlrd==2.0.1
xlwt==1.3.0
xmltodict==0.13.0
yarl==1.9.1
zipp==3.15.0
zope.interface==6.0