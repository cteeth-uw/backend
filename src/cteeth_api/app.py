
from fastapi import FastAPI

class CTeethApp:
    def __init__(self):
        self.app = FastAPI(title="CTeeth API")
        self._add_routes()

    def _add_routes(self):
        @self.app.get("/scans")
        def get_scans():
            return {"scans": ["scan1", "scan2", "scan3"]}

    def get_app(self):
        return self.app

cteeth_app = CTeethApp()
app = cteeth_app.get_app()
