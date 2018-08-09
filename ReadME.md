# Log Analysis
The third project of the Udacity _Full Stack Nanodegree_. The purpose for this project is to build an informative summary from logs for a large database.

## Prerequisites
Virtual Machine (VM) 
Vagrant 
Python3
##### Virtual Machine 
Download and Install the platform package for your operating system from [here](hhttps://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
##### Vagrant
Download and Install vagrant from [here](https://www.vagrantup.com/downloads.html).

## How to Run?
From your terminal `cd` into the vagrant directory and do the following.
1. Start the Virtual Machine.
`vagrant up` 
Then 
`vagrant ssh`
2. Connect to the news database and execute the SQL file for creating the view.
`psql -d news -f view_creation.sql`
**OR**
Connect to the database
`psql -d news`
Then execute this SQL 
* `CREATE VIEW day_requests AS (
SELECT date(time) as day,COUNT(*) as requests, COUNT(CASE WHEN status LIKE '4%' THEN 1 END) AS error
FROM log
GROUP BY day );`
3. Run the program.
`python3 analysis.py`
And wait a few moments.