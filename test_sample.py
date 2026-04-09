cat > /var/jenkins_home/test_sample.py <<'PY'
import pytest
from python_org_page import PythonOrgPage

@pytest.mark.parametrize("keyword, should_have_results", [
    ("pycon", True),
    ("selenium", True),
    ("zzzz_no_result_keyword_12345", False),
])
def test_python_search(driver, keyword, should_have_results):
    page = PythonOrgPage(driver)

    page.open()
    assert page.title_contains_python()

    page.search(keyword)

    if should_have_results:
        assert not page.has_no_results()
    else:
        assert page.has_no_results()
PY