# realtime-anomaly-detection-aws

Realtime anomaly detection using aws

If you prefer to deploy it manually, you can clone this repo and use [AWS Cloud Development Kit (CDK)](https://aws.amazon.com/cdk/), with the following commands:
Manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

You will see in the `cdk.out` folder the generated CloudFormation Template. To deploy it run the following command:

```
$ cdk deploy
```

To see the full documentation on how to start the data producer and the analytics application, checkout the article on BigData Insider.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
