from common_for_tests import multi_raster_16b
from telluric import GeoRaster2, MutableGeoRaster, GeoVector
from telluric.constants import MERCATOR_RESOLUTION_MAPPING



def test_as_mutable():
    raster = multi_raster_16b().as_mutable()
    assert isinstance(raster, MutableGeoRaster)

def test_construction_mutable_raster():
    raster = MutableGeoRaster.empty_from_roi(GeoVector.from_xyz(300,300,13), resolution=MERCATOR_RESOLUTION_MAPPING[13])
    print(type(raster))
    assert isinstance(raster, MutableGeoRaster)


