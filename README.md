Data Science Master class: Advanced software engineering
University: Berliner Hochschule für Technik (BHT)
Project name: Book recommendation system
Project author: Polina Kozyr


PROJECT DESCRIPTION
The goal of the project is to create a simple book recommendation system based on the genre and author analysis. The user enters his name and surname and a book that he has already read and liked. Based on data of this book other books recommendations are calculated. Project is a pet one and may be concerned as a small service of some big recommendation system. For now recommendations are evaluated only by one book that user entered. Maybe in the future this system could be expanded and possibility of taking into account several books for recommendation will be implemented. 

* Dataset with 54000 plus books was used.
Metadata can be found here:
https://www.kaggle.com/datasets/meetnaren/goodreads-best-books?select=book_data.csv
The dataset was taken from Kaggle and contained book titles, authors, genres, descriptions, and ratings. The data from the csv file has been put into the database.

1. **Use and understand Git!**<br />
You can see that the project is on Git-hub and check version control.

2. **UML at least 3 good different diagrams. "good" means you can pump it up artificially as written in DDD. \
You have 10 million $ from me! Please export the pics. I can not install all tools to view them!**<br />

[Use case diagram](https://github.com/polinatrump/book_recommendation/blob/master/Use_case_diagram.svg)<br />
[Activity diagram](https://github.com/polinatrump/book_recommendation/blob/master/Activity_diagram.svg)<br />
[Entity Relationship Diagram](https://github.com/polinatrump/book_recommendation/blob/master/Entity%20Relationship%20Diagram.jpg)<br />
[Object diagram](https://github.com/polinatrump/book_recommendation/blob/master/Object%20Diagram.jpg)

3. **DDD If your domain is too small, invent other domains around and document these domains (as if you have 100 Mio € from Edlich-Investment!) Develop a clear strategic design with mappings/relationships with >4 Domains coming from an Event Storming. Drop your Domains into a Core Domain Chart and indicate the Relations between the Domains!**<br />

Firstly I made Event Storming diagram, defined domain events and commands and reactions for them.

Please, after you go to the link click on Download - picture will not be downloaded on your computer but these way \ 
you can see full picture <br />
[Event Storming](https://github.com/polinatrump/book_recommendation/blob/master/EventStorming.jpg)<br />

Then based on Event Storming I made DDD:<br />
[Domain and Subdomain Relationships](https://github.com/polinatrump/book_recommendation/blob/master/DDD.jpg)<br />

4. **Metrics at least two. Sonarcube would be great. Other non-trivial metrics are also fine.**<br />
 I downloaded and installed Sonarcube and used it for my project.<br />
* Here you can see Sonarcube results:  <br />
[Sonarcube screenshot](https://github.com/polinatrump/book_recommendation/blob/master/Sonarcube.jpg)<br />

* Bugs: 0
* Vulnerabilities: 0
* Security Hotspot: 1 <br /> I checked by myself this moment and it is okay
* Code Smells: 16
There are issues like [that](https://github.com/polinatrump/book_recommendation/blob/master/Sonarcube_Code_smell.jpg), so after manual check I think it's okay to leave it like this<br />
* Coverage: I used [coverage report](https://github.com/polinatrump/book_recommendation/blob/master/Coverage.jpg)<br />
Coverage is 66 % for my project.

5. **Clean Code Development: at least 5 points you can show me + >>10 points on your personal cheat sheet**<br />

My personal cheet sheet :<br />

* Use descriptive intention revealing names - it's important to write code easy and readable. So [here](https://github.com/polinatrump/book_recommendation/blob/master/dataset_preprocessing.py#L85-L86) I used simple for cycle and you as a person who sees this project for the first time it is easy to understand code
* Don't repeat one code twice - Code should have a single, unambiguous, authoritative representation within a system. <br />
I wrote a function [here](https://github.com/polinatrump/book_recommendation/blob/master/dataset_preprocessing.py#L56-L58) that split values in column. I have two different columns (genres and authors) that I \
have to split and I didn't write code twice for each column but use just one function for this task
* You Aren't Gonna Need It - In my code I don't have variables and functions that I don't use - checked with Sonarcube
* Create the names of variables, functions and classes that way, that you can understand what they are for easily in the future - [example](https://github.com/polinatrump/book_recommendation/blob/master/src/models/BookModel.py#L22)
* The code should be easily testable
* Tests should be easy to understand and easy to change - see my tests [here](https://github.com/polinatrump/book_recommendation/blob/master/tests/unit/services/test_services.py#L6-L151)
* Use docstring (example [here](https://github.com/polinatrump/book_recommendation/blob/master/src/repository/author_repository.py#L13-L17)) to ealsily understand what each method or class does, its role and responsibility 
* Write Exceptions for some cases to easily understand if one certain error occurs - example [here](https://github.com/polinatrump/book_recommendation/blob/master/src/exceptions/author_exceptions.py#L3-L14) 
* Avoid using ambiguous shorthand. A variable should have a long descriptive name than a short confusing name.
* Don’t use magic numbers. Magic numbers are numbers with special, hardcoded semantics that appear in code but do not have any meaning or explanation. Usually, these numbers appear as literals in more than one location in our code. An example in my code [here](https://github.com/polinatrump/book_recommendation/blob/master/src/services/SearchNeighbours.py#L111)
* Single responsibility principle. Classes and functions should do one thing and do it well. It's good to write short and simple functions that perform a single task. My examples [here](https://github.com/polinatrump/book_recommendation/blob/master/dataset_preprocessing.py#L48-L81)


6. **Build Management with any Build System as Ant, Maven, Gradle, etc. (only Travis is perhaps not enough) Do e.g. generate Docs, call tests, etc. (it could be also disconnected from the project just to learn a build tool!)**<br />
The pyinstaller library was used as build management, which allows you to build python code into executable files ([link](https://github.com/polinatrump/book_recommendation/blob/master/run.exe)). For this, the pyinstaller --onefile run.py command was used. You can see output for this command [here](https://github.com/polinatrump/book_recommendation/blob/master/pyinstaller_launch.txt). This command collects the source files that are required to run run.py into a single executable file and creates the dist and build directories. The dist folder contains various files that the builder creates as it builds. In the dist folder, respectively, is the executable file itself. It is important that the executable must be rebuilt every time if the program is to be run on a different CPU architecture.

7. **Integrate some nice Unit-Tests in your Code to be integrated into the Build**<br />
[Unit tests](https://github.com/polinatrump/book_recommendation/blob/master/tests/unit/services/test_services.py) cover the main logic. Under the main logic of the application, an algorithm that looks for K nearest neighbors is implied. Since this was the main part of the applications around, which included the rest of the parts, I considered it important to cover this part with tests. Also, in order for the tests to always use the same source data, [fixtures for domain models](https://github.com/polinatrump/book_recommendation/tree/master/tests/fixtures/domain) were written. Test [coverage](https://github.com/polinatrump/book_recommendation/blob/master/Coverage.jpg) was 66%.

8. **Continuous Delivery: show me your pipeline using e.g. Jenkins, Travis-CI, Circle-CI, GitHub Action, GitLab CI, etc. E.g. you can also use Jenkins Pipelining or BlueOcean, etc. But at least insert more than 2 script calls as done in the lecture! (e.g. also call Ant or Gradle or something else).**<br />
Jenkins [file here](https://github.com/polinatrump/book_recommendation/blob/master/Jenkinsfile) is used for automated testing and deployment builds. For this, a pipeline is used, which describes the different stages of this entire process. Then first name of the agent is specified. The agent is a separate process in which the actions described in the pipeline are performed. In our case, the agent is a separate docker container, i.e. when pipeline is launched, a separate container is created in which subsequent commands are executed. Parameter pollSCM allows to monitor changes in the GitHub repository and if there is a new commit there, it starts the whole process. Next come the stages. In the first stage that is called Build dependencies and libraries are being installed. Then the testing stage goes, just so that tests all pass successfully. And the last thing, an executable file is being built if everything is ok at the previous stages. If one of the stages fails, the subsequent ones will not be executed.

9. **Use a good IDE and get fluent with it: e.g. IntelliJ. What are your favorite Key-Shortcuts?!**<br />

I developed my project in PyCharm IDE. The Key-Shortcuts that I actually used are:
* ctrl+/ --> Comment/uncomment current line or selected block with line comments
* When i have to change one certain code or variable everywhere where it is I press Ctrl+F than write code in search window than press Ctrl+Alt+Shift+J to select all occurrences and edit them at a time
* Double Shift --> Search everywhere any file, class, variable, symbol in project and current Git repository
* Shift + F10 --> Run the script
* Shift + F9 --> I use Debug for study errors in code
* Alt + Enter --> to import library or class in python file
* Developers can create database in PyCharm and easily see tables and write queries. For this press 'Database'. Ctrl+Shift+Q to get to Query Console, Ctrl+F5 to refresh Database

10. **DSL Create a small DSL Demo example snippet in your code even if it does not contribute to your project (hence it can also be in another language).**<br />
Using the click library, a DSL interface was created to run the program ([file here](https://github.com/polinatrump/book_recommendation/blob/master/src/entrypoints/DSLUserInterface.py)). This mode involves passing input parameters through flags. Command here: python run_dsl.py --first_name=1 --last_name=2 --book_title='The Hunger Games' --recommend_count=2

11. **Functional Programming: prove that you have covered all functional aspects in your code as:
only final data structures
(mostly) side effect free functions
the use of higher-order functions
functions as parameters and return values
use closures / anonymous functions
You can also do it outside of your project. Even in another language as F#, Clojure, Julia, etc.**<br />

In file [FP.py](https://github.com/polinatrump/book_recommendation/blob/master/FP.py) you can see simple example of user interface functions, where I used higher-order functions and functions as parameters and return values. They are all final data structures. There is almost no side effect except _recom_num_ variable. The example of anonymous function you can find [here](https://github.com/polinatrump/book_recommendation/blob/master/src/services/SearchNeighbours.py#L29).