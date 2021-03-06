import os as _os

api_key = _os.environ.get('SOLCAST_API_KEY')

from .pv_power_forecasts import PvPowerForecasts as get_pv_power_forecasts
from .pv_power_estimated_actuals import PvPowerEstimatedActuals as get_pv_power_estimated_actuals
from .radiation_forecasts import RadiationForecasts as get_radiation_forecasts
from .radiation_estimated_actuals import RadiationEstimatedActuals as get_radiation_estimated_actuals
from .rooftop_site import RooftopSite as post_rooftop_site
from .rooftop_measurement import RooftopMeasurement as post_rooftop_measurement
from .rooftop_measurements import RooftopMeasurements as post_rooftop_measurements

from .pv_power_forecasts import PvPowerForecasts
from .pv_power_estimated_actuals import PvPowerEstimatedActuals
from .radiation_forecasts import RadiationForecasts
from .radiation_estimated_actuals import RadiationEstimatedActuals
from .rooftop_site import RooftopSite
from .rooftop_measurement import RooftopMeasurement
from .rooftop_measurements import RooftopMeasurements

