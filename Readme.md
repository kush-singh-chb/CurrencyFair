#Currency Fair Backend Task

#Reason
Used Flask since I am currently working with it, but i can implement the same in spring or node.js
Also flask with sqlachemy due to it being very light weight and holds a lot of cloud sdk resemblance.
in the near future if this has to be migrated it can be done with very less effort.

##how to setup
**Requires Python pre-installed <br>
Run the following command in your terminal.
```shell script
pip install -r requirement.txt
FLASK_APP=run.py
python -m flask run
```

##Flask

The '/save_trade' is the data ingestion route

The '/graph' will return a json string that will contain all the values for those currency

The '/get_currency' is a get method for getting distinct currencies.



##Javascript
The following is a lightweight implementation of the task using Flask and vanilla javascript.

The '/' will return a graph page and will require a to and from selection from the drop down.

The 'Submit' button load the graph using vanilla ajax and displays it using plotly.

The 'Stop' button will stop calling the api every 0.5 seconds


#####Note
The following was done in a very small timeframe.