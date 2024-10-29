import boto3

iot = boto3.client('iot')

def create_iot_topic_rule(topic_name):
    rule_payload = {
        "sql": f"SELECT * FROM 'traffic/sensors/{topic_name}'",
        "ruleDisabled": False,
        "actions": []
    }
    response = iot.create_topic_rule(
        ruleName=topic_name,
        topicRulePayload=rule_payload
    )
    return response