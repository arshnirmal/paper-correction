# Automated-paper-correction

End to end solution for hassle free paper correction, for universities/teachers/students

## Usage

Clone the repo

    git clone https://parthchudasama@bitbucket.org/parthchudasama/paper-correction.git`
	cd paper-correction


## Installation
**We suggest you create a new envionment**
```bash
pip install -r requirements.txt
```
## Run

```python
python app.py
```
The app will be available at  `127.0.0.1:5000/`

## Application description 
The application is divided in to 4 steps
### Step 1:
1. In step 1 the user is required to upload the student answers.
2. Only PDF and Images are supported at the moment 
3. All the student answers are saved locally in a folder 'student_files' this folder is created in runtime and is temporary. We also provide an option to upload files to cloud if required.

![picture](https://bitbucket.org/parthchudasama/paper-correction/raw/a84cc7c98a1c97a86f2be15b18a9d2766025c7f2/static/screenshots/Step%201.png)

### Step 2:
1. In step 2 user is required to upload a master copy, the data provided in step 1 will be checked  against master copy i.e the original asnswers.
![picture](https://bitbucket.org/parthchudasama/paper-correction/raw/a84cc7c98a1c97a86f2be15b18a9d2766025c7f2/static/screenshots/Step%202.png)

### Step 3:
Handwriting recognition from google vision is not 100% acuracte. We have ensured through tests that the accuracy remains acceptable by means of image preporcessing. To further ensure that the words and sentences are detected correctly, we recommend user to upload material that has been used to refer by students (Reference book, papers etc)
![picture](https://bitbucket.org/parthchudasama/paper-correction/raw/a84cc7c98a1c97a86f2be15b18a9d2766025c7f2/static/screenshots/step%203.png)

### Step 4:
The last step generates a zip file where results are each student are stored along with deatailed review of each paper. 
Please be patient at this step as it might take a while depending upon the network connection.
![picture](https://bitbucket.org/parthchudasama/paper-correction/raw/a84cc7c98a1c97a86f2be15b18a9d2766025c7f2/static/screenshots/step%204.png)

### Test run
In order to test application, we have provided some test files which are present in `test_files` folder.

1. Select any Image/PDF in step 1
2. Select `master_file.txt` in step 2
3. Select `correction_file.txt` in step 3


## License

[MIT](https://choosealicense.com/licenses/mit/)


## License

[MIT](https://choosealicense.com/licenses/mit/)
