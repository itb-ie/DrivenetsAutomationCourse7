import re
import pytest
import logging

logger = logging.getLogger(__name__)

regex_ipv4 = re.compile(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")

regex_ipv6 = re.compile(r"^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$")


def is_ipv4(ip):
    return regex_ipv4.match(ip)


def is_ipv6(ip):
    return regex_ipv6.match(ip)


@pytest.mark.parametrize("ip", ["1.2.3.4", "1::7", "5:4:3:2:1:0:0:0", "ab:cd::01:02"])
def test_ips(ip):
    assert is_ipv4(ip) or is_ipv6(ip)

@pytest.mark.parametrize("ip", ["1.2.323.4", "x1::7", "55:5:55:5:4:3:2:1:0:0:0", "ab:cd::ax1:02"])
def test_ips_negative(ip):
    assert not is_ipv4(ip) and not is_ipv6(ip)


@pytest.mark.parametrize(argnames="ip, ipv4", argvalues=[("1.2.3.4", True), ("1::7", False), ("5:4:3:2:1:0:0:0", False), ("ab:cd::01:02", False)])
def test_ips_2(ip, ipv4):
    if ipv4:
        logger.info(f"Validating that {ip} is ipv4")
        assert is_ipv4(ip)
    else:
        logger.info(f"Validating that {ip} is ipv6")
        assert is_ipv6(ip)

# using a dictionary
ips_to_test = {
    "ipv4": ["1.2.3.4", "55.55.55.55", "99.122.2.0"],
    "ipv6": ["1::1", "5:4:3:2:1:0:0:0", "1:af::3"]
}


@pytest.mark.parametrize(argnames="ip", argvalues=list(range(3)))
@pytest.mark.parametrize(argnames="ipv4", argvalues=[True, False])
def test_ips_3(ip, ipv4):
    if ipv4:
        logger.info(f'Testing ip {ips_to_test["ipv4"][ip]}')
        assert is_ipv4(ips_to_test["ipv4"][ip])
    else:
        assert is_ipv6(ips_to_test["ipv6"][ip])
        logger.info(f'Testing ip {ips_to_test["ipv6"][ip]}')


@pytest.mark.parametrize(argnames="type_ip, ip", argvalues=[(type, ip) for type, ips in ips_to_test.items() for ip in ips])
def test_ips_4(ip, type_ip):
    if type_ip == "ipv4":
        assert is_ipv4(ip)
    else:
        assert is_ipv6(ip)
