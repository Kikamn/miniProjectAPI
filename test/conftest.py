import pytest

from setting.case_management import update_test_result


@pytest.fixture(scope='function', autouse=True)
def hook(request):
    # BEFORE TEST
    print("=================== BEFORE TEST =================")
    get_error = request.session.testsfailed

    yield
    # AFTER TEST
    print("=================== AFTER TEST =================")
    status = request.session.testsfailed - get_error
    test_caseID = request.node.get_closest_marker("QaseIO").args[0] # nama.a nyamain di case management
    #print(f"Markers Sekarang : {test_caseID}")
    # print(f"hasil result : {test_result}")

    if status == 0:
        update_test_result(test_caseID, "passed")

    else:
        update_test_result(test_caseID, "failed")

@pytest.fixture(scope='session', autouse=True)
def suite(request):
    # BEFORE SUITE
    print(" =============== Before All =============== ")

    yield
    # AFTER SUITE
    print(" =============== After All =============== ")
