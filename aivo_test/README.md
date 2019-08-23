# API REST for Aivo

This web application is used to filter countries according to indexs provided by the user. It can be extended easily by adding new routes on controllers folder.

## Project hierarchy

misc/  
|-> input_file.csv  
|-> script.sql  
src/  
|-> controllers/  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-> routes.py  
|-> models/  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-> indicators.py  
test/  
|-> unit/  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-> pytest.ini  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-> test_countries.py  
main.py  