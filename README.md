# Weather-Visualisation-Scenario-using-InfluxDB-Grafana-Python
### Summary:
Visualizing the weather for different areas.

### Goals:
Getting introduction to Python.
Getting introduction to data visualization tools.

### Tools:
* [Python 2.7+](https://www.python.org/)
* [InfluxDB](https://portal.influxdata.com/downloads) as time series database.
* [Grafana](https://grafana.com/) as Graphics dashboard.

### Details:
- The consumer requests frequently (every 10 min) about the weather for two different areas from [openweathermap.org](openweathermap.org), then store the response in InfluxDB.  
- Grafana queries the data from InfluxDB and visualizes it.

### InfluxDB settings:
- You can install InfluxDB from [HERE](https://docs.influxdata.com/influxdb/v1.2/introduction/installation/)
- After installation and to start influx type in the teminal: `$ influx`
- Then create the Database: `> CREATE DATABASE ws_db` "*ws_db*" is the name of the database which you could insert data in it.
- You can check your databases using: `> SHOW DATABASES `
- The default influxdb port is "8086", the default username is "root" and the default password is "root".
- For users management see the [influxdb documentation](https://docs.influxdata.com/influxdb/v1.2/query_language/authentication_and_authorization/#user-management-commands)

### Running the Application:
- Run the python file as a service to work in background:   `nohup python -m get_weather.py &`
- Now the application requests about weather and inserts the data in influx database.  


### Grafana settings:
- Install Grafana from [HERE](https://grafana.com/grafana/download)
- Start Grafana using web browser by enter: `localhost:3000` in the address
- The default Grafana user name is "admin" and the The default password is "admin".
- Add data source by selecting the *type of database* `InfluxDB` and specifying the *Url* `localhost:8086` or that define where the InfluxDB run. Should also provide the *name of database* whitch you already have created *ws_db*, in addition to *username* and *password*.
- Import the json file [dashboard configuration](https://github.wdf.sap.corp/D069020/Weather-Visualisation-Scenario-using-InfluxDB-Grafana-Python/files/2056/Grafana-Dashboard-Weather-configration.json.zip) to Grafana to get our dashboard which visualizes the weather, or create your own.  

![alt tag](https://github.wdf.sap.corp/storage/user/24134/files/bce8828c-148a-11e7-902a-1276f85c0262)
