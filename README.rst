==========================
AWS Healthchecker Response
==========================

This is a custom middleware for django that will return a 200 response with the content 'OK' to an AWS ELB Health Checker request. This exists because you can't set the HTTP host header for the ELB health check and so django rejects the request because the IP's are not in ALLOWED_HOSTS.

Installation
------------

The easiest way to install the package is via ``pip``::

    $ pip install aws-healthchecker-response

Usage
-----

Add ``aws_healthchecker_response`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        'aws_healthchecker_response',
        ...
    )

Add the middleware class to the top of your django ``MIDDLEWARE``::

    MIDDLEWARE = (
        'aws_healthchecker_response.middleware.AWSHealthCheckerResponseMiddleware',
        ...
    )

You can customise the list of User-Agents the middleware responds to adding to ``AWS_HEALTH_CHECKER_USER_AGENT``::

    AWS_HEALTH_CHECKER_USER_AGENT = (
        "ELB-HealthChecker/2.0",
        "AnotherMonitoringService/1.0",
    )

Copyright & License
-------------------

Copyright (c) 2018, Matt Magin. MIT License.
