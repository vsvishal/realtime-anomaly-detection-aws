#!/usr/bin/env python3

from aws_cdk import core

from anomaly_detection_data_streams.anomaly_detection_data_streams_stack import \
    AwsAnomalyDetectionDataStreamsStack

app = core.App()
AwsAnomalyDetectionDataStreamsStack(app, "anomaly-detection-data-streams")

app.synth()
