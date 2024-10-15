from datetime import datetime
from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from common.loadJson import LoadJson






from common.database import Application, User,Reviewer





class ApiServiceController:                               #providing services to handle endpoints, enabling resource/db access here

    def __init__(self) -> None:
        config = LoadJson()

        self.DATABASE_URL = config.json['db_remote']      # configirring db to be used ....can be found in coomon/configFiles/config.json
        self.engine = create_engine(self.DATABASE_URL,pool_size=10,
                                      max_overflow=2,
                                      pool_recycle=300,
                                      pool_use_lifo=True,
                                      pool_pre_ping=True)
        
        self.SessionLocal = sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=self.engine)

  
    def retrieve_all_connections(self):
        db=self.SessionLocal()     #creating Session per request
        try:
            applications = db.query(Application).order_by(Application.id.asc()).all()

            application_list = []
            for application in applications:
                application_data = {                    
                    'id': application.id,
                    'applicant_id': application.applicant_id,
                    'ownership': application.ownership,
                    'load_applied': application.load_applied,
                    'date_of_application': application.date_of_application.isoformat(),
                    'date_of_approval': application.date_of_approval.isoformat(),
                    'modified_date': application.modified_date.isoformat(),
                    'status': application.status,
                    'reviewer_id': application.reviewer_id,
                    'reviewer_comments': application.reviewer_Comments
                    }
                application_list.append(application_data)          #putting the json objects  retrieved from table to application_list list
        finally:
            db.close()                                               #closing session after request  is done

        
        
        return JSONResponse(application_list)
        
    
    async def get_user_by_id(self, request: Request):

        user_id = request.query_params.get('user_id')

        db=self.SessionLocal()   #creating Session per request
        try:

            user = db.query(User).get(user_id)

            if user:
                user_data = {
                    'id': user.id,
                    'name': user.name,
                    'gender': user.gender,
                    'district': user.district,
                    'state': user.state,
                    'pincode': user.pincode,
                    'govt_id_type': user.govt_id_type,
                    'id_number': user.id_number
            }
            
                return JSONResponse(user_data)
            else:
                return JSONResponse({'error': 'User not found'}), 404
        finally:
            db.close()                              #closing session after request  is done
            



    async def get_application_by_id(self, request: Request):
        json_payload = await request.json()
        application_id = json_payload.get('user_id')
        db=self.SessionLocal()                       #creating Session per request
        try:
        
            application = db.query(Application).get(application_id)

            if application:
                application_data={
                    "id": application.id,
                    "applicant_id": application.applicant_id,
                    "ownership": application.ownership,
                    "load_applied": application.load_applied,
                    "date_of_application": application.date_of_application.isoformat(),
                    "date_of_approval": application.date_of_approval.isoformat(),
                    "modified_date": application.modified_date.isoformat(),
                    "status": application.status,
                    "reviewer_id": application.reviewer_id,
                    "reviewer_comments": application.reviewer_Comments
                }
            
                return JSONResponse(application_data)
            else:
                return JSONResponse({'error': 'User not found'}), 404
        finally:
            db.close()                                #closing session after request  is done

        

    async def get_reviewer_by_id(self, request: Request):

        reviewer_id = request.query_params.get('reviewer_id')

        db=self.SessionLocal()                                  #creating Session per request
        try:
            reviewer = db.query(Reviewer).get(reviewer_id)
    
            if reviewer_id:
                reviewer_data={
                    "id": reviewer.id,
                    "name": reviewer.name
            }
            
                return JSONResponse(reviewer_data)
            else:
                return JSONResponse({'error': 'User not found'}), 404
        finally:
            db.close()                  #closing session after request  is done
        



    async def update_application(self, request: Request):
        new_application_data = await request.json()
        application_id = new_application_data.get('id')
        date_format = '%Y-%m-%d'                                          #changing date format for it to fit in postgresql
        db=self.SessionLocal()                                            #creating Session per request
        try:
            application_to_delete = db.query(Application).get(application_id)
            
            if application_to_delete:
                db.delete(application_to_delete)
                db.commit()
                print("deleted")

                new_application = Application(
                    id=application_id,  
                    applicant_id=new_application_data['applicant_id'],
                    ownership=new_application_data['ownership'],
                    load_applied=new_application_data['load_applied'],
                    date_of_application=datetime.strptime(new_application_data['date_of_application'], date_format),
                    date_of_approval=datetime.strptime(new_application_data['date_of_approval'], date_format),
                    modified_date=datetime.strptime(new_application_data['modified_date'], date_format),
                    status=new_application_data['status'],
                    reviewer_id=new_application_data['reviewer_id'],
                    reviewer_Comments=new_application_data['reviewer_comments']
                )
                db.add(new_application)
                db.commit()

                return JSONResponse({'message': 'Application updated successfully'}), 200
            else:
                return JSONResponse({'error': 'Application not found'}), 404
        finally:
            db.close()                          #closing session after request  is done
    


    