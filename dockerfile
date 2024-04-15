# Use the official Python image as the base image
ARG REPO_NAME=local_library
FROM python:3.12

# These set environment variables to prevent Python from writing pyc files 
# and ensure that Python's standard output is sent directly to the terminal without buffering.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /locallibrary_tutorial

# Copy the requirements file to the working directory
COPY requirements.txt /locallibrary_tutorial

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /locallibrary_tutorial/
COPY . /locallibrary_tutorial
