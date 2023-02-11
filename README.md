Data Science Master class: Advanced software engineering
University: Berliner Hochschule für Technik (BHT)
Project name: Book recommendation system
Project author: Polina Kozyr


PROJECT DESCRIPTION
The goal of the project is to create a simple book recommendation system based on the genre and author analysis. \
The user enters his name and surname and a book that he has already read and liked. Based on data of this book \
other books recommendations are calculated. Project is a pet one and may be concerned as a small service \
of some big recommendation system. For now recommendations are evaluated only by one book that user entered. Maybe in \
the future this system could be expanded and possibility of taking into account several books for recommendation \
will be implemented. 

Как описать что мы создали бд и что в каждом файле \
- надо ли это вообще

Как утановить и запустить проект

* Dataset with 54000 plus books was used.
Metadata can be found here:
https://www.kaggle.com/datasets/meetnaren/goodreads-best-books?select=book_data.csv

1. **Use and understand Git!**
You can see that the project is on Git-hub and check version control.

2. **UML at least 3 good different diagrams. "good" means you can pump it up artificially as written in DDD. \
You have 10 million $ from me! Please export the pics. I can not install all tools to view them!**

Use_case_diagram: https://github.com/polinatrump/Book_recommendation_system/blob/main/Use_case_diagram.svg
Activity_diagram: https://github.com/polinatrump/Book_recommendation_system/blob/main/Activity_diagram.svg
Entity Relationship Diagram: https://github.com/polinatrump/Book_recommendation_system/blob/main/Entity%20Relationship%20Diagram.jpg
Object_diagram: https://github.com/polinatrump/Book_recommendation_system/blob/main/Object%20Diagram.jpg

3. **DDD If your domain is too small, invent other domains around and document these domains (as if you have 100 Mio € from Edlich-Investment!) Develop a clear strategic design with mappings/relationships with >4 Domains coming from an Event Storming. Drop your Domains into a Core Domain Chart and indicate the Relations between the Domains!**

Firstly I made Event Storming diagram, defined domain events and commands and reactions for them.

Please, after you go to the link click on Download - picture will not be downloaded on your computer but these way \ 
you can see full picture
Event Storming: https://github.com/polinatrump/Book_recommendation_system/blob/main/EventStorming.jpg

Then based on Event Storming I made DDD:

Domain and Subdomain Relationships: https://github.com/polinatrump/Book_recommendation_system/blob/main/DDD.jpg

4. **Metrics at least two. Sonarcube would be great. Other non-trivial metrics are also fine.**
 I downloaded and installed Sonarcube and used it for my project.
* Here you can see results:  
добавить картинку с сонаркьюба
Вывод продублировать

5. **Clean Code Development: at least 5 points you can show me + >>10 points on your personal cheat sheet**

My personal cheet sheet :

* Use descriptive intention revealing names - it's important to write code easy and readable. So here I used simple for cycle and you as a \
person who sees this project for the first time it is easy to understand code
* Don't repeat one code twice - Code should have a single, unambiguous, authoritative representation within a system. 
I wrote a function здесь that split values in column. I have to different columns (genres and authors) that I \
have to split and i don't write code twice for each column but use just one function for this task
* You Aren't Gonna Need It - In my code I don't have variables and functions that I don't use in my code
* Create the names of variables, functions and classes that way, that you can understand what they are for easily in the future
* The code should be easily testable
* Tests should be easy to understand and easy to change
* Use docstring to ealsily understand what each method or class does, its role and responsibility 
* Write Exceptions for some cases to easily understand if one certain error occurs 
* Avoid using ambiguous shorthand. A variable should have a long descriptive name than a short confusing name.
* Don’t use magic numbers. Magic numbers are numbers with special, hardcoded semantics that appear in code but do not have any meaning or explanation. Usually, these numbers appear as literals in more than one location in our code. An example in my code here
* Classes and functions should do one thing and do it well. It's good to write short and simple functions that perform a single task. My example here
* Single responsibility principle 

6. **Build Management with any Build System as Ant, Maven, Gradle, etc. (only Travis is perhaps not enough) Do e.g. generate Docs, call tests, etc. (it could be also disconnected from the project just to learn a build tool!)**

7. **Integrate some nice Unit-Tests in your Code to be integrated into the Build**

8. **Continuous Delivery: show me your pipeline using e.g. Jenkins, Travis-CI, Circle-CI, GitHub Action, GitLab CI, etc. E.g. you can also use Jenkins Pipelining or BlueOcean, etc. But at least insert more than 2 script calls as done in the lecture! (e.g. also call Ant or Gradle or something else).**

9. **Use a good IDE and get fluent with it: e.g. IntelliJ. What are your favorite Key-Shortcuts?!**

I developed my project in PyCharm IDE. The Key-Shortcuts that I actually used are:
* ctrl+/ --> Comment/uncomment current line or selected block with line comments
* When i have to change one certain code or variable everywhere where it is I press Ctrl+F than write code in search window than press Ctrl+Alt+Shift+J to select all occurrences and edit them at a time
* Double Shift --> Search everywhere any file, class, variable, symbol in project and current Git repository
* Shift + F10 --> Run the script
* Shift + F9 --> I use Debug for study errors in code
* Developers can create database in PyCharm and easily see tables and write queries. For this press 'Database'. Ctrl+Shift+Q to get to Query Console, Ctrl+F5 to refresh Database

10. **DSL Create a small DSL Demo example snippet in your code even if it does not contribute to your project (hence it can also be in another language).**

11. **Functional Programming: prove that you have covered all functional aspects in your code as:
only final data structures
(mostly) side effect free functions
the use of higher-order functions
functions as parameters and return values
use closures / anonymous functions
You can also do it outside of your project. Even in another language as F#, Clojure, Julia, etc.**