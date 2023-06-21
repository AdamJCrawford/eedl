import ee
import pytest

from ee import ImageCollection

# we should change the name of our Image class - it conflicts with the class image in the ee package, and people will likely be using both. Let's not cause confusion
import ee_download


def test_simple():
	geometry = ee.FeatureCollection("users/nrsantos/vw_extraction_mask").geometry()
	s2_image = ImageCollection("COPERNICUS/S2_SR_HARMONIZED").filterBounds(geometry).filterDate("2022-07-01", "2022-07-14").first().select(["B8",])

	# Adam, make sure to set the drive root folder for your own testing - we'll need to fix this, and in the future,
	# we can use a Google Cloud bucket for most testing
	# this is clunky - we should make the instantiation of the image be able to take a kwarg that sets the value of image, I think.
	image = ee_download.Image(drive_root_folder=r"G:\My Drive")
	image.export(s2_image, "valley_water_s2_test_image", export_type="Drive", clip=geometry)

	# We need to make it check and report whether the export on the EE side was successful. This test "passed" because
	# Earth Engine failed and there wasn't anything to download (oops)
	# Adam, make sure to set the folder you want results to be downloaded to
	ee_download.image.main_task_registry.wait_for_images(r"D:\ee_export_test", sleep_time=60, callback="mosaic")