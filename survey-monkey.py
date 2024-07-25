#!/usr/bin/env python3.12

import json
import argparse
import requests


def create_survey(data):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    survey_name = list(data.keys())[0]
    pages = data[survey_name]

    # Step 1: Create Survey
    survey_payload = {
        "title": survey_name
    }
    # Send POST request to create survey
    response = requests.post('https://api.surveymonkey.com/v3/surveys', headers=headers, json=survey_payload)
    # Get survey ID from response
    survey_id = response.json().get('id')
    
    # Test if survey was created successfully
    if not survey_id:
        print("Failed to create survey.")
        return

    # Step 2: Create Pages and Questions
    
    for page_name, questions in pages.items():
        page_payload = {
            "title": page_name,
            "description": "",
            "position": 1
        }

        # Send POST request to create page

        page_response = requests.post(f'https://api.surveymonkey.com/v3/surveys/{survey_id}/pages', headers=headers, json=page_payload)
        page_id = page_response.json().get('id')

        if not page_id:
            print(f"Failed to create page '{page_name}'.")
            continue

        for question_name, question_info in questions.items():
            question_payload = {
                "headings": [{"heading": question_name}],
                "family": "single_choice",
                "subtype": "vertical",
                "answers": {"choices": [{"text": ans} for ans in question_info["Answers"]]},
                "position": 1
            }
            question_response = requests.post(f'https://api.surveymonkey.com/v3/surveys/{survey_id}/pages/{page_id}/questions', headers=headers, json=question_payload)

            if not question_response.ok:
                print(f"Failed to create question '{question_name}'.")

        print(f"Survey '{survey_name}' created successfully.")
        print(survey_id)
        return survey_id

def create_contact_list(list_name):
    # Create headers
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    # Create payload for the contact list
    contact_list_payload = {
        "name": list_name
    } 
    # Make the API request to create the contact list
    response = requests.post('https://api.surveymonkey.com/v3/contact_lists', headers=headers, json=contact_list_payload)
    
    if response.ok:
        contact_list_id = response.json().get('id')
        print(f"Contact list created successfully. ID: {contact_list_id}")
        return contact_list_id
    else:
        print(f"Failed to create contact list: {response.text}")
        return None

def add_contacts_to_list(contact_list_id, contacts):
    # Create headers
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Add each contact to the contact list 
    for contact in contacts:
        data = {
            "email": contact["email"]
        }
        response = requests.post(f'https://api.surveymonkey.com/v3/contact_lists/{contact_list_id}/contacts', headers=headers, json=data)
    
        if response.ok:
            print("Contact added successfully.")
        else:
            print(f"Failed to add contacts: {response.text}")

parser = argparse.ArgumentParser(description='Survey Monkey CLI')
parser.add_argument('questions', type=str, help='Path to the question file')
parser.add_argument('emails', type=str, help='Path to the email file')

args = parser.parse_args() 

with open(args.questions) as f:
    questions = json.load(f)

with open(args.emails) as f:
    recipients = [{"email": email.strip()} for email in f.readlines() if email.strip()]


survey_id = create_survey(questions)
list_name = "Test_name_for_list"

contact_list_id = create_contact_list(list_name)
if contact_list_id:
    add_contacts_to_list(contact_list_id, recipients)

