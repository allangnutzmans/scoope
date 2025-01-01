# SCOOPE  

SCOOPE is a virtual microscope simulator developed as a web application.  

## Features  
- **Navigation between structures:** easily explore different regions of the samples.  
- **Real high-magnification images:** electron microscopy images captured directly from real samples.  
- **Structure identification:** tools to highlight and identify important parts of the images.  

## Partnerships  
This project was developed in partnership with:  
- **State University of Londrina (UEL)**  
- **Embryology Laboratory**  
- **Department of Computer Science**  

The electron microscopy images were produced and provided by the Embryology Laboratory at UEL, ensuring high quality and realism.  

## Technologies Used  
- **Backend:** Django  
- **Frontend:** HTML, CSS, and JavaScript  
- **Database:** [Specify the database used, e.g., PostgreSQL, SQLite, etc.]  
- **Other technologies:** [List specific libraries or tools used in the project, if applicable.]  

## How to Run the Project  
1. Clone this repository:  
   ```bash  
   git clone [Repository URL]  
```
	2.	Create a virtual environment and activate it:
   ```bash 
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
```
	3.	Install the dependencies:
   ```bash 
pip install -r requirements.txt     
``` 
	4.	Set up the database:
```bash
python manage.py migrate  
```
	5.	Run the development server:
```bash
python manage.py runserver  
```
	6.	Open the application in your browser:
```bash
http://127.0.0.1:8000  
```