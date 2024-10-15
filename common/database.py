import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import datetime
from sqlalchemy.exc import IntegrityError
from common.loadJson import LoadJson


config=LoadJson()


app = Flask(__name__)     # creating flask instance


app.config['SQLALCHEMY_DATABASE_URI'] = config.json['db_remote']   #putting  the database link in the configuration of our app 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) #wrapping  the database with flask

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    gender = db.Column(db.String(6))
    district = db.Column(db.String(9))
    state = db.Column(db.String(9))
    pincode = db.Column(db.Integer)
    govt_id_type = db.Column(db.String(15))
    id_number = db.Column(db.String(15))

class Application(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    applicant_id = db.Column(db.String(99),)
    ownership = db.Column(db.String(99))
    load_applied = db.Column(db.Float)
    date_of_application = db.Column(db.Date)
    date_of_approval = db.Column(db.Date)
    modified_date = db.Column(db.Date)
    status = db.Column(db.String(99))
    reviewer_id = db.Column(db.Float)
    reviewer_Comments= db.Column(db.String(999))

class Reviewer(db.Model):
    id=db.Column(db.Integer)
    reviewer_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))                               #using db instances to crate the tables in db

# def process_excel_data(filename):
#     current_directory = os.path.dirname(__file__)
#     csv_file_path = os.path.join(current_directory, 'data', filename)
#     df = pd.read_csv(csv_file_path)
#     print("hi")


#     # print(os.getcwd())
#     # df = pd.read_csv(filename)
#     # target_date = datetime.datetime(2024, 1, 1)

#     replacement_date = datetime.datetime(1924, 1, 1)
#     # df.loc[df['Date_of_Approval'] == target_date, 'Date_of_Approval'] = replacement_date


#     # df['Date_of_Approval'].fillna(replacement_date, inplace=True)   gave error
#     df.fillna({'Date_of_Approval': replacement_date}, inplace=True)   #is resolution

#     df['Modified_Date'] = pd.to_datetime(df['Modified_Date'], format='%d-%m-%y').dt.strftime('%Y-%m-%d')
#     df['Date_of_Approval'] = pd.to_datetime(df['Date_of_Approval'], format='%d-%m-%y').dt.strftime('%Y-%m-%d')
#     df['Date_of_Application'] = pd.to_datetime(df['Date_of_Application'], format='%d-%m-%y').dt.strftime('%Y-%m-%d')
#     print(df['Modified_Date'])



#     # Iterate over rows and populate models
#     for index, row in df.iterrows():
#         # Create and add User instance
#         user = User(
#             id=row['ID'],
#             name=row['Applicant_Name'],
#             gender=row['Gender'],
#             district=row['District'],
#             state=row['State'],
#             pincode=row['Pincode'],
#             govt_id_type=row['GovtID_Type'],
#             id_number=row['ID_Number']
#         )
#         # print("user done")
#         db.session.add(user)
#         db.session.commit()


#         # Create and add Application instance


#         # Create and add Reviewer instance
#         existing_reviewer = Reviewer.query.filter_by(id=row['Reviewer_ID']).first()

#         if not existing_reviewer:
#             reviewer = Reviewer(
#             id=row['ID'],
#             reviewer_id=row['Reviewer_ID'],
#             name=row['Reviewer_Name']
#             )
#             db.session.add(reviewer)
#         try:
#             db.session.commit()
#             # print("reviewer done")
#         except IntegrityError:
#         # Handle the case where another process/thread added the same reviewer ID simultaneously
#             db.session.rollback()
#         # Optionally, you can log an error or take other actions here


#         application = Application(
#             id=row['ID'],
#             applicant_id=row['ID_Number'],  # Assuming ID is auto-generated
#             ownership=row['Ownership'],           
#             load_applied=row['Load_Applied (in KV)'],
#             date_of_application=row['Date_of_Application'],
#             date_of_approval=row['Date_of_Approval'],
#             modified_date=row['Modified_Date'],
#             status=row['Status'],
#             reviewer_id=row['Reviewer_ID'],
#             reviewer_Comments=row['Reviewer_Comments']
#         )
#         db.session.add(application)
#         print("application done ",index)
#         db.session.commit()


    # Commit the changes to the database
    # db.session.commit()

# Create the tables in the database
# with app.app_context():
#     # table = db.Model.metadata.tables.get('application')  # faking you cant derop reviewer bcoz of foreign key constraint you cant create aopplication bcoz of foreign key
#     # table.drop(db.engine)

#     db.drop_all()
#     db.create_all()
#     filename='electricity_board_case_study.csv'
#     process_excel_data(filename)
