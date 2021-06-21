from twarc import Twarc2, expansions
import json

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():
    # Remove existing rules
    existing_rules = client.get_stream_rules()
    if 'data' in existing_rules and len(existing_rules['data']) > 0:
        rule_ids = [rule['id'] for rule in existing_rules['data']]
        client.delete_stream_rule_ids(rule_ids)

    # Add new rules
    new_rules = [
        {"value": "covid OR covid19 lang:en", "tag": "covid-related-tweets"},
        {"value": "corona OR coronavirus", "tag": "corona-related-tweets"}
    ]
    added_rules = client.add_stream_rules(rules=new_rules)

    # Connect to the stream
    for count, result in enumerate(client.stream()):
        tweet = expansions.flatten(result)
        print(json.dumps(tweet))
        # Replace with the desired number of Tweets
        if count > 100:
            break

    # Delete the rules
    rule_ids = [rule['id'] for rule in added_rules['data']]
    client.delete_stream_rule_ids(rule_ids)


if __name__ == "__main__":
    main()
