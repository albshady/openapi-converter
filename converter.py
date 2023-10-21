import argparse
import json
import pathlib

import yaml


def main() -> None:
    parser = argparse.ArgumentParser(description="Accept a string as input.")
    parser.add_argument(
        "openapi_json",
        type=pathlib.Path,
        help="Path to openapi.json specification to be yamlified and camelCased",
    )
    args = parser.parse_args()
    content = args.openapi_json.read_text()
    yaml_spec = json_to_yaml(content)
    print(yaml_spec)


def json_to_yaml(raw_json: str) -> str:
    data = json.loads(raw_json)
    for path_detail in data['paths'].values():
        for method in path_detail:
            operation_id = path_detail[method]['operationId']
            path_detail[method]['operationId'] = snake_to_camel(operation_id)
    return yaml.safe_dump(data, indent=2)


def snake_to_camel(identifier: str) -> str:
    components = identifier.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


if __name__ == "__main__":
    main()
