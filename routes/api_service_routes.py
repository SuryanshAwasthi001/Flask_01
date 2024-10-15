from fastapi import FastAPI
from controller.api_service_controller import ApiServiceController


class ApiServiceRoutes:                 #mapping endpoints to the right service to deal with

    def __init__(self,app) -> None:
        self.app=app
        self.version = "/api/v1/"
        self.apiServiceController = ApiServiceController()

    def initialize(self):
        self.app.add_api_route(self.version + "connections/getAll", self.apiServiceController.retrieve_all_connections, methods=["GET"])
        self.app.add_api_route(self.version + "connections/get_user", self.apiServiceController.get_user_by_id, methods=["GET"])
        self.app.add_api_route(self.version + "connections/get_application", self.apiServiceController.get_application_by_id, methods=["GET"])
        self.app.add_api_route(self.version + "connections/update_application", self.apiServiceController.update_application, methods=["POST"])
        self.app.add_api_route(self.version + "connections/get_reviewer", self.apiServiceController.get_reviewer_by_id, methods=["GET"])

