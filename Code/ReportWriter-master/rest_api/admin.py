# @OPENSOURCE_HEADER_START@
# MORE Tool 
# Copyright 2016 Carnegie Mellon University.
# All Rights Reserved.
#
# THIS SOFTWARE IS PROVIDED "AS IS," WITH NO WARRANTIES WHATSOEVER.
# CARNEGIE MELLON UNIVERSITY EXPRESSLY DISCLAIMS TO THE FULLEST EXTENT
# PERMITTEDBY LAW ALL EXPRESS, IMPLIED, AND STATUTORY WARRANTIES,
# INCLUDING, WITHOUT LIMITATION, THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT OF PROPRIETARY
# RIGHTS.
#
# Released under a modified BSD license, please see license.txt for full
# terms. DM-0003473
# @OPENSOURCE_HEADER_END@
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from models import RESTConfiguration

admin.site.register(RESTConfiguration, SingletonModelAdmin)

