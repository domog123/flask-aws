# Flask-MySQL-Docker to AWS Registration of Voter's in the Philippines

Create an instance EC2 with Key Pair ppk to establish connection in Putty ssh

Create Security Groups 
Port 5000 
Port 3306 for MySQL
Port 22 for SSH

Install docker, mysql, and github in the instance

git clone https://github.com/domog123/flask-aws.git
cd flask-aws

run the docker 

sudo docker-compose up --build -d

Open the form in 

http://YOUR_AWS_PUBLIC_IP:5000

Input the form and the form will be saved in the mysql 

to check the database 

sudo docker exec -it mysql_db mysql -uroot -proot

SHOW DATABASES;
USE flaskdb;

SELECT * FROM users;








