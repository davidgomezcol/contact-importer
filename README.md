# Contact Importer

The application will allow users to upload contact files in CSV format and process them in order
to generate a unified contact file. The contacts must be associated with the user who imported
them into the platform. When uploading the files, the application must validate that the fields
entered are correctly formatted. You must take into account that the files can have many
records.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To run this project you will need to install Django and flake8 for tests...

```
pip install --upgrade pip
pip install Django==4.0.3
pip install flake==84.0.1
```

you also can install what is needed to run the app using the "requirements.txt" file by typing:

```
pip install -r requirements.txt
```

## Running the tests

To run the tests run the command as follows:

python manage.py test && Flake8

### Break down into end-to-end tests

There are a couple of unit test that can help you test the program if you modify or refactor the components.
There are tests for the user creation, contacts, etc.

Example:
```
     def test_that_an_user_is_created(self):
        """Test that an user is created successfully"""
        payload = {
            'email': 'test@test.com',
            'password': 'password123',
        }

        create_user(**payload)

        queryset = get_user_model().objects.get(id=1)

        self.assertEqual(queryset.email, payload['email'])
        self.assertTrue(queryset.check_password(payload['password']))
```

### Run the program

To run the program you just go to the core folder and run the following command:

```
python manage.py runserver
```

The csv file for test is placed in the "files" folder located in the root folder.

You can find credentials for the test user in the "docs" folder for you to test the app.

## Built With

* [Python](https://www.python.org/) - The Language used

## Authors

* **David Gomez** - *Initial work* - https://github.com/davidgomezcol/contact-importer

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details