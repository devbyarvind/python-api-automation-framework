try:
    import pytest
except ImportError as exc:
    raise ImportError(
        "pytest is not installed in the active Python environment. "
        "Install it with: python -m pip install pytest"
    ) from exc
from datetime import datetime
import os

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    config.option.html = f"{report_dir}/report_{now}.html"


@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("Starting")
    yield
    print("End")


