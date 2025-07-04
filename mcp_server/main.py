# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T09:00:20+00:00



import argparse
import json
import os
from typing import *

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity, HTTPBasic

app = MCPProxy(
    contact={
        'email': 'developer-experience@adyen.com',
        'name': 'Adyen Developer Experience team',
        'url': 'https://www.adyen.help/hc/en-us/community/topics',
        'x-twitter': 'Adyen',
    },
    description='Adyen sends notifications through webhooks to inform your system that reports were generated and are ready to be downloaded.\n\nYou can download reports programmatically by making an HTTP GET request, or manually from your [Balance Platform Customer Area](https://balanceplatform-test.adyen.com/balanceplatform).',
    termsOfService='https://www.adyen.com/legal/terms-and-conditions',
    title='Report webhooks',
    version='1',
    servers=[{'url': 'https://balanceplatform-api-test.adyen.com/bcl/v1'}],
)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
