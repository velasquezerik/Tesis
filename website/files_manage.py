from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required,user_passes_test
from rolepermissions.shortcuts import assign_role, remove_role
from rolepermissions.verifications import has_permission, has_role
from rolepermissions.decorators import has_role_decorator
from roles import SystemAdmin, SystemUser
from models import UserImage, Folder, File
from tesis.settings import *
import os
import shutil

#create folder
def create_folder(root, name):
	directory = root +"/"+ name
	print directory
	if not os.path.exists(directory):
		try:
			os.makedirs(directory)
		except Exception, e:
			return False
		else:
			return True
		

#create folder
def create_root_folder(user_id):
	root = MEDIA_ROOT
	user = User.objects.get(id=user_id)
	directory = root +"/"+ user.username
	print directory
	if not os.path.exists(directory):
		try:
			folder = Folder()
			folder.name = user.username
			folder.path = directory
			folder.user = user
			folder.save()
			os.makedirs(directory)
		except Exception, e:
			return False
		else:
			return True
		

#create new folder
def create_new_folder(user_id,father_id,name):
	root = MEDIA_ROOT
	user = User.objects.get(id=user_id)
	father = Folder.objects.get(id=father_id)
	directory = father.path +"/"+ name
	id_folder = 0
	print directory
	if not os.path.exists(directory):
		try:
			folder = Folder()
			folder.name = name
			folder.path = directory
			folder.user = user
			folder.father = father.id
			folder.active = True
			folder.save()
			id_folder = folder.id
			os.makedirs(directory)
		except Exception, e:
			return id_folder
		else:
			return id_folder

#create new folder
def edit_folder(user_id,folder_id,name):
	root = MEDIA_ROOT
	user = User.objects.get(id=user_id)
	folder = Folder.objects.get(id=folder_id)
	father = Folder.objects.get(id=folder.father)
	directory = father.path +"/"+ name

	os.rename(folder.path,directory)

	folder.name = name
	folder.path = directory
	folder.save()
	return True



#delete folder
def delete_folder(user_id, folder_id):
	root = MEDIA_ROOT
	user = User.objects.get(id=user_id)
	folder = Folder.objects.get(id=folder_id)
	father = Folder.objects.get(id=folder.father)
	directory = father.path +"/"+ name

	shutil.rmtree(folder.path)

	folder.delete()

	return True


#create new file
def create_file(name, folder_id):
	root = MEDIA_ROOT
	folder = Folder.objects.get(id=folder_id)
	# Open a file
	f = open(folder.path + "/" + name, "w")
	# Close opend file
	f.close()

	file = File()
	file.name = name
	file.folder = folder
	file.active = True
	file.save()

	return True

#upload files
def upload_file(name, folder_id, f):
	root = MEDIA_ROOT
	folder = Folder.objects.get(id=folder_id)
	# create a file
	with open(folder.path + "/" + name, 'w') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

	file = File()
	file.name = name
	file.folder = folder
	file.active = True
	file.save()

	return True