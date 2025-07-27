
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import FileResponse
import os

class CTeethApp:
    def __init__(self):
        self.app = FastAPI(title="CTeeth API")
        self._add_routes()

    def _add_routes(self):
        @self.app.get("/api/scans")
        def get_scans():
            files = os.listdir("data")
            return {"scans": files}
        
        @self.app.get("/api/scans/{filename}")
        def get_scan(filename):
            files = os.listdir("data")
            if filename not in files:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail="File Not Found")
            return FileResponse(
                "data/"+filename,
                media_type="application/dicom",
                filename=filename
            )

    def get_app(self):
        return self.app

cteeth_app = CTeethApp()
app = cteeth_app.get_app()
