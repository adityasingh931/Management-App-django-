import logging
from django.shortcuts import render
from rest_framework import viewsets, status
from .models import *
from rest_framework.response import Response
from .serializers import ManagerSerializer, EmployeeSerializer
from django.utils.translation import gettext as _


logger = logging
# Create your views here.
class ManagerViewset(viewsets.ModelViewSet):
    model = Manager
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    def create(self, request, **args):
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
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        try:
            pagination_data = None
            page = self.paginate_queryset(self.filter_queryset(self.get_queryset().order_by('first_name')))
            if page is not None:
                serializer = self.serializer_class(
                    page, many=True)
                pagination_data = self.get_paginated_response(serializer.data)
            else:
                serializer = self.serializer_class(
                    self.filter_queryset(self.get_queryset().order_by('first_name')), many=True)
            context = {
                "success": True, "message": _("Record details returned successfully."), "data": serializer.data, "pagination_data": pagination_data}

            return Response(context, status=status.HTTP_200_OK)
        except Exception as error:
            context = {'error': str(error), 'success': False, 'message': _(
                'Failed to return record.')}
            
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, pk=None):
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
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
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
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
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
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EmployeeViewset(viewsets.ModelViewSet):
    model = Employee
    query_set = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def create(self, request, **args):
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
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        try:
            pagination_data = None
            page = self.paginate_queryset(self.filter_queryset(self.get_queryset().order_by('first_name')))
            if page is not None:
                serializer = self.serializer_class(
                    page, many=True)
                pagination_data = self.get_paginated_response(serializer.data)
            else:
                serializer = self.serializer_class(
                    self.filter_queryset(self.get_queryset().order_by('first_name')), many=True)
            context = {
                "success": True, "message": _("Record details returned successfully."), "data": serializer.data, "pagination_data": pagination_data}

            return Response(context, status=status.HTTP_200_OK)
        except Exception as error:
            context = {'error': str(error), 'success': False, 'message': _(
                'Failed to return record.')}
            
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, pk=None):
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
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
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
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
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
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)