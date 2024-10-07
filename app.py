from flask import Flask
from flask_cors import CORS

app =Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return "API Flask"

@app.route('/api/Config/GetOrganizationMap')
def GetOrganizationMap():
    return "ruta para OrganizationMap"

@app.route('/api/Config/GetWindMap')
def GetWindMap():
    return "ruta para GetWindMap"

@app.route('/api/Config/GetAssetsMap')
def GetAssetsMap():
    return "ruta para GetAssetsMap"

@app.route('/api/Config/GetDiagramList') 
def GetDiagramList():
    return "ruta para GetDiagramList"

@app.route('/api/Config/GetImages360Map') 
def GetImages360Map():
    return "ruta para GetImages360Map"

@app.route('/api/Config/GetOrientedImageryMap')
def GetOrientedImageryMap():
    return "ruta para GetOrientedImageryMap"

@app.route('/api/Config/GetAerialImagesMap') 
def GetAerialImagesMap():
    return "ruta para GetAerialImagesMap"

@app.route('/api/Config/GetOpticalSensorsMap') 
def GetOpticalSensorsMap():
    return "ruta para GetOpticalSensorsMap"

@app.route('/api/Config/GetDiagramMap')
def GetDiagramMap():
    return "ruta para GetDiagramMap"

@app.route('/api/Config/GetFacilityMap') 
def GetFacilityMap():
    return "ruta para GetFacilityMap"

@app.route('/api/Config/GetCCTVMap') 
def GetCCTVMap():
    return "ruta para GetCCTVMap"

@app.route('/api/Config/GetEmissionsLayer') 
def GetEmissionsLayer():
    return "ruta para GetEmissionsLayer"

@app.route('/api/Config/GetMatterportLayer') 
def GetMatterportLayer():
    return "ruta para GetMatterportLayer"

# Iride IOT

@app.route('/api/IrideIOT/GetLastValue') 
def GetLastValue():
    return "ruta para GetLastValue"


@app.route('/api/IrideIOT/GetAllValuePress') 
def GetAllValuePress():
    return "ruta para GetAllValuePress"


@app.route('/api/IrideIOT/GetAllValuesTemp') 
def GetAllValuesTemp():
    return "ruta para GetAllValuesTemp"

if __name__== "__main__":
    app.run()
    