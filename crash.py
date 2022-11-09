#!/usr/bin/env python3
import asyncio
import bellows.types
import bellows.zigbee.application


async def main():
    app = bellows.zigbee.application.ControllerApplication({
        "backup_enabled": False,
        "device": {
            "path": "socket://localhost:9999"
        },
        "ezsp_config": {
            # Do not set any configuration on startup
            "CONFIG_END_DEVICE_POLL_TIMEOUT": None,
            "CONFIG_INDIRECT_TRANSMISSION_TIMEOUT": None,
            "CONFIG_TC_REJOINS_USING_WELL_KNOWN_KEY_TIMEOUT_S": None,

            "CONFIG_SECURITY_LEVEL": None,
            "CONFIG_APPLICATION_ZDO_FLAGS": None,

            "CONFIG_SUPPORTED_NETWORKS": None,
            "CONFIG_PAN_ID_CONFLICT_REPORT_THRESHOLD": None,

            "CONFIG_TRUST_CENTER_ADDRESS_CACHE_SIZE": None,
            "CONFIG_SOURCE_ROUTE_TABLE_SIZE": None,
            "CONFIG_MULTICAST_TABLE_SIZE": None,
            "CONFIG_ADDRESS_TABLE_SIZE": None,
            "CONFIG_PACKET_BUFFER_COUNT": None,

            # This is the only config option actually set
            # "CONFIG_STACK_PROFILE": None,
        }
    })

    try:
        await app.connect()
        await app.initialize(auto_form=False)

        # Ensure you have a relatively large Zigbee network formed, with a few dozen
        # routers and end-devices. This seems necessary to trigger the assertion.
        while True:
            await app._ezsp.getMfgToken(bellows.types.EzspMfgTokenId.MFG_CUSTOM_EUI_64)
    finally:
        await app.disconnect()


if __name__ == "__main__":
    import coloredlogs
    coloredlogs.install(level="DEBUG")

    asyncio.run(main())
