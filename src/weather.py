import csv


class Weather:
    def __init__(self):
        self.data = None
        self.lowest_temperature_row = None
        self.highest_fluctuation_station = None

    @staticmethod
    def calculate_fluctuation(last_temperature, current_temparature):
        fluctuation = None
        if last_temperature > current_temparature:
            fluctuation = last_temperature - current_temparature
        else:
            fluctuation = current_temparature - last_temperature
        return fluctuation

    def load_data(self, csv_filename):
        '''
        # Sample data structure.
        {
            'station_id': {
                'last_temperature_value': 3.33
                'temperature_fluctuation': 1.11,
                'data': {
                    'date1': 2.22,
                    'date2': 3.33,
                }
            }
        }
        '''
        self.data = {}
        self.lowest_temperature_row = None
        self.highest_fluctuation_station = None

        with open(csv_filename) as file_reader:
            csv_reader = csv.DictReader(file_reader)
            for idx, row in enumerate(csv_reader):
                row['date'] = float(row['date'])
                row['temperature_c'] = float(row['temperature_c'])
                if row['station_id'] in self.data:
                    self.data[row['station_id']]['data'].update({
                        row['date']: row['temperature_c']
                    })
                    self.data[row['station_id']]['temperature_fluctuation'] += self.calculate_fluctuation(
                        self.data[row['station_id']]['last_temperature_value'], row['temperature_c']
                    )
                    self.data[row['station_id']]['last_temperature_value'] = row['temperature_c']
                else:
                    self.data[row['station_id']] = {
                        'last_temperature_value': float(row['temperature_c']),
                        'temperature_fluctuation': 0,
                        'data': {
                            row['date']: row['temperature_c']
                        }
                    }

                if idx == 0:
                    self.lowest_temperature_row = row
                else:
                    if self.lowest_temperature_row['temperature_c'] > row['temperature_c']:
                        self.lowest_temperature_row = row

        self.highest_fluctuation_station = max(
            [(key, value['temperature_fluctuation']) for key, value in self.data.items()], key=lambda x:x[1]
        )

    def get_minimum_temperature_station_date(self):
        return {'station_id': self.lowest_temperature_row['station_id'], 'date': self.lowest_temperature_row['date']}

    def get_maximum_fluctuation_station(self):
        return self.highest_fluctuation_station[0]

    def get_maximum_fluctiation_date_range(self, start_date, end_date):
        start_date = float(start_date)
        end_date = float(end_date)
        temperature_data = {
            'station_id': {'fluctuation': 0, 'last_temperature_value': 0}
        }
        for station_id, data in self.data.items():
            for date, temperature in data['data'].items():
                if start_date <= date <= end_date:
                    if station_id in temperature_data:
                        temperature_data[station_id]['fluctuation'] += self.calculate_fluctuation(
                            temperature_data[station_id]['last_temperature_value'], temperature
                        )
                    else:
                        temperature_data[station_id] = {'fluctuation': 0, 'last_temperature_value': temperature}
        highest_fluctuation_station = max(
            [(key, value['fluctuation']) for key, value in temperature_data.items()], key=lambda x:x[1]
        )
        return highest_fluctuation_station[0]
