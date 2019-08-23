# API REST for Aivo

This web application is used to filter countries according to indexs provided by the user. It can be extended easily by adding new routes on controllers folder.

## Project hierarchy

misc/  
|-> input_file.csv  
|-> script.sql  
src/  
|-> controllers/  
    |-> routes.py  
|-> models/  
    |-> indicators.py  
test/  
|-> unit/  
    |-> pytest.ini  
    |-> test_countries.py  
main.py  