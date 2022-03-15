import csv
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.files.storage import FileSystemStorage

from .helpers.validators import validate_phone, card_type, \
    validate_name, validate_date, validate_email

from contacts.models import Contacts
from logs.models import FilesStatus

ROW_COUNT = ""


def update_file_status(status_id, status):
    """Creates a log entry for status"""
    update_status = FilesStatus.objects.get(id=status_id)
    update_status.status = status
    update_status.save()
    return update_status


def home_view(request):
    """Home Page"""
    return render(request, 'pages/home.html')


@login_required(login_url='login')
def upload_file_view(request):
    """Upload file page and retrieve headers"""
    data = {}
    global ROW_COUNT
    if request.method == "GET":
        return render(request, "pages/upload-file.html", data)

    try:
        if request.FILES:
            csv_file = request.FILES['csv_file']
            request.session['csv'] = str(csv_file)
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'File is not CSV type')
                return redirect('upload-file')

            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            data['fieldnames'] = reader.fieldnames
            data['filename'] = csv_file.name

            fs = FileSystemStorage()
            fs.save(csv_file.name, csv_file)

            file = FilesStatus.objects.create(
                user=request.user,
                file_name=csv_file.name,
            )

            ROW_COUNT = sum(1 for row in reader)

            request.session['file_status'] = file.id
        else:
            messages.error(request, 'No file was selected.')
            return redirect('upload-file')
    except IOError:
        return messages.error(request, 'Could not read file')
    return render(request, 'pages/upload-file.html', data)


@login_required(login_url='login')
def process_uploaded_file(request):
    """Process the file to save data to database"""
    fs = FileSystemStorage()
    filename = ""
    counter = 0
    global ROW_COUNT

    if request.method == 'POST':
        try:
            filename = request.POST.get('filename')
            csv_file = fs.open(name=filename)

            dict_fields = dict(request.POST)

            name, birthday, phone, address, \
                credit_card, email = "", "", "", "", "", ""

            fields = dict_fields['correct_field']
            for field in fields:
                if field == "name":
                    name = fields.index(field)
                if field == "birthday":
                    birthday = fields.index(field)
                if field == "phone":
                    phone = fields.index(field)
                if field == "address":
                    address = fields.index(field)
                if field == "credit_card":
                    credit_card = fields.index(field)
                if field == "email":
                    email = fields.index(field)

            decoded_file = csv_file.read().decode('utf-8').splitlines()
            readers = csv.DictReader(decoded_file)

            if ROW_COUNT >= 1:
                for reader in readers:
                    update_file_status(
                        status_id=request.session['file_status'],
                        status="Processing"
                    )
                    name_value = list(reader.values())[name]
                    name_valid = validate_name(name_value)
                    if name_valid is None:
                        messages.error(
                            request,
                            f"{name_value} couldn't be saved. "
                            f"Wrong Name format."
                        )
                        continue
                    birthday_value = list(reader.values())[birthday]
                    birthday_valid = validate_date(birthday_value)
                    if birthday_valid is None:
                        messages.error(
                            request,
                            f"{name_value} couldn't be saved. "
                            f"Wrong Birth Date format."
                        )
                        continue
                    phone_value = list(reader.values())[phone]
                    phone_valid = validate_phone(phone_value)
                    if phone_valid is None:
                        messages.error(
                            request,
                            f"{name_value} couldn't be saved. "
                            f"Wrong Phone number format."
                        )
                        continue
                    address_value = list(reader.values())[address]
                    credit_card_value = list(reader.values())[credit_card]
                    email_value = list(reader.values())[email]
                    email_valid = validate_email(email_value)
                    if email_valid is None:
                        messages.error(
                            request,
                            f"{name_value} couldn't be saved. "
                            f"Wrong Email format."
                        )
                        continue
                    email_exists = Contacts.objects.filter(
                        user=request.user, email=email_value
                    )
                    if email_exists:
                        messages.error(
                            request,
                            f"{name_value} couldn't be saved. "
                            f"Email already exists."
                        )
                        continue
                    franchise = card_type(credit_card_value)
                    Contacts.objects.create(
                        user=request.user,
                        name=name_valid,
                        date_of_birth=birthday_valid,
                        phone=phone_value,
                        address=address_value,
                        credit_card=credit_card_value,
                        email=email_value,
                        franchise=franchise,
                    )
                    counter += 1

            else:
                messages.error(request, f"The file {csv_file.name} is empty.")

            if counter == 0:
                update_file_status(
                    status_id=request.session['file_status'],
                    status="Failed"
                )
            else:
                update_file_status(
                    status_id=request.session['file_status'],
                    status="Finished"
                )

            messages.add_message(
                request,
                messages.INFO,
                f"{counter} contacts were saved successfully"
            )

            fs.delete(filename)

        except ValueError:
            fs.delete(filename)
            return messages.error(request, 'Data could not be saved.')

    return redirect('contacts')
