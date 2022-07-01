Coverage 98%
# CRUD Application for a book shop review site.

<h1>Overview</h1>
This application for a book review site allows user to add books to the database, read them from the database, update the books in the database or delete them from the dadtabase. It also allows the ability to add, read, update and delete reviews they have of the books in the database.

This was for a QA project week. We were tasked with creating a CRUD application which utilises supporting tools, methodologies and technologies that have been taught throught the course so far. It must show our knowledge on Project Management, Python Fundamentals, Python Testing, Git, Basic Linux, Python Web Development, Continuous Integration, Cloud Fundamentals and Databases. 

Challenges that were faced came mostly in the Jenkins side of the application. It was the first time I have used Jenkins with an application like this so getting it installed and setup to run it was tricky. I still haven't managed to complete the build in Jenkins, however, the application still runs on the browser and Jenkins runs the necessary pytests. I tried to set it up as a systemd server but with no luck in the time limits.

Looking forward, trying to set up the application as a systemd server would be ideal to ensure the build finishes. Furthermore, I would like to expand this application further. Adding a customers table (with user identification) and orders table allow the book shop not only to provide reviews to books but also sell on the website. 

<h1>Getting Started</h1>
Prerequisites:
This application was created using a virtual machine from GCP connected to Visual Studio Code by ssh key configuration. An account for GCP or equivelant will be needed to run this as well as downloading VSCode.
GCP - https://cloud.google.com
VSCode downlaod: https://code.visualstudio.com/download


Installation:
Setting up in VSCode:
  Open a new bash terminal and run the command 'ssh-keygen'
  Delete the known hosts by running 'rm .ssh/known_hosts'
  View the ssh key by running 'cat .ssh/id_rsa.pub
  Copy this ssh key
  Run the command 'sudo visudo'
    Insert 'jenkins ALL=(ALL:ALL) NOPASSWD:ALL' under Sudo User
  
When setting up the VM:
  ensure that the base disk is Ubuntu with minumum 20.04 LTS.
  machine type minimum e2-medium.
  firewall rules allow port 5000 and 8080 to be open.
  Insert the ssh key into the network key.
  
Once VSCode and VM are connected via ssh key, clone down this despository git@github.com:gregorule/book_shop.git.
Use the setup.sh file to update the environment but running './setup.sh'.
Run 'chmod +x jenkins.sh' and './jenkins.sh' to install Jenkins.
Once the initial password is displayed (can take 5-10 mins) copy it.
Put the external IP of the VM into a new tab with ':8080' after it.
Insert the initial password.
Install suggested plugins.
Create a new job on Jenkins making sure to add the git-hub repository where necessary.
Copy the contents of forJenkins.txt and add it into build shell.
Use the external IP of the VM again in a new tab but with ':5000' at the end instead to use the app.

<h1>Testing</h1>
Jenkins will run the integration and unit tests that the application has.

Unit Testing:

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        
Integration Testing:

class TestAdd(TestBase):
    def test_book_add(self):
        response = self.client.post(
            url_for('addBooks'),
            data = dict(book_name="James and the Giant Peach",author_name="Roald Dahl",pages=160,genre="Fantasy")
        )
        assert Books.query.filter_by(book_name="James and the Giant Peach").first().book_id == 2
        assert len(Books.query.all()) == 2
        
<h1>Entity Relationship Diagram</h1>
My original ERD design was kept basic to make sure the MVP was met:
![2022-06-23 (2)](https://user-images.githubusercontent.com/104358226/176905496-2070ced9-c1a3-476c-8582-614dd387039a.png)
![2022-06-23 (2)](https://user-images.githubusercontent.com/104358226/176905761-2ac445dc-29f0-4691-b373-42628524df3f.png)


For future implications, the ERD would look something like this:
![2022-07-01 (4)](https://user-images.githubusercontent.com/104358226/176905266-014692b5-8c6f-4a0e-bc96-12e9020b5843.png)




<h1>Authors</h1>
Gregor Rule

<h1>Acknowledgments</h1>
I'd like to that Ryan Wright and Victoria Sacre for their help on this project.








