// introduction This project is a Flask application where i used Docker to create its image and run it through a container.
//Steps used
As a first step Docker should be installed on the machine that you're using for verification : docker --version should be working
2-Git should be installed as well / or you can just upload the repository from github 
3- Clone the repository using : "git clone https://github.com/ineeees/Interview.git" 
4- to build the docker image you should be under /Interview : cd Interview 
5- Build the docker image : docker build -t interviewopt . 
6- Run the docker container : docker run -p 5000:5000 interviewopt 
7- Access to the application via : http://127.0.0.1:5000 where you should automatically try the query http://127.0.0.1:5000/api/stats?ticker=MSFT&start=2023-01-01&end=2023-12-31
