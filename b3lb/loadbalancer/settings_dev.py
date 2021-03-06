# B3LB - BigBlueButton Load Balancer
# Copyright (C) 2020-2021 IBH IT-Service GmbH
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License
# for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


from loadbalancer.settings_base import *

#####
# Missing parameters in settings_base
#####

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qz1%&75i+p)4yo92=w87bi9j&8vb5j=21^#(gjct-f0m0%hkdc'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Configure Celery
CELERY_BROKER_URL = 'amqp://user:password@localhost:5672/'

#####
# Optional overwrite default settings in settings_base
#####

DEBUG = True

ASSETS_FOLDER_URL = "https://localhost/logos"
API_BASE_DOMAIN = "localhost"
