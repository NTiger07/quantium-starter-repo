from Task_4 import app

def test_header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#title", timeout=10)
    
def test_graph(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#graph", timeout=10)
    
def test_radio(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#radio", timeout=5)
        