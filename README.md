<br />

  <h3 align="center">Project: Data Modelling with Postgres</h3>

  
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
         <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
   
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

1. Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.
2. State and justify your database schema design and ETL pipeline.
3. [Optional] Provide example queries and results for song play analysis.


A music streaming app startup "Sparkify" is collecting the data about user activity on their app. the user activities are collected as JSON logs on their stream server.

To understand the users demand and behaviour to improve the app and make it more user relevant, the analytics team wants to build a database to load these JSON user activity logs and able to write queries on adhoc basis to analyze the captured data.

### Database modelling design

we decided to build the database using PostgreSQL. As it is open source Database aswell and the requirement to satisfy the adhoc analytical queries and aggregation requirement can be best supported by a RDBM database 

* conceptual modelling
As part of the data modelling excersie we identified following entities to be required
1. Songs
2. users
3. Artists 
4. time 

Then we decided to build the data model using star schema as this is best model faster analytical capabilities for adhoc queries and also best suited for analysis. 
* logical modelling
 ![Star schema](/images/Star_datamodel.png)

* Physical modelling

![sql queries](/sql_querues.py)

we will use Python to build our ETL pipeline as this is new language which provides lot of functionalities to read data and also integrate in future into any orchestration tool like airflow

### Built With


* [Python](https://www.python.org/)
* [PostgreSQL](https://www.postgresql.org/)


## Getting Started
1. go to terminal run the below command to create database and required tables 

![create_tables](/images/create_tables.png)

![ETL](/images/etl.png)
