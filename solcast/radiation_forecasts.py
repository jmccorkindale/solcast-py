from datetime import datetime, timedelta
from urllib.parse import urljoin

from isodate import parse_datetime, parse_duration
import requests

from solcast.base import Base

class RadiationForecasts(Base):

    end_point = 'radiation/forecasts'

    def __init__(self, latitude, longitude, *args, **kwargs):

        self.latitude = latitude
        self.longitude = longitude
        self.forecasts = None

        self.params = {'latitude' : self.latitude,
                       'longitude' : self.longitude}

        self._get(*args, **kwargs)

        if self.ok:
            self._generate_forecast_dict()

    def _generate_forecast_dict(self):

        self.forecasts = []

        for forecast in self.content.get('forecasts'):

            forecast['period_end'] = parse_datetime(forecast['period_end'])
            forecast['period'] = parse_duration(forecast['period'])

            self.forecasts.append(forecast)