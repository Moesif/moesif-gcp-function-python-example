# Moesif GCP Cloud Function Example for Python

[Moesif](https://www.moesif.com) is an API analytics platform.
[moesif-gcp-function-python](https://github.com/Moesif/moesif-gcp-function-python)
is a middleware that logs API calls to Moesif for GCP Cloud Function.

This example is a Python application with Moesif's API analytics and monitoring integrated.

## How to run this example.

Create a new GCP Cloud function from the console or command line and then deploy the function.

```
 gcloud functions deploy python-http-function \
--gen2 \
--runtime=python311 \
--region=<Your Region> \
--source=. \
--entry-point=hello_get \
--trigger-http
```

`Note: Replace the cloud region of the function`

You will also want to add an environment vairable `MOESIF_APPLICATION_ID` with the value being your 
application id from your Moesif account

Go to the URL of the Cloud function such as https://xxxx-xxxx.cloudfunctions.net/python-http-function

The API Calls should show up in Moesif.
