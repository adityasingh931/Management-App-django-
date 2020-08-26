import logging
from django.shortcuts import render
from rest_framework import viewsets, status
from .models import *
from rest_framework.response import Response
from .serializers import ManagerSerializer, EmployeeSerializer
from django.utils.translation import gettext as _
from rest_framework.decorators import action


# Create your views here.
class ManagerViewset(viewsets.ModelViewSet):
    model = Manager
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    def create(self, request, **args):
        logging.info("requested to create Manager")
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                obj = serializer.save()
                context = {"success": True, "message": _("Record has been added successfully."), "data": serializer.data}
                return Response(context, status=status.HTTP_200_OK)
            context = {'error': serializer.errors, "success": False, "message": _("Failed to create new record.")}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            context = {'error': str(error), 'success': False, 'message': _('Failed to add record.')}
            logging.error("Failed to add record.")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        logging.info("requested the list of Manager")
        try:
            serializer = self.serializer_class(
                self.filter_queryset(self.get_queryset().order_by('first_name')), many=True)
            context = {
                "success": True, "message": _("Record details returned successfully."), "data": serializer.data}

            return Response(context, status=status.HTTP_200_OK)
        except Exception as error:
            context = {'error': str(error), 'success': False, 'message': _(
                'Failed to return record.')}
            logging.error("Failed to return record ")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, pk=None):
        logging.info("requested to update the Manager of id {}".format(pk))
        try:
            try:
                obj = self.model.objects.get(id=pk)
            except Exception as error:
                context = {'error': str(error), 'success': False, 'message': _('ID not found')}
                return Response(context, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                context = {"success": True, "message": _("Record updated successfully"), "data": self.serializer_class(obj).data}
                return Response(context, status=status.HTTP_200_OK)
            context = {'error': serializer.errors, "success": False, "message": _("Failed to update Record.")}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            context = {'error': str(error), 'success': False, 'message': _('Failed to update Record.')}
            logging.error("Failed to update Record.")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        logging.info("requested to retrieve the Manager of id {}".format(pk))
        try:
            try:
                obj = self.model.objects.get(id=pk)
            except Exception as error:
                context = {'error': str(error), 'success': False, 'message': _('ID not found')}
                return Response(context, status=status.HTTP_404_NOT_FOUND)
            context_data = {"request_user":request.user}
            serializer = self.serializer_class(obj)
            context = {"success": True, "message": _("Record retrieved successfully"), "data": serializer.data}
            return Response(context, status=status.HTTP_200_OK)
        except Exception as error:
            context = {'error': str(error), 'success': False, 'message': _('Failed to retrieve Record.')}
            logging.error("Failed to retrieve Record.")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        logging.info("requested to delete the Manager of id {}".format(pk))
        try:
            try:
                obj = self.get_object()
            except Exception as error:
                context = {'error': str(
                    error), 'success': False, 'message': _('ID not found')}
                return Response(context, status=status.HTTP_404_NOT_FOUND)

            self.perform_destroy(obj)

            context = {
                "success": True, "message": _("Record deleted successfully."), "data": None}
            
            return Response(context, status=status.HTTP_200_OK)

        except Exception as error:
            context = {'error': str(error), 'success': False,
                       'message': _('Failed to delete record.')}
            logging.error("Failed to delete record.")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'], name="login")
    def login(self, request):
        logging.info("Manager requested to login.")
        try:
            data = request.data
            
            obj = Manager.objects.filter(email= data["email"]).filter(password=data["password"])
            if len(obj) == 0:
                context = {'error': str('Authentication Fail.'
                ), 'success': False, 'message': _('Email/password does not matches.')}
                return Response(context, status=status.HTTP_404_NOT_FOUND)

            serializer = self.serializer_class(obj[0])
            context = {
                "success": True, "message": _(""), "data": serializer.data}
            logging.error("Manager login Failed.")
            return Response(context, status=status.HTTP_200_OK)

        except Exception as error:
            context = {'error': str(error), 'success': False,
                       'message': _('Email/password does not matches.')}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EmployeeViewset(viewsets.ModelViewSet):
    model = Employee
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def create(self, request, **args):
        logging.info("requested to create the Employee list")
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                obj = serializer.save()
                context = {"success": True, "message": _("Record has been added successfully."), "data": serializer.data}
                return Response(context, status=status.HTTP_200_OK)
            context = {'error': serializer.errors, "success": False, "message": _("Failed to create new Record.")}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            context = {'error': str(error), 'success': False, 'message': _('Failed to add Record.')}
            logging.error("Failed to add Record.")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        logging.info("requested for the Employee list")
        try:
            serializer = self.serializer_class(
                self.filter_queryset(self.get_queryset().order_by('employee_id')), many=True)
            context = {
                "success": True, "message": _("Record details returned successfully."), "data": serializer.data}

            return Response(context, status=status.HTTP_200_OK)
        except Exception as error:
            context = {'error': str(error), 'success': False, 'message': _(
                'Failed to return record.')}
            logging.error("Failed to return record.")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, pk=None):
        logging.info("requested to update Employee list {}".format(pk))
        try:
            try:
                obj = self.model.objects.get(employee_id=pk)
            except Exception as error:
                context = {'error': str(error), 'success': False, 'message': _('ID not found')}
                return Response(context, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                context = {"success": True, "message": _("Record updated successfully"), "data": self.serializer_class(obj).data}
                return Response(context, status=status.HTTP_200_OK)
            context = {'error': serializer.errors, "success": False, "message": _("Failed to update Record.")}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            context = {'error': str(error), 'success': False, 'message': _('Failed to update Record.')}
            logging.error("Failed to update Record.")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        logging.info("requested for the Employee list of id {}".format(pk))
        try:
            try:
                obj = self.model.objects.get(employee_id=pk)
            except Exception as error:
                context = {'error': str(error), 'success': False, 'message': _('ID not found')}
                return Response(context, status=status.HTTP_404_NOT_FOUND)
            context_data = {"request_user":request.user}
            serializer = self.serializer_class(obj)
            context = {"success": True, "message": _("Record retrieved successfully"), "data": serializer.data}
            return Response(context, status=status.HTTP_200_OK)
        except Exception as error:
            context = {'error': str(error), 'success': False, 'message': _('Failed to retrieve Record.')}
            logging.error("Failed to retrieve Record.")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        logging.info("requested to delete the Employee of id {}".format(pk))
        try:
            try:
                obj = self.get_object()
            except Exception as error:
                context = {'error': str(
                    error), 'success': False, 'message': _('ID not found')}
                return Response(context, status=status.HTTP_404_NOT_FOUND)

            self.perform_destroy(obj)

            context = {
                "success": True, "message": _("Record deleted successfully."), "data": None}
            
            return Response(context, status=status.HTTP_200_OK)

        except Exception as error:
            context = {'error': str(error), 'success': False,
                       'message': _('Failed to delete record.')}
            logging.error("Failed to delete record.")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
