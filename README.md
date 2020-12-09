# Data Engineering Bootcamp (IGTI)

## Project 01 - enade
The Enade - Exame Nacional de Desempenho dos Estudantes (National Student Performance Exam) evaluates the performance of students of university courses.

In this project, there is the extraction of data from Enade 2019, which are available on the website [Microdados Inep](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enade) in zip format.

Understanding the data you are working with is an important part of data engineering. So, an analysis of the data is made, such as the **Descriptive Statistics** of the fields using **describe()**, **filters using loc[]**, **groupings with groupby**, **aggregations like mean()** and **replacement of values using replace()**.

## Project 02 - twitter
Programming a Crawler for streaming tweets: Implements a **Stream Listener for Twitter** where a list of words to be monitored is informed. Each time there is a new tweet with one of the words this tweet is collected and **saved in a json file**.

In the transformation step, we **read the .json** file that contains the extracted tweets, **select the relevant data** and **convert it to the Pandas DataFrame format**.

We use a **config.ini** file to store the Twitter API access tokens as well as the database **access credentials**. The **DBMS used is Postgresql**.

We use the **os library** to standardize the file path and **ConfigParser() to read the .ini** file. There are no passwords or tokens directly in the script, only in the .ini file (not available in this repository for security reasons).

The **sqlalchemy library** helps us to **load the DataFrame into Postgresql**.